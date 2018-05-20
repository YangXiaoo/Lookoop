# coding: utf-8

import os, sys, time, re
from Crypto.Cipher import AES
import crypt
import pwd
from binascii import b2a_hex, a2b_hex
import hashlib
import datetime
import random
import subprocess
import uuid
import json
import logging

from settings import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from ssh.models import User, Asset, UserPar
from ssh.settings import *

from django.core.mail import send_mail
from email.mime.text import MIMEText
from email.utils import formataddr
from smtplib import SMTP, SMTP_SSL, SMTPAuthenticationError, SMTPConnectError, SMTPSenderRefused

URL = 'http://www.lxa.kim'
os.environ['DJANGO_SETTINGS_MODULE'] = 'ssh.settings'

def color_print(msg, color='red', exits=False):
    """
    Print colorful string.
    颜色打印字符或者退出
    """
    color_msg = {'blue': '\033[1;36m%s\033[0m',
                 'green': '\033[1;32m%s\033[0m',
                 'yellow': '\033[1;33m%s\033[0m',
                 'red': '\033[1;31m%s\033[0m',
                 'title': '\033[30;42m%s\033[0m',
                 'info': '\033[32m%s\033[0m'}
    msg = color_msg.get(color, 'red') % msg
    print msg
    if exits:
        time.sleep(2)
        sys.exit()
    return msg
    
def set_log(level, filename='ssh.log'):
    """
    return a log file object
    根据提示设置log打印
    参考博客：https://www.cnblogs.com/xielisen/p/6817807.html
    """
    log_file = os.path.join(LOG_DIR, filename)
    if not os.path.isfile(log_file):
        os.mknod(log_file)
        os.chmod(log_file, 0777)
    log_level_total = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARN, 'error': logging.ERROR,
                       'critical': logging.CRITICAL}
    logger_f = logging.getLogger('ssh')
    logger_f.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file)
    fh.setLevel(log_level_total.get(level, logging.DEBUG))
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger_f.addHandler(fh)
    return logger_f

logger = set_log(LOG_LEVEL)

def bash(cmd):
    '''
    执行bash命令
    '''
    return subprocess.call(cmd, shell=True)

def get_mac_address():
    '''
    获得服务端的mac地址
    '''
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac

def get_object(model, **kwargs):
    '''
    数据库查询
    '''
    for value in kwargs.values():
        if not value:
            return None
    the_object = model.objects.filter(**kwargs)
    if len(the_object) == 1:
        the_object = the_object[0]
    else:
        the_object = None
    return the_object

def db_add_user(**kwargs):
    '''
    数据库中添加用户
    '''
    pass

def defend_attack(func):
    def _deco(request, *args, **kwargs):
        if int(request.session.get('visit', 1)) > 10:
            logger.debug('请求次数: %s' % request.session.get('visit', 1))
            Frobidden = '<h1>Forbidden.403.请求次数过多，请稍后再试。</h1>'
            return HttpResponse(Frobidden, status=403)
        request.session['visit'] = request.session.get('visit', 1) + 1
        request.session.set_expiry(300)
        return func(request, *args, **kwargs)
    return _deco

def require_login(func):
    """
    用户验证
    """
    def _deco(request, *args, **kwargs):
        if request.session.get('role_id') != 0:
            return HttpResponseRedirect(reverse('login'))
        else:
            return func(request, *args, **kwargs)
    return _deco

class ServerError(Exception):
    """
    自定义异常
    """
    pass

def chown(path, user, group=''):
    if not group:
        group = user
    try:
        uid = pwd.getpwnam(user).pw_uid
        gid = pwd.getpwnam(group).pw_gid
        os.chown(path, uid, gid)
    except KeyError:
        pass

def mkdir(dir_name, username='', mode=755):
    """
    目录存在，如果不存在就建立，并且权限正确
    """
    cmd = '[ ! -d %s ] && mkdir -p %s && chmod %s %s' % (dir_name, dir_name, mode, dir_name)
    bash(cmd)
    if username:
        chown(dir_name, username)


