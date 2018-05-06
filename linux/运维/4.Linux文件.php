<?php 
/**
 * date(2018-3-28)
 * Linux文件
 */
[root@yangxiao ~]# ls /
bin  boot  dev  etc  home  lib  lib64  linux  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

/：处于linux系统树形结构的最顶端，linux的入口文件
bin: binary(二进制)，常用二进制命令
boot: 存放的系统启动相关文件
dev：device的缩写，设备文件目录
	设备文件：/dev/sda,/dev/sda1,/dev/tty1,/dev/tty2,/dev/pts/1,/dev/zero,/dev/null,/dev/cdroom
etc: 常用系统二进制安装包配置文件默认路径和服务器启动命令目录
	passwd 用户信息文件
	shadow 用户密码文件
	group 存储用户组信息
	fstab 系统开机启动自动挂载分区列表
	hosts 设定用户自己的IP与主机名对应的信息
home：普通用户家目录
lib: 库文件存放目录
lost+found: 默认为空，被FSCK(file system check)用来放文件的，centos6才有
mnt: 临时挂载设备
opt:一般为空目录
proc：操作系统运行时，进程信息与内核信息。不是真正的文件系统，该目录是虚拟的，是内存映射的目录。这个文件存在内存，不存在磁盘
	du -sh /etc/
	du -sh /proc 
	cat /proc/meminfo |grep "Mem"  #内存信息
	cat /proc/cpuinfo	#CPU信息
sys:系统目录
run：运行目录，系统运行时存放的目录,比如服务运行时的PID(进程号)文件
sbin:超级管理员，涉及系统管理的目录
srv:服务目录
tmp：临时文件，定时清理，不能存放重要程序
	drwxrwxrwt. 13 root root 4096 Mar 29 20:03 /tmp ，只能被owner和root删除覆盖
usr:存放应用程序文件，第三方文件
var：系统运行和软件运行产生的日志信息，该目录的内容是经常变动的
==============================================
文件管理
创建/修改/移动/删除  touch mkdir mv vi rm cp 

创建 touch 
	如果空文件怎创建，若文件非空则改变文件时间
	查看文件状态 [root]# stat /etc/passwd   #查看文件状态
	Access:最近获取时间 cat 
	Modify:最近修改时间 vim
	Change:最近改变属性 chmod 
	[root]# touch file{6..20}  #创建file.6 到 file.20文件

创建 mkdir
	创建普通目录
	[root]#mkdir test.txt    #创建一个目录
	[root]#mkdir -p /temp/a/b/c   #创建多个目录，前面加个-p
	-Z：设置安全上下文，当使用SELinux时有效；
    -m<目标属性>或--mode<目标属性>建立目录的同时设置目录的权限；
    -p或--parents 若所要建立目录的上层目录目前尚未建立，则会一并建立上层目录；
    --version 显示版本信息。
删除文件和目录 rm
	选项：
	-f, --force   ignore nonexistent files and arguments, never prompt
	-r, -R, --recursive   remove directories and their contents recursively

	[root]# rm -rf file*  #以file开头的所有文件

复制文件 cp 
	命令：cp  源文件/目录  目录文件/目录
	选项：-R/r，递归处理，指定目录下所有文件与子目录一并处理，一般用于复制文件目录
	[root]# cp /etc/passwd /opt/  #复制文件
	[root]# cp -r /etc/passwd /opt/  #复制目录

查看文件 cat 
	[root]# cat /etc/passwd  #查看文件所有类容
	more(查看文件):
		用法 more 文件名
		说明：按下回车刷新一下，按下空格刷新一屏，输入q退出，不支持后退
		[root]# more /etc/passwd  #查看文件
	less:和more一样，但功能更强大
		用法：less 文件名
		说明：up前页，down后页；enter向下翻一行，输入q退出
		[root]# less /etc/passwd  #查看文件
	head:显示前n行
		用法:head -n 3 文件名
		[root]# head -n 3 /etc/passwd  #显示前三行
	tail:显示文件尾部结尾
		[root]# tail -n 3 文件名   #显示文件末尾三行
		[root]# tail -f 文件名    #动态数据，一般查看日志

移动 mv 
	[root]# mv /etc/test.txt /tmp/mv.txt   #移动并修改名称

排序：
[root]# sort files#排序
	参数：p80
=============================================================
xfs文件系统的备份和恢复

xfsdump的备份级别分为两种：
0 完全别分
1-9 增量备份

完全备份： 每次都把指定的备份目录完整的复制一遍，不管目录下的文件是否有变化
增量备份: 每次将之前(第一次，二次，直到前一次)做过的备份之后有变化的文件备份
差异备份：每次都将第一次完整备份以来有变化的文件进行备份

==============================================================
date(2018-3-30)

[root]# whereis useradd #查看命令所在目录，并且显示压缩包

grep过滤
[root]# grep x test.txt #过滤显示test.txt中的x内容
[root]# grep -v x test.txt #过滤显示test.txt中不为x开头的内容
[root]# grep ^x test.txt #过滤显示test.txt中的以x开头的内容
[root]# grep ^$ test.txt #过滤显示test.txt中空行开头内容

find:
在目录总搜索文件
find pathname -options [-print]

-options:
	-name 文件名
	-prem 文件权限
	-user 按照文件属性
	-mtime -n +n 文件更改时间
		-n 距离现在n天以内
		+n n天前

[root]# find ./ -name '*.txt'  查找以txt结尾的文件
[root]# find /etc/ -name 'host*'  查找以host开始的文件
[root]# find /etc/ -type d  #查找所有目录

