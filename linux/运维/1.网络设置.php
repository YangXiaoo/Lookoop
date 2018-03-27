<?php
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
	[root]# nmtui 	#进入编辑界面
	可以修改网卡，ip，dns，网关。。。。。。
	重启网络服务
	[root]# systemctl network restart  #旧方法：service network restart

	2)通过修改网卡位置文件配置
	vim快捷键：
	i:进入插入模式
	保存：先按Esc,再按 :wq
	[root]# vim /etc/sysconfig/network-scripts/ifcfg-eth0 