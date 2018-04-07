
桥接模式(Brige)
--------
将主机网卡与虚拟机的网卡利用虚拟机网桥进行通信。在桥接的作用下，类似于把物理主机虚拟为一个交换机，
然后桥接设置的虚拟机连接到这个交换机的一个桥接口上，物理机也同样插在这个交换机当中。
虚拟机ip地址需要与主机在同一个网段，如果需要联网，则网卡与DNS需要与主机网卡一致。


NAT(地址转换模式)
-----------------
在NAT模式下，虚拟主机需要借助虚拟机NAT设备和虚拟DHCP服务器，使得虚拟机可以联网。虚拟机和物理机共有一个Ip地址
虚拟机使用NAT时。linux系统要配置成动态Ip



1.1.linux网卡命名规则：
	centos6非固定，在centos6和之前的版本，网络接口使用连续号码命名：eth0,eth1等，当增加或删除网卡时可能名称改变。
	centos7采用dmidecode采集命名方案，以此来得到主板信息，可以实现网卡名永久化。(dmidecode这个命令可以采集有关硬件方面的信息)
	1)如果firmware或BIOS为主板上集成的设备提供的索引信息可用，且可预测则根据此索引进行命名：如ifcfg-ens33
	2)如果firmware或BIOS为PCI-E扩展槽所提供的索引信息可用，且可预测则根据此索引进行命名：如ifcfg-enp33
	3)若硬件接口的物理位置信息可用，则根据此信息进行命名例如：enp2s0
	上述均不可用时用传统方式
	在centos7中，en表示ethernet以太网，现在用的局域网
	enX：
		o:主板板载网卡，
		p：独立网卡，PCI网卡
		s:热插拔网卡，usb之类，扩展槽索引引号
		nnn数字表示：MAC地址+主板信息计算出的唯一序列


1.2 ifconfig 使用
--------------------------------------------------------------------------
[root]# ifconfig
//UP：表示网卡运行状态
//RUNNING：网线处理连接状态
//MULTICAST：支持组播
//mtu 1500：(maximum transmission unit)最大传输单元大小为1500字节
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
//IP地址，子网掩码，广播地址
        inet 172.16.252.65  netmask 255.255.255.0  broadcast 172.16.252.255
//网卡MAC地址，ether表示连接类型为以太网
//txqueuelen：传输列队的长度
        ether 00:16:3e:04:7c:26  txqueuelen 1000  (Ethernet)
//网卡发送数据包的统计信息和发送错误的统计信息
//dropped：丢失
        RX packets 776801  bytes 421119093 (401.6 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 430424  bytes 318612520 (303.8 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1  (Local Loopback)
        RX packets 414038  bytes 25674643 (24.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 414038  bytes 25674643 (24.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
------------------------------------------------------------------------
1.3 临时修改ip
	1) ifconfig 网卡名称 ip地址 子网掩码
	[root]# ifconfig eth0 172.16.252.60 重启后就没有
	//阿里云centos7.3修改后xshell不能连接，此时重启服务器
	重启网络服务
	[root]# systemctl restart network;  //centos7下
	[root]# serverice network restart;  //centos6下

	2)添加多个临时ip
	[root]# ifconfig eth0 172.16.250.64
	[root]# ifconfig eth0 172.16.250.63

	3)临时删除ip
	[root]# ifconfig eth0:0 del 172.16.250.63

1.4 networkManager概述
	networkManager服务是管理和监控网络设置的守护进程，CENTOS7之前通过network
	服务管理网络，之后的版本统一使用networkManager服务管理。它是一个动态
	的，事件驱动的网络管理服务。
	查看服务当前状态: 
	[root]# systemctl status NetworkManager
	[root]# chkconfig NetworkManager on 	#开机开启NetworkManager
	[root]# sysytemctl enable NetworkManger #开机启动
	[root]# service NetworkManager start 	#立刻开启

1.5 网卡设置
	[root]# ls /etc/sysconfig/network-scripts/
--------------------------------------------------------------------
ifcfg-eth0  ifdown-bnep  ifdown-ippp ifdown-post  ifdown-sit  ifdown-tunnel
  ifup-bnep  ifup-ippp  ifup-plip   ifup-ppp     ifup-Team      ifup-wireless      network-functions-ipv6
ifcfg-lo    ifdown-eth   ifdown-ipv6  ifdown-ppp     ifdown-Team      ifup           ifup-eth   ifup-ipv6  ifup-plusb  ifup-routes  ifup-TeamPort  init.ipv6-global   route-eth0
ifdown      ifdown-ib    ifdown-isdn  ifdown-routes  ifdown-TeamPort  ifup-aliases   ifup-ib    ifup-isdn  ifup-post   ifup-sit     ifup-tunnel    network-functions

----------------------------------------------------------------------
	ifcfg-eth0 ：网卡配置
	ifcfg-lo：网卡回环口
	[root]# ls /etc/resolv.conf
	[root]# cat /etc/resolv.conf   	#显示详细内容 cat ! $显示当前路径下详细文件
	nameserver 100.100.2.138
	nameserver 100.100.2.136 //服务器地址
	[root]# cat /etc/hosts #设置主机和Ip绑定信息
	[root]# cat /etc/hostname #设置主机名  [root@izwz9dnvbin1s0rrkbzr7jz ~]，@和~之间的为主机名

1.6 永久修改网卡地址
	1) 使用umtui文本框方式修改
	[root]# nmtui 	#进入编辑界面，修改网卡地址
	可以修改网卡，ip，dns，网关。。。。。。
	重启网络服务
	[root]# systemctl network restart  #旧方法：service network restart

	2)通过修改网卡位置文件配置
	vim快捷键：
	i:进入插入模式
	保存：先按Esc,再按 :wq
	[root]# vim /etc/sysconfig/network-scripts/ifcfg-eth0 
