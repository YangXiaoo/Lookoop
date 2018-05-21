#!/usr/bin/env python
# coding: utf-8

import sys

import os
import re
import time
import datetime
import textwrap
import readline
                
import readline 
import django
import paramiko 
import errno    
import pyte
import operator 
import getpass
import struct, fcntl, signal, socket, select
from io import open as copen
import uuid

os.environ['DJANGO_SETTINGS_MODULE'] = 'ssh.settings'
if not django.get_version().startswith('1.6'):
    setup = django.setup()

from django.contrib.sessions.models import Session
from django.db.models import Q
from ssh.api import * 
from ssh.settings import LOG_DIR, NAV_SORT_BY
from ssh.ansible_api import MyRunner
from ssh.tty_api import Tty
from ssh.models import User, UserPar, Log, AssetGroup

login_user = get_object(UserPar, username=getpass.getuser()) 

try:
    remote_ip = os.environ.get('SSH_CLIENT').split()[0]
except (IndexError, AttributeError):
    remote_ip = os.popen("who -m | awk '{ print $NF }'").read().strip('()\n')

try:
    import termios
    import tty
except ImportError:
    print '\033[1;31m仅支持类Unix系统 Only unix like supported.\033[0m'
    time.sleep(3)
    sys.exit()



class SshTty(Tty):
    """
    一个虚拟终端类，实现连接ssh和记录日志
    """

    @staticmethod
    def get_win_size():
        """
        This function use to get the size of the windows!
        获得terminal窗口大小
        """
        if 'TIOCGWINSZ' in dir(termios):
            TIOCGWINSZ = termios.TIOCGWINSZ
        else:
            TIOCGWINSZ = 1074295912L
        s = struct.pack('HHHH', 0, 0, 0, 0)
        x = fcntl.ioctl(sys.stdout.fileno(), TIOCGWINSZ, s)
        return struct.unpack('HHHH', x)[0:2]

    def set_win_size(self, sig, data):
        """
        This function use to set the window size of the terminal!
        设置terminal窗口大小
        """
        try:
            win_size = self.get_win_size()
            self.channel.resize_pty(height=win_size[0], width=win_size[1])
        except Exception:
            pass

    def posix_shell(self):
        """
        Use paramiko channel connect server interactive.
        使用paramiko模块的channel，连接后端，进入交互式
        """
        log_file_f, log_time_f, log = self.get_log()
        # termlog = TermLogRecorder(User.objects.get(id=self.user.id))
        # termlog.setid(log.id)
        old_tty = termios.tcgetattr(sys.stdin)
        pre_timestamp = time.time()
        data = ''
        input_mode = False
        try:
            tty.setraw(sys.stdin.fileno())
            tty.setcbreak(sys.stdin.fileno())
            self.channel.settimeout(0.0)

            while True:
                try:
                    r, w, e = select.select([self.channel, sys.stdin], [], [])
                    flag = fcntl.fcntl(sys.stdin, fcntl.F_GETFL, 0)
                    fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, flag|os.O_NONBLOCK)
                except Exception:
                    pass

                if self.channel in r:
                    try:
                        x = self.channel.recv(10240)
                        if len(x) == 0:
                            break

                        index = 0
                        len_x = len(x)
                        while index < len_x:
                            try:
                                n = os.write(sys.stdout.fileno(), x[index:])
                                sys.stdout.flush()
                                index += n
                            except OSError as msg:
                                if msg.errno == errno.EAGAIN:
                                    continue
                        now_timestamp = time.time()
                        #termlog.write(x)
                        #termlog.recoder = False
                        log_time_f.write('%s %s\n' % (round(now_timestamp-pre_timestamp, 4), len(x)))
                        log_time_f.flush()
                        log_file_f.write(x)
                        log_file_f.flush()
                        pre_timestamp = now_timestamp
                        log_file_f.flush()

                        self.vim_data += x
                        if input_mode:
                            data += x

                    except socket.timeout:
                        pass

                if sys.stdin in r:
                    try:
                        x = os.read(sys.stdin.fileno(), 4096)
                    except OSError:
                        pass
                    #termlog.recoder = True
                    input_mode = True
                    if self.is_output(str(x)):
                        # 如果len(str(x)) > 1 说明是复制输入的
                        if len(str(x)) > 1:
                            data = x
                        match = self.vim_end_pattern.findall(self.vim_data)
                        if match:
                            if self.vim_flag or len(match) == 2:
                                self.vim_flag = False
                            else:
                                self.vim_flag = True
                        elif not self.vim_flag:
                            self.vim_flag = False
                            data = self.deal_command(data)[0:200]
                        data = ''
                        self.vim_data = ''
                        input_mode = False

                    if len(x) == 0:
                        break
                    self.channel.send(x)

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
            log_file_f.write('End time is %s' % datetime.datetime.now())
            log_file_f.close()
            log_time_f.close()
            #termlog.save()
            #log.filename = termlog.filename
            log.is_finished = True
            log.end_time = datetime.datetime.now()
            log.save()

    def connect(self):
        """
        Connect server.
        连接服务器
        """
        # 发起ssh连接请求 Make a ssh connection
        ssh = self.get_connection()

        transport = ssh.get_transport()
        transport.set_keepalive(30)
        transport.use_compression(True)

        # 获取连接的隧道并设置窗口大小 Make a channel and set windows size
        global channel
        win_size = self.get_win_size()
        # self.channel = channel = ssh.invoke_shell(height=win_size[0], width=win_size[1], term='xterm')
        self.channel = channel = transport.open_session()
        channel.get_pty(term='xterm', height=win_size[0], width=win_size[1])
        channel.invoke_shell()
        try:
            signal.signal(signal.SIGWINCH, self.set_win_size)
        except:
            pass

        self.posix_shell()

        # Shutdown channel socket
        channel.close()
        ssh.close()


