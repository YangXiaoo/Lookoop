#!/usr/bin/env python
# coding: utf-8

import time
import datetime
import json
import os
import sys
import os.path
import threading
import re
import functools
from django.core.signals import request_started, request_finished


import readline # https://www.cnblogs.com/liujiacai/p/7838294.html
import django
import paramiko  # https://blog.csdn.net/songfreeman/article/details/50920767
import getpass  # https://www.cnblogs.com/xuchunlin/p/7763728.html
import errno
import pyte
import operator     # 这些函数主要分为几类：对象比较、逻辑比较、算术运算和序列操作
import struct, fcntl, signal, socket, select

import tornado.options
from pyinotify import WatchManager, ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY, AsyncNotifier
import select

try:
    import termios
    # 堡垒机实现：https://my.oschina.net/eddylinux/blog/604317
    import tty
except ImportError:
    print '\033[1;31m仅支持类Unix系统 Only unix like supported.\033[0m'
    time.sleep(3)
    sys.exit()

try:
    import simplejson as json
except ImportError:
    import json

os.environ['DJANGO_SETTINGS_MODULE'] = 'ssh.settings'
if not django.get_version().startswith('1.6'):
    setup = django.setup()

from ssh.api import *

from ssh.models import *
from ssh.settings import IP, PORT, LOG_DIR, NAV_SORT_BY

try:
    remote_ip = os.environ.get('SSH_CLIENT').split()[0]
except (IndexError, AttributeError):
    remote_ip = os.popen("who -m | awk '{ print $NF }'").read().strip('()\n')
    
    
