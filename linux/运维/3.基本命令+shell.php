<?php
/**
 * date(2018-3-28)
 */
查看终端：
[root]#tty    #Teletype查看终端
/dev/pts/0  #阿里云网页发起的连接终端：/dev/pts/1
注：shift+ctrl+N快读打开一个终端

不同终端的通信
[root]# echo shuchu > /dev/pts/1

	对所有终端广播消息：系统十分钟后关机
	[root]# shutdown +10   #十分钟后关机
	[root]# shutdown -c   #取消关机

	广播
	[root]# wall "关机了"

==============================shell==========================
#和$区别：#root用户，$普通用户
[root]# cat /etc/shells   #查看shell类型，所用指令
[root]# head -1 /etc/passwd  #查看当前用户使用什么指令
1.文件
[root]# ls #查看文件
[root]# ls -l    #查看文件的详细信息
[root]# ls -a 	#查看所有文件，包括.开头的隐藏文件
[root]# ls -d   #查看目录，详细属性
[root]# ls -S   #大小写排序
ls-l与ll命令相同

文件类型：
	d:目录文件(document)
	l:链接文件(symbol link)
	b:块设备文件(block)
	c:字符设备文件(character)
	p:管道文件(pipe)
	-:表示普通文件

文件颜色：
	蓝色：目录
	黑色：文件
	浅蓝色：链接
	红色：压缩文件
	绿色：可执行文件
	黑底黄字：设备文件
-----------------------
2.别名
//下列命令临时有效
[root]# alias vimeth0="vim /etc/sysconfig/network-scripts/ifcfg-eth0" 
[root]# vim vimeth0   #执行网卡修改命令
[root]# unalias vimeth0    #取消别名
//永久设置别名
[root]# vim /etc/bashrc
//在最后面添加：alias vimeth0="vim /etc/sysconfig/network-scripts/ifcfg-eth0"
-------------------
3.切换目录
[root]# cd ..  #进入上级目录
[root]# cd .    #进入当前目录
[root]# cd -    #切换到之前的目录

---------------------
4.历史命令history
[root]# history    #查看历史命令
快捷键：
	ctrl+r 关键字   ,输入后按右光标
	!cd    匹配最近一条
-----------------------------
5.其余快捷键
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


---------------
6.系统时间
硬件时钟：BIOS,系统时钟：Kernel
[root]# hwclock   #硬件时间
[root]# date      #系统时间
[root]# date -h   #查看帮助

时区：	UTC(Universal Time Coordinated)
		CST(China Standard Time)
		GMT(Greenwich Mean Time)

[root]# date -s "2018-11-2 22:30"
[root]# date "+%F"	#完整日期
------------------
查看帮助：
[root]# man 指令  #搜索：/字段 ，退出：q
//下面两个一样
[root]# 指令 -h
[root]# 指令 --help
------------------------
7.开关机
关机(两种方法)：
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
---------------------------
8.默认的运行界面
[root]# systemctl set_default multi-user.target  #字符界面3
[root]# systemctl set_default graphical.target   #图形界面5

查看当前级别
[root]# runlevel
[root]# systemctl get_default



==========================================================
					BASH脚本
==========================================================
[root]# vim first.sh
------------------
#! /bin/bash  #主要是为了声明为bash解释器，不是注释，有用
#This is my first shell script  #注释信息不生效
mkdir /tmp/shell/ 
ifconfig
----------------:wq保存退出
[root]# chmod +x first.sh #权限
[root]# ./first.sh   #执行



执行脚本的不同方式;
	绝对路径
	相对路径
	sh  路径/脚本名.sh    #不需要执行权限
	bash  路径/脚本名.sh    #不需要执行权限,与上一中方法一样的

shell中的变量
定义：可以存放一个可变值得空间
常见变量：自定义变量，环境变量，位置变量，预定义变量
一般echo输出

1) 自定义变量 
	不需要提前声明，而是直接指定变量名并赋给初始值
	定义变量格式：变量名=变量值，两边没有等号
	height=170
	[root]# echo $height #170
	[root]# echo ${height}systemctl #170systemctl
	[root]# read weight height
		170 135
	[root]# $weight $height  #170 135
	[root]# read -p "input your password" passwd #提示符

数值运算：
	格式 变量1 运算符 变量2    
	+  -  \*  /  %
	[root]# A=10 B=20
	[root]# expr $A + $B   #30

2) 环境变量
	环境配置变量文件再/etc/profile(全局)
	用户宿主目录/home/root/.bash_profile(局部)
	[root]# env 变量  #环境变量
	$PATH 只有执行的命令在path变量包含的目录下，才能直接使用
	$USER $SHELL $HOME $LANG 