class Nav(object):
    """
    导航提示类
    """
    def __init__(self, user):
        self.user = user
        self.user_id = user.id
        self.assets = AssetGroup.objects.filter(user_id=self.user_id)
        self.search_result = self.assets

    @staticmethod
    def print_nav():
        """
        打印提示导航
        """
        msg = """\n\033[1;32m###    简易堡垒机   ### \033[0m

        1) 输入 \033[32mID\033[0m 直接登录 或 输入\033[32m部分 IP,主机名,备注\033[0m 进行搜索登录(如果唯一).
        2) 输入 \033[32m/\033[0m + \033[32mIP, 主机名 or 备注 \033[0m搜索. 如: /ip
        3) 输入 \033[32mP/p\033[0m 显示你有权限的主机.
        4) 输入 \033[32mE/e\033[0m 批量执行命令.
        5) 输入 \033[32mH/h\033[0m 帮助.
        6) 输入 \033[32mQ/q\033[0m 退出.
        """
        print textwrap.dedent(msg)



    def search(self, str_r=''):
        # 搜索结果保存
        if str_r:
            try:
                id_ = int(str_r)
                if id_ < len(self.assets):
                    self.search_result = [self.search_result[id_]]
                    return
                else:
                    raise ValueError

            except (ValueError, TypeError):
                str_r = str_r.lower()
                self.search_result = AssetGroup.objects.filter(
                    Q(ip__contains=str_r) |
                    Q(hostname__contains=str_r) |
                    Q(comment__contains=str_r)
                    )
        else:
            self.search_result = self.assets

    @staticmethod
    def truncate_str(str_, length=30):
        str_ = str_.decode('utf-8')
        if len(str_) > length:
            return str_[:14] + '..' + str_[-14:]
        else:
            return str_

    @staticmethod
    def get_max_asset_property_length(assets, property_='hostname'):
        try:
            return max([len(getattr(asset, property_)) for asset in assets])
        except:
            return 30

    def print_search_result(self):
        hostname_max_length = self.get_max_asset_property_length(self.search_result)
        line = '[%-3s] %-16s %-5s  %-' + str(hostname_max_length) + 's  %s'
        color_print(line % ('ID', 'IP', 'Port', 'Hostname', 'Comment'), 'title')
        if hasattr(self.search_result, '__iter__'):
            for re in self.search_result:
                print line % (re.id, re.ip, re.port, self.truncate_str(re.hostname), re.comment)
            print
        else:
            if self.search_result:
                print line % (self.search_result.id, self.search_result.ip, self.search_result.port, self.truncate_str(self.search_result.hostname), self.search_result.comment)
            print

    def try_connect(self):
        try:
            asset = self.search_result[0]
            print('Connecting %s ...' % asset.hostname)
            ssh_tty = SshTty(asset)
            ssh_tty.connect()
        except (KeyError, ValueError):
            color_print('请输入正确ID', 'red')
        except ServerError, e:
            color_print(e, 'red')

    def exec_cmd(self):
        """
        批量执行命令
        """
        while True:
            roles = self.user_perm.get('role').keys()
            if len(roles) > 1:  # 授权角色数大于1
                color_print('[%-2s] %-15s' % ('ID', '系统用户'),  'info')
                role_check = dict(zip(range(len(roles)), roles))

                for i, r in role_check.items():
                    print '[%-2s] %-15s' % (i, r.name)
                print
                print "请输入运行命令所关联系统用户的ID, q退出"

                try:
                    role_id = int(raw_input("\033[1;32mRole>:\033[0m ").strip())
                    if role_id == 'q':
                        break
                except (IndexError, ValueError):
                    color_print('错误输入')
                else:
                    role = role_check[int(role_id)]
            elif len(roles) == 1:  # 授权角色数为1
                role = roles[0]
            else:
                color_print('当前用户未被授予角色，无法执行任何操作，如有疑问请联系管理员。')
                return
            assets = list(self.user_perm.get('role', {}).get(role).get('asset'))  # 获取该用户，角色授权主机
            print "授权包含该系统用户的所有主机"
            for asset in assets:
                print ' %s' % asset.hostname
            print
            print "请输入主机名或ansible支持的pattern, 多个主机:分隔, q退出"
            pattern = raw_input("\033[1;32mPattern>:\033[0m ").strip()
            if pattern == 'q':
                break
            else:
                res = gen_resource({'user': self.user, 'asset': assets, 'role': role}, perm=self.user_perm)
                runner = MyRunner(res)
                asset_name_str = ''
                print "匹配主机:"
                for inv in runner.inventory.get_hosts(pattern=pattern):
                    print ' %s' % inv.name
                    asset_name_str += '%s ' % inv.name
                print

                while True:
                    print "请输入执行的命令， 按q退出"
                    command = raw_input("\033[1;32mCmds>:\033[0m ").strip()
                    if command == 'q':
                        break
                    elif not command:
                        color_print('命令不能为空...')
                        continue
                    runner.run('shell', command, pattern=pattern)
                    ExecLog(host=asset_name_str, user=self.user.username, cmd=command, remote_ip=remote_ip,
                            result=runner.results).save()
                    for k, v in runner.results.items():
                        if k == 'ok':
                            for host, output in v.items():
                                color_print("%s => %s" % (host, 'Ok'), 'green')
                                print output
                                print
                        else:
                            for host, output in v.items():
                                color_print("%s => %s" % (host, k), 'red')
                                color_print(output, 'red')
                                print
                    print "~o~ Task finished ~o~"
                    print