class Tty(object):
    """
    A virtual tty class
    一个虚拟终端类，实现连接ssh和记录日志，基类
    """
    def __init__(self,asset,login_type='ssh'):
        self.username = asset.username
        self.asset_name = asset.hostname
        self.ip = asset.ip
        self.port = asset.port
        self.passwd = asset.password
        self.ssh_key = asset.ssh_key
        self.ssh = None
        self.channel = None
        # self.asset = asset
        self.remote_ip = ''
        self.login_type = login_type
        self.vim_flag = False
        self.vim_end_pattern = re.compile(r'\x1b\[\?1049', re.X)
        self.vim_data = ''
        self.stream = None
        self.screen = None
        self.__init_screen_stream()

    def __init_screen_stream(self):
        """
        初始化虚拟屏幕和字符流
        """
        self.stream = pyte.ByteStream()
        self.screen = pyte.Screen(80, 24)
        self.stream.attach(self.screen)

    @staticmethod
    def is_output(strings):  #有换行符就输出
        newline_char = ['\n', '\r', '\r\n']
        for char in newline_char:
            if char in strings:
                return True
        return False

    @staticmethod
    def command_parser(command):
        """
        处理命令中如果有ps1或者mysql的特殊情况,极端情况下会有ps1和mysql
        :param command:要处理的字符传
        :return:返回去除PS1或者mysql字符串的结果
        PS1：prompt sign 命令提示符
        """
        result = None
        match = re.compile('\[?.*@.*\]?[\$#]\s').split(command) #[root@yangxiao ~]# 
        if match:
            # 只需要最后的一个PS1后面的字符串
            result = match[-1].strip()
        else:
            # PS1没找到,查找mysql
            match = re.split('mysql>\s', command)
            if match:
                # 只需要最后一个mysql后面的字符串
                result = match[-1].strip()
        return result

    def deal_command(self, data):
        """
        处理截获的命令
        :param data: 要处理的命令
        :return:返回最后的处理结果
        """
        command = ''
        try:
            self.stream.feed(data)
            # 从虚拟屏幕中获取处理后的数据
            for line in reversed(self.screen.buffer):
                line_data = "".join(map(operator.attrgetter("data"), line)).strip()
                if len(line_data) > 0:
                    parser_result = self.command_parser(line_data)
                    if parser_result is not None:
                        # 2个条件写一起会有错误的数据
                        if len(parser_result) > 0:
                            command = parser_result
                    else:
                        command = line_data
                    break
        except Exception:
            pass
        # 虚拟屏幕清空
        self.screen.reset()
        return command

    def get_log(self):
        """
        记录用户的日志
        """
        tty_log_dir = os.path.join(LOG_DIR, 'tty')
        if not os.path.isfile(tty_log_dir):
            try:
                mkdir(tty_log_dir, mode=777)
            except:
                logger.debug('创建目录 %s 失败' % tty_log_dir)
        date_today = datetime.datetime.now()
        date_start = date_today.strftime('%Y%m%d')
        time_start = date_today.strftime('%H%M%S')
        today_connect_log_dir = os.path.join(tty_log_dir, date_start)
        log_file_path = os.path.join(today_connect_log_dir, '%s_%s_%s' % (self.username, self.asset_name, time_start))

        try:
            mkdir(os.path.dirname(today_connect_log_dir), mode=777)
            mkdir(today_connect_log_dir, mode=777)
        except OSError:
            logger.debug('创建目录 %s 失败，请修改%s目录权限' % (today_connect_log_dir, tty_log_dir))
            raise ServerError('创建目录 %s 失败，请修改%s目录权限' % (today_connect_log_dir, tty_log_dir))

        try:
            log_file_f = open(log_file_path + '.log', 'a')
            log_time_f = open(log_file_path + '.time', 'a')
        except IOError:
            logger.debug('创建tty日志文件失败, 请修改目录%s权限' % today_connect_log_dir)
            raise ServerError('创建tty日志文件失败, 请修改目录%s权限' % today_connect_log_dir)

        if self.login_type == 'ssh':  # 如果是ssh连接过来，记录connect.py的pid，web terminal记录为日志的id
            pid = os.getpid()
            self.remote_ip = remote_ip  # 获取远端IP
        else:
            pid = 0

        log = Log(user=self.username, host=self.asset_name, remote_ip=self.remote_ip, login_type=self.login_type,
                  logfile_path=log_file_path, start_time=date_today, pid=pid)
        log.save()
        if self.login_type == 'web':
            log.pid = log.id  # 设置log id为websocket的id, 然后kill时干掉websocket
            log.save()

        log_file_f.write('Start at %s\r\n' % datetime.datetime.now())
        return log_file_f, log_time_f, log

    def get_connect_info(self):
        """
        获取需要登陆的主机的信息和映射用户的账号密码
        """
        # passwd = CRYPTOR.decrypt(self.passwd)
        connect_info = {'user': self.username, 'asset_hostname': self.asset_name, 'ip': self.ip, 'port': self.port,'ssh_passwd': self.passwd, 'role_key': self.ssh_key}
        logger.debug(connect_info)
        logger.debug('get_connection_info successful')
        return connect_info

    def get_connection(self):
        """
        获取连接成功后的ssh
        """
        logger.debug('start connection')
        connect_info = self.get_connect_info()

        # 发起ssh连接请求 Make a ssh connection
        ssh = paramiko.SSHClient()
        # ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            role_key = connect_info.get('role_key')
            if role_key and os.path.isfile(role_key):
                try:
                    ssh.connect(connect_info.get('ip'),
                                port=connect_info.get('port'),
                                username=connect_info.get('user'),
                                password=connect_info.get('ssh_passwd'),
                                key_filename=role_key,
                                look_for_keys=False)
                    return ssh
                except (paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException):
                    logger.warning(u'使用ssh key %s 失败, 尝试只使用密码' % role_key)
                    pass

            ssh.connect(connect_info.get('ip'),
                        port=connect_info.get('port'),
                        username=connect_info.get('user'),
                        password=connect_info.get('ssh_passwd'),
                        allow_agent=False,
                        look_for_keys=False)

        except (paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException):
            raise ServerError('认证失败 Authentication Error.')
        except socket.error:
            raise ServerError('端口可能不对 Connect SSH Socket Port Error, Please Correct it.')
        else:
            self.ssh = ssh
            return ssh