-------------------------------------------------------------------
DEVICE=eth0
ONBOOT=yes//网卡启动
//DNS1=192.168.1.1
//DNS1=192.168.1.2  多个DNS
BOOTPROTO=static //dhcp:动态获取ip地址，static：表示ip，none表示不指定，就是动态
IPADDR=172.16.252.65
NETMASK=255.255.255.0
//UUID:网卡名(唯一识别号)，不是MAC地址
---------------------------------------------------------------------
网关：从一个网络向另一个网络发送信息，也必须经过一道“关口”，这道关口就是网关

2.1 关闭防火墙
[root]# systemctl status firewalld 	#当前状态firewalld可以写成firewalld.service
[root]# systemctl stop firewalld.service
[root]# systemctl start firewalld.service
[root]# systemctl disable firewalld.service #开机不启动
[root]# systemctl enable firewalld.service  #开机启动
[root]# systemctl --list|grep firewalld.service  #centeos6开机启动

2.2 临时和永久关闭selinux
	临时关闭
	[root]# getenforce  #查看firewalld是否开启
	[root]# setenforce 0  #临时关闭
	永久关闭
	[root]# vim /etc/selinux/config
	#SELINUX=enforcing  改为
	#SELINUX=disabled
	[root]# reboot 	#重启服务

2.3 设置系统光盘开机自动挂载
	1)方法一  
	[root]# vim /etc/fstab   --文档后面增加以下内容
	/dev/cdrom    /mnt   iso9600 defaults 0 0
	退出保存

	2)方法二 
	[root]# echo "/dev/sr0/media iso9660 defaults 0 0" >> /etc/fstab
	cdrom为sr0/media的快捷方式

	验证挂载是否成功
	[root]# umount /mnt/
	[root]# ls /mnt/
	[root]# mount -a
	[root]# ls /mnt/

2.4 配置本地yum源
   	yum所配置在
   	[root]# cd /etc/yum.repos.d/
   	[root]# ls
   	创建新的yum源，结尾必须为repo
   	[root]# vim CentOs7.repo   #写入以下
   	-----------------------
   	[CentOS7]  #yum源的ID，必须唯一
   	name=CentOS- server #描述信息
   	baseurl=file:///mnt  #mnt表示光盘的挂载点
   	enabled=1  #启用
   	gpgcheck=0 	#取消验证
   	---------------------------

   	清空yum缓存
   	[root]# yum clean all   #清理缓存
   	[root]# yum list     #生成列表
   	[root]# yum install -y xx   #安装

==================================================================
//date(2018-3-30)
Linux和UDP采用16位端口号来识别应用程序 2^16=65536  最大65535
TCP/IP的临时分配1024-5000之间的端口，大于5000以上的是为其它服务保留

TCP端口号：
21 ftp 文件传输
22 ssh 安全远程连接
23 telnet 远程连接服务
25 smtp 电子邮件服务
53 DNS 域名解析服务
80 http web服务
443 https 安全web服务 

UDP端口：
69 tftp 简单文件传输协议
123 ntp 时间同步服务器(云主机，手机通过网络同步时间)
161 snmp 简单网络管理

[root]# cat /etc/servies #查看端口号

netstat查看端口监听状态
tcp端口:anpt  udp端口：anpu  
全部为：
-a,--all 
-n,--numeric 
-p,--programs
-t 显示tcp连接
-u 显示udp连接  
[root]# systemctl 
[root]# netstat -antup | grep sshd

[root]# route -n  #查看默认路由

[root]# ping lxxx.site -c 3  -i 3  #ping
-c 数目 在发送指定的包后停止
-i 秒数 设定隔几秒送一个网络封装包给一台机器，预设值是一秒一次
----------------------------------递归查询
[root]# vim /etc/named.conf  #修改配置 