def main():
    """
    主程序
    """
    if not login_user:
        color_print('没有该用户', exits=True)

    if not login_user.is_active:
        color_print('您的用户已禁用，请联系管理员.', exits=True)

    gid_pattern = re.compile(r'^g\d+$')
    nav = Nav(login_user)
    nav.print_nav()

    try:
        while True:
            try:
                option = raw_input("\033[1;32mOpt or ID>:\033[0m ").strip()
            except EOFError:
                nav.print_nav()
                continue
            except KeyboardInterrupt:
                sys.exit(0)
            if option in ['P', 'p', '\n', '']:
                nav.search()
                nav.print_search_result()
                continue
            if option.startswith('/'):
                nav.search(option.lstrip('/'))
                nav.print_search_result()
            elif option in ['E', 'e']:
                nav.exec_cmd()
                continue
            elif option in ['H', 'h']:
                nav.print_nav()
            elif option in ['Q', 'q', 'exit']:
                sys.exit()
            else:
                nav.search(option)
                if len(nav.search_result) == 1:
                    print('Only match Host:  %s ' % nav.search_result[0].hostname)
                    nav.try_connect()
                else:
                    nav.print_search_result()
                    nav.try_connect()

    except IndexError, e:
        color_print(e)
        time.sleep(5)

if __name__ == '__main__':
    main()
