#!/usr/bin/python
# coding: utf-8

import time
import os
import sys
from smtplib import SMTP, SMTP_SSL, SMTPAuthenticationError, SMTPConnectError, SMTPSenderRefused
import ConfigParser
import socket
import random
import string

import re
import platform #识别运行环境操作系统
import shlex

#获得当前脚本的绝对路径，去掉最后两个路径
ssh_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(ssh_dir)


def bash(cmd):
    """
    执行bash命令
    """
    return shlex.os.system(cmd)


def valid_ip(ip):
    if ('255' in ip) or (ip == "0.0.0.0"):
        return False
    else:
        return True


def color_print(msg, color='red', exits=False):
    """
    Print colorful string.
    颜色打印字符或者退出
    参考：https://www.cnblogs.com/hellojesson/p/5961570.html
    开头部分：
        \033[显示方式;前景色;背景色m + 结尾部分：\033[0m
    注意：
        开头部分的三个参数：显示方式，前景色，背景色是可选参数，
        可以只写其中的某一个；另外由于表示三个参数不同含义的数值都是唯一的没有重复的，
        所以三个参数的书写先后顺序没有固定要求，系统都能识别；
        但是，建议按照默认的格式规范书写
    """
    color_msg = {'blue': '\033[1;36m%s\033[0m',
                 'green': '\033[1;32m%s\033[0m',
                 'yellow': '\033[1;33m%s\033[0m',
                 'red': '\033[1;31m%s\033[0m',
                 'title': '\033[30;42m%s\033[0m',
                 'info': '\033[32m%s\033[0m'}
    # print("\033[1;36m%s\033[0m" % msg)
    msg = color_msg.get(color, 'red') % msg  
    print msg
    if exits:
        time.sleep(2)
        sys.exit()
    return msg


