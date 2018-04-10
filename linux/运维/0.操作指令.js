//date(2018-3-28)
[root]# pwd  #当前目录
[root]# ifconfig
[root]# ifconfig eth0 172.16.252.60 重启后就没有
//阿里云centos7.3修改后xshell不能连接，此时重启服务器
重启网络服务
[root]# systemctl restart network;  //centos7下
[root]# serverice network restart;  //centos6下

添加多个临时ip
[root]# ifconfig eth0 172.16.250.64
[root]# ifconfig eth0 172.16.250.63
临时删除ip
[root]# ifconfig eth0:0 del 172.16.250.63

NetworkManager
[root]# systemctl status NetworkManager
[root]# chkconfig NetworkManager on 	#开机开启NetworkManager
[root]# service NetworkManager start 	#立刻开启
[root]# ls /etc/sysconfig/network-scripts/  #网卡设置
[root]# nmtui 	#进入编辑界面，修改网卡地址
[root]# systemctl network restart  #旧方法：service network restart
[root]# vim /etc/sysconfig/network-scripts/ifcfg-eth0 #通过配置文件

防火墙
[root]# systemctl status firewalld 	#当前状态firewalld可以写成firewalld.service
[root]# systemctl stop firewalld.service
[root]# systemctl start firewalld.service
[root]# systemctl disable firewalld.service #开机不启动
[root]# systemctl enable firewalld.service  #开机启动
[root]# systemctl --list|grep firewalld.service  #centeos6开机启动

	临时关闭
	[root]# getenforce  #查看firewalld是否开启
	[root]# setenforce 0  #临时关闭
	永久关闭
	[root]# vim /etc/selinux/config
	#SELINUX=enforcing  改为
	#SELINUX=disabled
	[root]# reboot 	#重启服务

[root]# netstat -antup | grep sshd #查看端口状态
[root]# route -n  #查看默认路由
[root]# ping lxxx.site -c 3  -i 3  #ping

[root]#tty    #Teletype查看终端
[root]# echo shuchu > /dev/pts/1  #向终端/dev/pts/1  发消息
[root]# wall "关机了"  #向所有在线的终端广播消息

[root]# ls #查看文件
[root]# ls -l    #查看文件的详细信息
[root]# ls -a 	#查看所有文件，包括.开头的隐藏文件
[root]# ls -d   #查看目录，详细属性
[root]# ls -S   #大小写排序

[root]# alias vimeth0="vim /etc/sysconfig/network-scripts/ifcfg-eth0" 
[root]# vim vimeth0   #执行网卡修改命令
[root]# unalias vimeth0    #取消别名
[root]# vim /etc/bashrc  #永久设置别名，修改系统变量
[root]# vim /etc/profile #全局变量

[root]# cd ..  #进入上级目录
[root]# cd .    #进入当前目录
[root]# cd -    #切换到之前的目录

[root]# history    #查看历史命令。ctrl+r 关键字   ,输入后按右光标。!cd    匹配最近一条

快捷键
ctrl+
  ^C :停止前台当前进程
  ^D :退出，等价于exit
  ^L :清屏，等价于clear
  ^R :搜索历史命令
  ^A :调到命令开头
  ^E :调到命令行末尾
  ^U :将光标到开头的命令删除
  ^K :光标到末尾命令删除

!$ :引用上一个命令的参数

[root]# hwclock   #硬件时间
[root]# date      #系统时间
[root]# date -h   #查看帮助
[root]# date -s "2018-11-2 22:30"
[root]# date "+%F"	#完整日期

[root]# man 指令  #搜索：/字段 ，退出：q
[root]# 指令 -h   #和下面的一样
[root]# 指令 --help

[root]# shutdown [选项]
-r : 重启 
-h : 关机
-h 时间 ： 定时关机
-c : 取消关机

[root]# init [选项]
#0  停机（千万不能把initdefault 设置为0）
#1  单用户模式
#2  多用户，没有 NFS(和级别3相似，会停止部分服务)
#3  完全多用户模式，字符界面
#4  没有用到
#5  图形界面
#6  重新启动（千万不要把initdefault 设置为6）

[root]# systemctl set_default multi-user.target  #字符界面3
[root]# systemctl set_default graphical.target   #图形界面5

[root]# runlevel   #查看当前级别，显示两个旧和新
[root]# systemctl get_default  #查看当前级别

----------------文件----------------------
[root]# stat /etc/passwd   #查看文件状态
[root]# touch file{6..20}  #创建file.6 到 file.20文件
[root]#mkdir test.txt    #创建一个目录
[root]#mkdir -p /temp/a/b/c   #创建多个目录，前面加个-p
[root]# rm -rf file*  #以file开头的所有文件
[root]# cp /etc/passwd /opt/  #复制文件
[root]# cp -r /etc/passwd /opt/  #复制目录
[root]# cat /etc/passwd  #查看文件所有内容
[root]# more /etc/passwd  #查看文件
[root]# less /etc/passwd  #查看文件
[root]# head -n 3 /etc/passwd  #显示前三行
[root]# tail -n 3 文件名   #显示文件末尾三行
[root]# tail -f 文件名    #动态数据，一般查看日志
[root]# mv /etc/test.txt /tmp/mv.txt   #移动并修改名称


[root]# whereis useradd #查看命令所在目录，并且显示压缩包
grep过滤
[root]# grep x test.txt #过滤显示test.txt中的x内容
[root]# grep -v x test.txt #过滤显示test.txt中不为x开头的内容
[root]# grep ^x test.txt #过滤显示test.txt中的以x开头的内容
[root]# grep ^$ test.txt #过滤显示test.txt中空行开头内容

[root]# find ./ -name '*.txt'  查找以txt结尾的文件
[root]# find /etc/ -name 'host*'  查找以host开始的文件
[root]# find /etc/ -type d  #查找所有目录



-----------------------vim---------------------------------
永久设置环境：
[root]# vim /etc/.vimrc  #影响所有用户
[root]# vim ~/.vimrc  #只能影响当前用户

vim打开多个文件：
[root]# vim -o /etc/passwd /etc/hostname   #上下显示
[root]# vim -O /etc/passwd /etc/hostname   #左右显示，使用ctrl+ww切换编辑

[root]# vimdiff /etc/passwd test.txt  #比较文件内容

打开乱码解决方案：
[root]# iconv -f gb2312 -t utf8 test.txt  #test.txt文件乱码解决
文件串行解决：
[root]# rpm dos2nuix  #centos6需要安装dos2nuix
[root]# unix2dos test1.txt #解决串行
[root]# sz test1.txt #发送到windows本地

删除所有文件:
[root]# rm -rf/*   #删除所有文件*/

查看inode号：
[root]# stat test.txt  #查看文件状态
[root]# ls -i test.txt #直接显示inode号
[root]# ls -l test.txt #显示详细信息



[root]# free -m  #查看内存状态
[root]# systemctl status atd  #查看服务是否运行
[root]# ls /usr/lib/systemd/system  #查看所有服务命令
[root]# at -l #查看任务

[root]# vim /etc/crontab #系统计划任务
[root]# systemctl status crond #查看crond状态
[root]# systemctl restart crond #启动
[root]# systemctl enable crond #开机启动

[root]# crontab -e #创建一个计划任务
[root]# crontab -l #显示任务
[root]# crontab -r #删除计划任务