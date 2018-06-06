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
from ssh.tty_api import Tty
try:
    remote_ip = os.environ.get('SSH_CLIENT').split()[0]
except (IndexError, AttributeError):
    remote_ip = os.popen("who -m | awk '{ print $NF }'").read().strip('()\n')
    # NF : the number of the list

from ssh.models import *
from ssh.settings import IP, PORT, LOG_DIR, NAV_SORT_BY

from tornado.options import options, define as _define
    
# Not need , just in case of repeat defined   
def define(name, default=None, type=None, help=None, metavar=None,
           multiple=False, group=None, callback=None):
    if name not in options._options:
        return _define(name, default, type, help, metavar,
           multiple, group, callback)
    
tornado.options.define = define


define("port", default=PORT, help="run on the given port", type=int)
define("host", default=IP, help="run port on given host", type=str)

def django_request_support(func): 
    @functools.wraps(func)
    def _deco(*args, **kwargs):
        request_started.send_robust(func)
        response = func(*args, **kwargs)
        request_finished.send_robust(func)
        return response
    return _deco


def write_log(f, msg):
    msg = re.sub(r'[\r\n]', '\r\n', msg)
    f.write(msg)
    f.flush()



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
    # https://www.cnblogs.com/shijingjing07/p/6558668.html
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
        asset_id = self.get_argument('id', 1)
        asset = get_object(Asset, id=asset_id)
        logger.debug('%s %s ' % (asset.ip,asset.password))
        # self.termlog = TermLogRecorder(User.objects.get(id=self.user_id))
        if asset:
            logger.debug('Websocket: request web terminal Host: %s User: %s' % (asset.hostname, asset.username))
        else:
            logger.warning('Websocket: No that Host: %s User: %s ' % (asset_id, asset.username))
            self.close()
            return
        self.term = WebTty(asset, login_type='web')
        # logger.debug('test webtty can')
        # aa = self.term.get_log()
        # self.term.remote_ip = self.request.remote_ip
        self.term.remote_ip = self.request.headers.get("X-Real-IP")
        if not self.term.remote_ip:
            self.term.remote_ip = self.request.remote_ip
        logger.debug('remote_ip_0: %s' % self.term.remote_ip)
        self.ssh = self.term.get_connection()
        logger.debug('remote_ip: %s' % self.term.remote_ip)
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
            # self.termlog.write(message)
            self.channel.resize_pty(
                width=int(jsondata.get('data').get('resize').get('cols', 100)),
                height=int(jsondata.get('data').get('resize').get('rows', 35))
            )
        elif jsondata.get('data'):
            # self.termlog.recoder = True
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
        end = '*'*30
        logger.debug(end)
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
    print "Run server on %s:%s" % (options.host, options.port)
    main()
