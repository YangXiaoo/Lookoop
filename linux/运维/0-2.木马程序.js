#date(2018-4-8)
1)小程序
[root]# cd /usr/bin/yxmm 
#!/bin/bash
touch /tmp/yxmm.txt
while true
do 
	echo `date` >> /tmp/yxmm.txt
	sleep 1
done
[root]# chmod +x yxmm #执行权限

2)如何自动运行
[root]# vim /etc/rc.local #自动运行

crontab 
-------
排查容易

crontab -l 

查看： 
[root]# ll /var/spool/cron/ #展示所有用户的计划任务

高级的crontab篡改系统级别
[root]# cd /etc/ #或cd /etc/cron 
crontab  #系统具体时间的定时任务
cron.d/    		#系统级别的定时任务
cron.daily/ 	#系统每天要执行的任务
cron.hourly/ 
cron.monthly/
cron.weekly/

[root]# vim /etc/crontab
1 1 * * * root/usr/bin/yxmm & #后台
排查：	1.直接进入该文件查看
	 	2.利用md5sum 查看文件完整性，语法：md5sum 文件
	 		保存所有可能被入侵的文件哈希值
	 		[root]#  find /etc/cron* -type f -exec md5sum {} \; > /tmp/yymm.txt
	 	3.与其他型号服务器文件进行对比 vimdiff
上面排查方法都可以通用

开机启动
-------
/etc/rc.local 开机启动脚本

排查:直接测试或查看
[root]# grep -v ^$ /etc/rc.local #取消文档空行
[root]# vim /etc/init.d/httpd #/etc/init.d下的文件都是开机启动
start{}里面写入代码

父进程保护子进程
----------------
如何避免复制的时候的交互操作？
[root]# /bin/cp /tmp/1.txt /tmp/2.txt  #无交互操作

[root]# vim /etc/init.d/yxmm 
#!/bin/bash
#chkconfig: 12345 90 90 #90为开机顺序和关机顺序
#description:yxmm
case $1 in
start)
        /usr/bin/yxmm &
        ;;
stop)
        ;;
*)
        /usr/bin/yxmm &
        ;;
esac

[root]# service yx start #开启脚本 ,查看脚本是否运行
[root]#  chkconfig --add yx #开机启动脚本 
[root]# reboot #重启

[root]# tail -f /tmp/yxmm.txt #开机查看写入的脚本 


其他排查方法：
[root]# ls /etc/rc.d #或/etc/rc ，进入下面的文件找到开机文件，删除
init.d  rc0.d  rc1.d  rc2.d  rc3.d  rc4.d  rc5.d  rc6.d  rc.local
[root]# chkconfig --del yx #直接删除开机启动



总结
----
(1)md5值
(2)查找修改过的文件
[root]# find /etc/init.d/ -mtime -1 #查看被修改过的文件
(3)rpm 查看所有生成的文件是否被改动过
[root]# rpm -V 文件 
S.5....T.  /xx/xx 
注：
S file size 
MMode #模式不一样，包括许可和文件类型
5 MD5 sum 
DDevice #主从设备号不匹配
L readLink(2) #路径不匹配
UUser #属主
GGroup #属组
TmTime #时间