class PyCrypt(object):
    """
    加密类
    """

    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    @staticmethod
    def gen_rand_pass(length=16, especial=False):
        """
        random password
        随机生成密码
        """
        salt_key = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        symbol = '!@$%^&*()_'
        salt_list = []
        if especial:
            for i in range(length - 4):
                salt_list.append(random.choice(salt_key))
            for i in range(4):
                salt_list.append(random.choice(symbol))
        else:
            for i in range(length):
                salt_list.append(random.choice(salt_key))
        salt = ''.join(salt_list)
        return salt

    @staticmethod
    def md5_crypt(string):
        """
        md5 encrypt method
        md5非对称加密方法
        """
        return hashlib.new("md5", string).hexdigest()

    @staticmethod
    def gen_sha512(salt, password):
        """
        generate sha512 format password
        生成sha512加密密码
        """
        return crypt.crypt(password, '$6$%s$' % salt)

    def encrypt(self, passwd=None, length=32):
        """
        encrypt gen password
        对称加密之加密生成密码
        """
        if not passwd:
            passwd = self.gen_rand_pass()

        cryptor = AES.new(self.key, self.mode, b'8122ca7d906ad5e1')
        try:
            count = len(passwd)
        except TypeError:
            raise ServerError('Encrypt password error, TYpe error.')

        add = (length - (count % length))
        passwd += ('\0' * add)
        cipher_text = cryptor.encrypt(passwd)
        return b2a_hex(cipher_text)

    def decrypt(self, text):
        """
        decrypt pass base the same key
        对称加密之解密，同一个加密随机数
        """
        cryptor = AES.new(self.key, self.mode, b'8122ca7d906ad5e1')
        try:
            plain_text = cryptor.decrypt(a2b_hex(text))
        except TypeError:
            raise ServerError('Decrypt password error, TYpe error.')
        return plain_text.rstrip('\0')

CRYPTOR = PyCrypt(KEY)



def db_add_user(**kwargs):
    """
    数据库中添加用户
    """
    user = UserPar(**kwargs)
    user.save()
    return user

def server_add_user(username, ssh_key_pwd=''):
    """
    在服务器上添加一个用户
    """
    # useradd -s :https://zhidao.baidu.com/question/2121042840507711787.html
    bash("useradd -s '%s' '%s'" % (os.path.join(BASE_DIR, 'init.sh'), username))
    gen_ssh_key(username, ssh_key_pwd)

def user_add_mail(user, password='', ssh_key_pwd=''):
    """
    add user send mail
    发送用户添加邮件
    """
    mail_title = 'User %s add successful' % user.name
    mail_msg = """
    Hi, %s
        Your name: %s 
        Your web password: %s 
        Your Public Key password: %s 
        Public Key file address: %s/key_down/?uuid=%s
        Please don't reply, this is send automatically.
        My blog: http://www.lxxx.site
    """ % (user.name, user.username, password , ssh_key_pwd, URL, user.uuid)
    msg=MIMEText(mail_msg,'plain','utf-8')
    msg['From']=formataddr(['sshweb',EMAIL_HOST_USER])
    msg['To']=formataddr([user.name,user.email])             
    msg['Subject']= mail_title 
    try:
        smtp = SMTP_SSL('smtp.qq.com', port=465, timeout=2)
        smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtp.sendmail(EMAIL_HOST_USER, (user.email, ), msg.as_string())
        smtp.quit()
        # return True
    except:
        pass

def get_display_msg(user, password='', ssh_key_pwd='', send_mail_need=False):
    if send_mail_need:
        msg = u'添加用户 %s 成功！ 用户密码已发送到 %s 邮箱！' % (user.name, user.email)
    else:
        msg = u"""
        web address: %s .\n\r
        username: %s  .\n\r
        password: %s  .\n\r
        publick key password: %s  .\n\r
        publick key file download url: %s/key_down/?uuid=%s  .\n\r
        You can use this count!\n\r
        """ % (URL, user.username, password, ssh_key_pwd, URL, user.uuid)
    return msg


def gen_ssh_key(username, password='',
                key_dir=os.path.join(KEY_DIR, 'user'),
                authorized_keys=True, home="/home", length=2048):
    """
    生成一个用户ssh密钥对
    """
    logger.debug('生成ssh key')
    private_key_file = os.path.join(key_dir, username+'.pem')
    mkdir(key_dir, mode=777)
    if os.path.isfile(private_key_file):
        os.unlink(private_key_file)
    ret = bash('echo -e  "y\n"|ssh-keygen -t rsa -f %s -b %s -P "%s"' % (private_key_file, length, password))

    if authorized_keys:
        auth_key_dir = os.path.join(home, username, '.ssh')
        mkdir(auth_key_dir, username=username, mode=700)
        authorized_key_file = os.path.join(auth_key_dir, 'authorized_keys')
        with open(private_key_file+'.pub') as pub_f:
            with open(authorized_key_file, 'w') as auth_f:
                auth_f.write(pub_f.read())
        os.chmod(authorized_key_file, 0600)
        chown(authorized_key_file, username)

def ssh_del_user(username):
    """
    删除系统上的用户
    """
    bash('userdel -r -f %s' % username)
    logger.debug('rm -f %s/%s_*.pem' % (os.path.join(KEY_DIR, 'user'), username))
    bash('rm -f %s/%s_*.pem' % (os.path.join(KEY_DIR, 'user'), username))
    bash('rm -f %s/%s.pem*' % (os.path.join(KEY_DIR, 'user'), username))