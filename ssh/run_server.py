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

import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.gen
import tornado.httpclient
import readline # https://www.cnblogs.com/liujiacai/p/7838294.html
import django
import paramiko  # https://blog.csdn.net/songfreeman/article/details/50920767
import getpass  # https://www.cnblogs.com/xuchunlin/p/7763728.html
import errno
import pyte
import operator     # 这些函数主要分为几类：对象比较、逻辑比较、算术运算和序列操作
import struct, fcntl, signal, socket, select

from tornado.options import define, options
from pyinotify import WatchManager, ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY, AsyncNotifier
import select

try:
    import simplejson as json #simplejson（c语言）速度要快于json
except ImportError:
    import json

os.environ['DJANGO_SETTINGS_MODULE'] = 'ssh.settings'
if not django.get_version().startswith('1.6'):
    setup = django.setup()

from ssh.api import color_print, logger
try:
    remote_ip = os.environ.get('SSH_CLIENT').split()[0]
except (IndexError, AttributeError):
    remote_ip = os.popen("who -m | awk '{ print $NF }'").read().strip('()\n')


from ssh.settings import IP, PORT, LOG_DIR, NAV_SORT_BY

define("port", default=PORT, help="run on the given port", type=int)
define("host", default=IP, help="run port on given host", type=str)

def django_request_support(func): 
    # 带参数的装饰器
    @functools.wraps(func)# 编写装饰器时，在实现前加入 @functools.wraps(func) 可以保证装饰器不会对被装饰函数造成影响
    def _deco(*args, **kwargs): # *元组，**字典；无名参数和有名参数的区别
        request_started.send_robust(func)
        response = func(*args, **kwargs)
        request_finished.send_robust(func)
        return response
    return _deco


def write_log(f, msg):
    msg = re.sub(r'[\r\n]', '\r\n', msg)
    f.write(msg)
    f.flush()


class Tty(object):
    """
    A virtual tty class
    一个虚拟终端类，实现连接ssh和记录日志，基类
    """
    def __init__(self,asset,login_type='ssh'):
        self.username = asset.username
        self.asset_name = asset.hostname
        self.ip = asset.ip
        self.port = asset.ip
        self.passwd = asset.passwd
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
        passwd = CRYPTOR.decrypt(self.passwd)
        connect_info = {'user': self.username, 'asset_name': self.hostname, 'ip': self.ip,
                        'port': int(self.port),'role_passwd': passwd, 'role_key': self.ssh_key}
        logger.debug(connect_info)
        return connect_info

    def get_connection(self):
        """
        获取连接成功后的ssh
        """
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
                                password=connect_info.get('role_passwd'),
                                key_filename=role_key,
                                look_for_keys=False)
                    return ssh
                except (paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException):
                    logger.warning(u'使用ssh key %s 失败, 尝试只使用密码' % role_key)
                    pass

            ssh.connect(connect_info.get('ip'),
                        port=connect_info.get('port'),
                        username=connect_info.get('user'),
                        password=connect_info.get('role_passwd'),
                        allow_agent=False,
                        look_for_keys=False)

        except (paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException):
            raise ServerError('认证失败 Authentication Error.')
        except socket.error:
            raise ServerError('端口可能不对 Connect SSH Socket Port Error, Please Correct it.')
        else:
            self.ssh = ssh
            return ssh


class WebTty(Tty):
    def __init__(self, *args, **kwargs):
        super(WebTty, self).__init__(*args, **kwargs)
        self.ws = None
        self.data = ''
        self.input_mode = False

class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)

    def run(self):
        try:
            super(MyThread, self).run()
        except WebSocketClosedError:
            pass


class WebTerminalKillHandler(tornado.web.RequestHandler):
    @django_request_support
    def get(self):
        ws_id = self.get_argument('id')
        Log.objects.filter(id=ws_id).update(is_finished=True)
        for ws in WebTerminalHandler.clients:
            if ws.id == int(ws_id):
                logger.debug("Kill log id %s" % ws_id)
                ws.log.save()
                ws.close()
        logger.debug('Websocket: web terminal client num: %s' % len(WebTerminalHandler.clients))