def get_ip_addr():
    '''
    socket参考：https://www.cnblogs.com/wumingxiaoyao/p/7047658.html
    socket(family,type[,protocal]) 使用给定的地址族、套接字类型、协议编号（默认为0）来创建套接字。
    socket.AF_INET -服务器之间的网络通信
    socket.SOCK_STREAM -流式socket , for TCP
    socket.SOCK_DGRAM -数据报式socket , for UDP
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM 数据报
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        #LANG=C 防止出现乱码
        if_data = ''.join(os.popen("LANG=C ifconfig").readlines()) 
        #re.MULTILINE 匹配字符串换行符后面的位置      
        ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', if_data, flags=re.MULTILINE)
        ip = filter(valid_ip, ips) # filter(function,iter),iter作为参数传递给function
        if ip:
            return ip[0]
    return ''


class PreSetup(object):
    def __init__(self):
        self.db_host = '127.0.0.1'
        self.db_port = 3306
        self.db_user = 'sshweb'
        self.db_pass = 'ssh@web'
        self.db = 'sshweb'
        self.mail_host = 'smtp.qq.com'
        self.mail_port = 25
        self.mail_addr = 'ssh@web.com'
        self.mail_pass = ''
        self.ip = ''
        self.key = ''.join(random.choice(string.ascii_lowercase + string.digits) \
                           for _ in range(16)) # _：无关变量
        self.dist = platform.linux_distribution()[0].lower()
        '''
        >>> dist=platform.linux_distribution()
        >>> print dist
        ('CentOS Linux', '7.3.1611', 'Core')
        '''
        self.version = platform.linux_distribution()[1]

    @property
    def _is_redhat(self):
        if self.dist.startswith("centos") or self.dist.startswith("red") or self.dist == "fedora" or self.dist == "amazon linux ami":
            return True

    @property
    def _is_centos7(self):
        if self.dist.startswith("centos") and self.version.startswith("7"):
            return True

    @property
    def _is_fedora_new(self):
        if self.dist == "fedora" and int(self.version) >= 20:
            return True

    @property
    def _is_ubuntu(self):
        if self.dist == "ubuntu" or self.dist == "debian":
            return True

    def check_platform(self):
        if not (self._is_redhat or self._is_ubuntu):
            print(u"支持的平台: CentOS, RedHat, Fedora, Debian, Ubuntu, Amazon Linux, 暂不支持其他平台安装.")
            exit()

    #Python 中的 classmethod 和 staticmethod 有什么具体用途？ - 知乎用户的回答 - 知乎
    #https://www.zhihu.com/question/20021164/answer/115518482

    @staticmethod
    def check_bash_return(ret_code, error_msg):
        if ret_code != 0:
            color_print(error_msg, 'red')
            exit()

    def write_conf(self, conf_file=os.path.join(ssh_dir, 'ssh.conf')):
        color_print('开始写入配置文件', 'green')
        conf = ConfigParser.ConfigParser() # import ConfigParser
        conf.read(conf_file)
        conf.set('base', 'url', 'http://%s' % self.ip)
        conf.set('base', 'key', self.key)
        conf.set('db', 'host', self.db_host)
        conf.set('db', 'port', self.db_port)
        conf.set('db', 'user', self.db_user)
        conf.set('db', 'password', self.db_pass)
        conf.set('db', 'database', self.db)
        conf.set('mail', 'email_host', self.mail_host)
        conf.set('mail', 'email_port', self.mail_port)
        conf.set('mail', 'email_host_user', self.mail_addr)
        conf.set('mail', 'email_host_password', self.mail_pass)
        '''
        [sec_a]  
        a_key1 = 20  
        a_key2 = 10 
        生成配置文件：
        [db]
        db_host = '127.0.0.1'
        ...

        [mail]
        email_host = xxx
        '''

        with open(conf_file, 'w') as f:
            conf.write(f)

    def _setup_mysql(self):
        color_print('开始安装设置mysql (请手动设置mysql安全)', 'green')
        color_print('默认用户名: %s 默认密码: %s' % (self.db_user, self.db_pass), 'green')
        if self._is_redhat:
            if self._is_centos7 or self._is_fedora_new:
                ret_code = bash('yum -y install mariadb-server mariadb-devel')
                self.check_bash_return(ret_code, "安装mysql(mariadb)失败, 请检查安装源是否更新或手动安装！")

                bash('systemctl enable mariadb.service')
                bash('systemctl start mariadb.service')
            else:
                ret_code = bash('yum -y install mysql-server')
                self.check_bash_return(ret_code, "安装mysql失败, 请检查安装源是否更新或手动安装！")

                bash('service mysqld start')
                bash('chkconfig mysqld on')
            bash('mysql -e "create database %s default charset=utf8"' % self.db) #???不需要登录密码吗
            # grant 权限1,权限2,…权限n on 数据库名称.表名称 to 用户名@用户地址 identified by ‘连接口令’;
            bash('mysql -e "grant all on %s.* to \'%s\'@\'%s\' identified by \'%s\'"' % (self.db,
                                                                                         self.db_user,
                                                                                         self.db_host,
                                                                                         self.db_pass))
        if self._is_ubuntu:
            cmd1 = "echo mysql-server mysql-server/root_password select '' | debconf-set-selections"
            cmd2 = "echo mysql-server mysql-server/root_password_again select '' | debconf-set-selections"
            cmd3 = "apt-get -y install mysql-server"
            ret_code = bash('%s; %s; %s' % (cmd1, cmd2, cmd3))
            self.check_bash_return(ret_code, "安装mysql失败, 请检查安装源是否更新或手动安装！")

            bash('service mysql start')
            bash('mysql -e "create database %s default charset=utf8"' % self.db)
            bash('mysql -e "grant all on %s.* to \'%s\'@\'%s\' identified by \'%s\'"' % (self.db,
                                                                                         self.db_user,
                                                                                         self.db_host,
                                                                                         self.db_pass))

    def _set_env(self):
        color_print('开始关闭防火墙和selinux', 'green')
        if self._is_redhat:
            os.system("export LANG='en_US.UTF-8'") # 全局变量
            if self._is_centos7 or self._is_fedora_new:
                cmd1 = "systemctl status firewalld 2> /dev/null 1> /dev/null"
                cmd2 = "systemctl stop firewalld"
                cmd3 = "systemctl disable firewalld"
                bash('%s && %s && %s' % (cmd1, cmd2, cmd3))
                bash('localectl set-locale LANG=en_US.UTF-8')
                '''
                [root@yangxiao ~]# localectl status
                System Locale: LANG=en_US.UTF-8
                VC Keymap: us
                X11 Layout: n/a
                '''
                bash('which setenforce 2> /dev/null 1> /dev/null && setenforce 0')
            else:
                bash("sed -i 's/LANG=.*/LANG=en_US.UTF-8/g' /etc/sysconfig/i18n")
                bash('service iptables stop && chkconfig iptables off && setenforce 0')

        if self._is_ubuntu:
            os.system("export LANG='en_US.UTF-8'")
            bash("which iptables && iptables -F")
            bash('which setenforce && setenforce 0')

    def _test_db_conn(self):
        import MySQLdb
        try:
            MySQLdb.connect(host=self.db_host, port=int(self.db_port),
                            user=self.db_user, passwd=self.db_pass, db=self.db)
            color_print('连接数据库成功', 'green')
            return True
        except MySQLdb.OperationalError, e:
            color_print('数据库连接失败 %s' % e, 'red')
            return False

    def _test_mail(self):
        try:
            if self.mail_port == 465:
                smtp = SMTP_SSL(self.mail_host, port=self.mail_port, timeout=2)
            else:
                smtp = SMTP(self.mail_host, port=self.mail_port, timeout=2)
            smtp.login(self.mail_addr, self.mail_pass)
            smtp.sendmail(self.mail_addr, (self.mail_addr, ),
                          '''From:%s\r\nTo:%s\r\nSubject:SshWeb Mail Test!\r\n\r\n  Mail test passed!\r\n''' %
                          (self.mail_addr, self.mail_addr))
            smtp.quit()
            return True

        except Exception, e:
            color_print(e, 'red')
            skip = raw_input('是否跳过(y/n) [n]? : ')
            if skip == 'y':
                return True
            return False

    def _rpm_repo(self):
        if self._is_redhat:
            color_print('开始安装epel源', 'green')
            bash('yum -y install epel-release')
            #Extra Packages for Enterprise Linux ,安装包

    def _depend_rpm(self):
        color_print('开始安装依赖包', 'green')
        if self._is_redhat:
            cmd = 'yum -y install git python-pip mysql-devel rpm-build gcc automake autoconf python-devel vim sshpass lrzsz readline-devel'
            ret_code = bash(cmd)
            self.check_bash_return(ret_code, "安装依赖失败, 请检查安装源是否更新或手动安装！")
        if self._is_ubuntu:
            cmd = "apt-get -y --force-yes install git python-pip gcc automake autoconf vim sshpass libmysqld-dev python-all-dev lrzsz libreadline-dev"
            ret_code = bash(cmd)
            self.check_bash_return(ret_code, "安装依赖失败, 请检查安装源是否更新或手动安装！")

    def _require_pip(self):
        color_print('开始安装依赖pip包', 'green')
        bash('pip uninstall -y pycrypto')
        bash('rm -rf /usr/lib64/python2.6/site-packages/Crypto/') #删除原依赖
        ret_code = bash('pip install -r requirements.txt')
        self.check_bash_return(ret_code, "安装SshWeb 依赖的python库失败！")

    def _input_ip(self):
        ip = raw_input('\n请输入您服务器的IP地址，用户浏览器可以访问 [%s]: ' % get_ip_addr()).strip()
        self.ip = ip if ip else get_ip_addr()

    def _input_mysql(self):
        while True:
            mysql = raw_input('是否安装新的MySQL服务器? (y/n) [y]: ')
            if mysql != 'n':
                self._setup_mysql()
            else:
                db_host = raw_input('请输入数据库服务器IP [127.0.0.1]: ').strip()
                db_port = raw_input('请输入数据库服务器端口 [3306]: ').strip()
                db_user = raw_input('请输入数据库服务器用户 [sshweb]: ').strip()
                db_pass = raw_input('请输入数据库服务器密码: ').strip()
                db = raw_input('请输入使用的数据库 [sshweb]: ').strip()

                if db_host: self.db_host = db_host
                if db_port: self.db_port = db_port
                if db_user: self.db_user = db_user
                if db_pass: self.db_pass = db_pass
                if db: self.db = db

            if self._test_db_conn():
                break

            print

    def _input_smtp(self):
        while True:
            self.mail_host = raw_input('请输入SMTP地址: ').strip()
            mail_port = raw_input('请输入SMTP端口 [25]: ').strip()
            self.mail_addr = raw_input('请输入账户: ').strip()
            self.mail_pass = raw_input('请输入密码: ').strip()

            if mail_port: self.mail_port = int(mail_port)

            if self._test_mail():
                color_print('\n\t请登陆邮箱查收邮件, 然后确认是否继续安装\n', 'green')
                smtp = raw_input('是否继续? (y/n) [y]: ')
                if smtp == 'n':
                    continue
                else:
                    break
            print

    def start(self):
        color_print('开始安装...')
        time.sleep(3)
        self.check_platform() # 检查环境
        self._rpm_repo() # 安装Extra Packages for Enterprise Linux ,安装包
        self._depend_rpm() # 安装依赖
        self._require_pip() # 安装pip
        self._set_env() # 设置环境，关闭防火墙和selinux
        self._input_ip()  # 输入服务器ip
        self._input_mysql() # 输入数据库配置
        self._input_smtp() # 输入邮箱配置
        self.write_conf() # 保存配置成文本
        os.system('python %s' % os.path.join(ssh_dir, 'install/next.py')) 
        # 设置admin，写入 数据库，初始化运行环境，执行run_server.py
        # os.system(cmd)的返回值只会有0(成功),1,2
        # os.popen(cmd)会吧执行的cmd的输出作为值返回。


if __name__ == '__main__':
    pre_setup = PreSetup()
    pre_setup.start()
