//date(2018-3-28)
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
[root]# vim /etc/bashrc  #永久设置别名

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