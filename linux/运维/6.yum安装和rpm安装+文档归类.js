//data(2018-3-30)
[root]# umount /mnt/	#卸载/mnt/挂载
[root]# mount /dev/sr0 /mnt/	#安装
[root]# cd /mnt/Packages

包的结构 zsh-5.0.2-14.el7.x86_64.rpm 
zsh 名称
-5 版本号
.0 次版本号
.2 修订号
.el7 RHEL7版本，只能在RHEL7系统中用
.x86 CPU构架平台
64 支持系统位数
=====================================================
rpm:
-i,--install  安装软件包
-v,--verbose 提供更多的详细信息输出
-h,--hash  软件包安装时列出哈希标记，安装进程
--nodeps  不验证软件包依赖
[root]# rpm -ivh mariadb.server #需要手动安装依赖

查询功能：
	[root]# rpm -qa
	-a 查询所有已安装的软件包
	-f 查询文件所属软件包
	-p 查询软件包，通常用来查看还未安装的包
 	-i 显示软件包信息
 	-l 显示软件包中的文件列表
 	-d 显示被标注为文档的文件列表
 	-c 显示被标注为配置文件的文件列表
 	通常配合管道|more来使用 查看详细信息

 	[root]# rpm -Uvh mysql  #升级,很少用
 	[root]# rpm -e mysql #卸载
======================================================
yum(自动化安装):
[root]# yum install mariadb.server  #不需要手动安装依赖
	1) 安装 		yum install -y 
	2) 检测升级 	yum check-update
	3) 升级 		yum update 
	4) 软件包查询 	yum list
	5) 软件包信息 	yum info 
	6) 卸载 		yum remove xx -y  #不用写软件版本号
	7) 组安装		yum groupinstall "xx" -y #安装一组
[root]# cat /etc/redhat-release    #显示当前系统信息

=======================================================
源码编译安装
优点：可以安装最新版本，灵活，自定义参数，自定义安装目录
1) 解压包
	tar -zxvf 源代码包
	x 解包
	z 解压(仅适用于gzip,j适用于bz2)
	v 显示过程
	f 指定被解压包名
2) 配置
进入解压后的目录，用
.config[--prefix=/usr/local/filname --user=username --group=groupname]
来配置。这个过程主要是
用来收集系统信息，设置安装目录(卸载时只需将该目录删除)

3) 编译
	把源代码编译成可执行的二进制文件
	make -j 4
	注：-j 4表示以4个进程同时编译，速度快。 -j 后的数字与CPU核数一样

4) 安装 
	make install 

================================================================
						文档归类
================================================================

视频，图片本身就是压缩文件

tar用法：
	tar 选项 包 目标文件/目录
	[root]# tar cvf ni.tar /tmp/user   #归档
	c create创建
	v 详细信息
	f 文件 
linux不根据文件后缀识别文件
用file命令查看文件类型
	[root]# file test.txt
	[root]# du -sh /temp  #查看文件夹大小

压缩：gz,bz2,xz,zip,Z 

gz压缩语法： 
	[root]# tar zcvf newfile.tar.gz /tmp/user  #压缩 

解压：
[root]# tar zxvf newfile.tar.gz -C /opt/  #解压到/opt/目录

bz2归档加压缩：
[root]# tar jcvf new.tar.bz2 /etc/hostname  #对/etc/hostname进行压缩
解压：
[root]# tar jxvf new.tar.bz2 -C /opt/   #解压到/opt/目录

zip压缩
[root]# zip passwd.zip /etc/passwd  #/etc/passwd压缩为passwd.zip
[root]# zip grub.zip /etc/grub/     #/etc/grup压缩为grup.zip

解压
[root]# unzip grup.zip -d /opt/   #加压grup.zip到/opt/内 -d为指定路径

