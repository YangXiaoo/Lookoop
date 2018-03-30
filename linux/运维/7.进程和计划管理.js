//date(2018-3-30)
进程：运行的程序，可能有多个进程

进程属性：
进程ID(PID): 唯一的数值，用来区分进程；
父进程和父进程的ID：父进程和子进程的关系为管理和被管理关系，当父进程被终止，子进程
	一定会被终止。反过来并不一定会。
启动进程的用户ID(UID)和所归属的组(GID)；
进程状态：运行R，休眠S，僵尸Z；
进程执行的优先级；
进程所连得终端名；
进程所占用：占用资源(内存，CPU占用量，读写磁盘量)

进程管理工具：ps,kill

-ps top管理进程
ps 提供进程的一次性查看，结果并不是动态连续的；如果想对进程时间控制，用top工具

ps 监视进程工具

参数：
常用组合aux
u 按用户名和启动时间的顺序来显示进程
a 显示所有用户的所有进程
x 显示没有控制终端的进程
l 长格式输出；
f 用树形格式来显示进程
r 显示运行中的进程
-e 显示所有进程包括没有控制终端的进程

[root]# ps -aux   #查看所有进程
USER：进程属组       
PID 
%CPU 
%MEM  
NI 进程优先级，nice值，负值表示高优先级，正值表示低优先级，优先级取值范围(-20,19)

VSZ   进程占用虚拟内存大小
RSS   固定的内存使用数量
TTY    进程启动的终端ID
STAT 进程状态
R  正在运行或在队列中可运行的
S  休眠状态
T 停止或被追踪
Z 僵尸进程(zombie)，父进程终止，子进程还在
N 优先级较低的进程
L 有些页被锁进内存
s 进程的领导者
START   启动时间
TIME 消耗时间
COMMAND 命令

ps -aux 是BSD的格式来显示进程(更多信息)
ps -ef是标准格式显示进程

top管理进程(类似于Windows的任务管理器)
系统整体，显示前五行
最长队列为 3x核数
top 快捷键：
空格：立即刷新
q：退出
M：按内存排序
P：按CPU排序
清空内存只是把buff/cache清空

=====================控制进程================
kill
用法 kill [进程号]
通过信号的方式来控制进程
[root]# kill -l   #进程
可以用9来终止进程
[root]# kill -s 9[进程号]  #强制关不进程
[root]# kill -9[进程号]	#强制关闭进程
[root]# killall  #终止所有进程

进程的优先级管理
进程的优先级定义：CPU是分时运行，所以可以同时运行多个程序

查看进程 ps -aux | grep xxx
[root]# nice -n -5 vim test.txt  #设置进程优先级以-5级别运行
[root]# nice  -5 vim test.txt  #设置进程优先级以5级别运行
[root]# ps -aux | grep vim  #查看进程号，grep为筛选
root      9429  0.0  0.2 151308  5024 pts/0    SN+  14:27   0:00 vim test.txt
[root]# top -p 9429  #查看运行级别
  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
 9429 root      25  -5  151308   5024   2580 S  0.0  0.3   0:00.02 vim

 改变正在运行的级别
 [root]# renice -n -6 vim test.txt  #改变正在运行进程的优先级


 [root]# free -m  #查看内存状态



=========================计划任务=============================
计划任务：at cron
------ 
at 一次性使用  #很少用
[root]# systemctl status atd  #查看服务是否运行
[root]# ls /usr/lib/systemd/system  #查看所有服务命令

使用：
[root]# at 16:20 #启动时间，20:00 2018-3-31，now +10min 都可以
at> mkdir /tmp/linux 
at> #ctl+v结束
[root]# at -l #查看任务

删除at计划任务
[root]# atrm 命令   #删除计划任务
[root]# atrm 计划任务编号   #删除计划任务
--------
cron命令
系统级别：
[root]# vim /etc/crontab #系统计划任务
[root]# systemctl status crond #查看crond状态
[root]# systemctl restart crond #启动
[root]# systemctl enable crond #开机启动

针对用户：
对于root用户
	命令：
	[root]# crontab -e #创建一个计划任务
	[root]# crontab -l #显示任务
	[root]# crontab -r #删除计划任务
	--------------------------
	[root]# crontab -e #写法
	分 时 日 月 星 谁做后面的事 命令
	例：每个月9，18,22号这几天的凌晨1点1分，执行一个备份脚本

	[root]# crontab -e #添加下列命令，:wq保存退出
	1 1 9,18,22 * * /root/back/bash 

	每月9-22号的1点1分执行：1 1 9-22 * * /root/back.sh 

	每五分钟执行：*/5 * * * * /root/back.sh 

anacron
情景：cron用控制循环执行工作，若执行命令时机器未开启，则机器重启后cron的脚本不会被执行