class WebTerminalHandler(tornado.websocket.WebSocketHandler):
    # 参考博客 https://www.cnblogs.com/shijingjing07/p/6558668.html
    clients = []
    tasks = []

    def __init__(self, *args, **kwargs):
        self.term = None
        self.log_file_f = None
        self.log_time_f = None
        self.log = None
        self.id = 0
        self.user = None
        self.ssh = None
        self.channel = None
        super(WebTerminalHandler, self).__init__(*args, **kwargs)

    def check_origin(self, origin):
        return True

    @django_request_support
    def open(self):
        logger.debug('Websocket: Open request')
        asset_name = self.get_argument('user', 'sb')
        asset_id = self.get_argument('id', 9999)
        asset = get_object(Asset, id=asset_id)
        # self.termlog = TermLogRecorder(User.objects.get(id=self.user_id))
        if asset:
            logger.debug('Websocket: request web terminal Host: %s User: %s' % (asset.hostname, asset.username))
        else:
            logger.warning('Websocket: No that Host: %s User: %s ' % (asset_id, asset.username))
            self.close()
            return
        self.term = WebTty(asset, login_type='web')
        # self.term.remote_ip = self.request.remote_ip
        self.term.remote_ip = self.request.headers.get("X-Real-IP")
        if not self.term.remote_ip:
            self.term.remote_ip = self.request.remote_ip
        self.ssh = self.term.get_connection()
        self.channel = self.ssh.invoke_shell(term='xterm')
        WebTerminalHandler.tasks.append(MyThread(target=self.forward_outbound))
        WebTerminalHandler.clients.append(self)

        for t in WebTerminalHandler.tasks:
            if t.is_alive():
                continue
            try:
                t.setDaemon(True)
                t.start()
            except RuntimeError:
                pass

    def on_message(self, message):
        jsondata = json.loads(message) #将str类型转换为字典类型
        if not jsondata:
            return

        if 'resize' in jsondata.get('data'):
            self.termlog.write(message)
            self.channel.resize_pty(
                width=int(jsondata.get('data').get('resize').get('cols', 100)),
                height=int(jsondata.get('data').get('resize').get('rows', 35))
            )
        elif jsondata.get('data'):
            self.termlog.recoder = True
            self.term.input_mode = True
            if str(jsondata['data']) in ['\r', '\n', '\r\n']:
                match = re.compile(r'\x1b\[\?1049', re.X).findall(self.term.vim_data)
                if match:
                    if self.term.vim_flag or len(match) == 2:
                        self.term.vim_flag = False
                    else:
                        self.term.vim_flag = True
                elif not self.term.vim_flag:
                    result = self.term.deal_command(self.term.data)[0:200]
                self.term.vim_data = ''
                self.term.data = ''
                self.term.input_mode = False
            self.channel.send(jsondata['data'])
        else:
            pass

    def on_close(self):
        logger.debug('Websocket: Close request')
        if self in WebTerminalHandler.clients:
            WebTerminalHandler.clients.remove(self)
        try:
            self.log_file_f.write('End time is %s' % datetime.datetime.now())
            self.log.is_finished = True
            self.log.end_time = datetime.datetime.now()
            # self.log.filename = self.termlog.filename
            self.log.save()
            self.log_time_f.close()
            self.ssh.close()
            self.close()
        except AttributeError:
            pass

    def forward_outbound(self):
        self.log_file_f, self.log_time_f, self.log = self.term.get_log()
        self.id = self.log.id
        # self.termlog.setid(self.id)
        try:
            data = ''
            pre_timestamp = time.time()
            while True:
                r, w, e = select.select([self.channel], [], [])
                if self.channel in r:
                    recv = self.channel.recv(1024)
                    if not len(recv):
                        return
                    data += recv
                    self.term.vim_data += recv
                    try:
                        self.write_message(data.decode('utf-8', 'replace'))
                        # self.termlog.write(data)
                        # self.termlog.recoder = False
                        now_timestamp = time.time()
                        self.log_time_f.write('%s %s\n' % (round(now_timestamp - pre_timestamp, 4), len(data)))
                        self.log_file_f.write(data)
                        pre_timestamp = now_timestamp
                        self.log_file_f.flush()
                        self.log_time_f.flush()
                        if self.term.input_mode:
                            self.term.data += data
                        data = ''
                    except UnicodeDecodeError:
                        pass
        except IndexError:
            pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/terminal', WebTerminalHandler),
            (r'/kill', WebTerminalKillHandler),
        ]

        setting = {
            'cookie_secret': 'DFksdfsasdfkasdfFKwlwfsdfsa1204mx',
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'debug': False,
        }

        tornado.web.Application.__init__(self, handlers, **setting)


def main():
    from django.core.wsgi import get_wsgi_application
    import tornado.wsgi
    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    setting = {
        'cookie_secret': 'DFksdfsasdfkasdfFKwlwfsdfsa1204mx',
        'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'debug': False,
    }
    tornado_app = tornado.web.Application(
        [
            (r'/ws/terminal', WebTerminalHandler),
            (r'/ws/kill', WebTerminalKillHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler,
             dict(path=os.path.join(os.path.dirname(__file__), "static"))),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ], **setting)

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port, address=IP)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    # tornado.options.parse_command_line()
    # app = Application()
    # server = tornado.httpserver.HTTPServer(app)
    # server.bind(options.port, options.host)
    # #server.listen(options.port)
    # server.start(num_processes=5)
    # tornado.ioloop.IOLoop.instance().start()
    print "Run server on %s:%s" % (options.host, options.port)
    main()
