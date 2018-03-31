//date(2018-3-31)
集群(cluser)就是一组计算机，它们作为一个整体向用户提供一组网络资源，
这些耽搁计算机系统就是集群的节点(node).

集群种类：
	负载均衡：(Load Balance)集群，简称LB，多台一起工作
	高可用(Hight Availability)集群，简称HA集群，防止单点故障
	高性能计算机(High Perfermance Computeing)集群，简称HPC集群

LB实现手段：
	硬件： F5负载均衡器
	软件：LVS(4层，传输层) Nginx(7层，应用层)

	LVS(Linux Virtual Server),是一个虚拟的服务器集群系统。
	采用三层结构：
	1)分发器/负载调度器 它是整个集群对外面的前端机，负责将客户的请求发送到一组服务器上
	执行，而客户认为服务是来自一个IP地址
	2)服务池(server pool)
	真正执行客户请求的服务器，执行的服务有WEB,MAIL,FTP，DNS
	3)共享存储(shared storge)
	为服务器池提供一个共享的存储区

LVS负载均衡的三种包转发方式
	NAT(网络地址映射),IP Tunneling(IP隧道)，Direct Routing(直接路由)。
	NAT：通过网络地址转换，需要重新写入，能力有限
	IP Tunneling(IP隧道)：提高director的分发能力。
	Direct Routing(直接路由)：只能在同一个局域网里

实例：LVS NAT模式(网络地址转换)
1.准备三台机器 [root@0 ~]为分发器 1和2为服务池 real server
2.iptables -F 
3./etc/selinux/config #关闭selinux
	#SELINUX=enforcing  改为
	#SELINUX=disabled

1)打开路由转发功能
[root@0 ~]# vim /etc/sysctl.conf #打开路由转发功能
[root@0 ~]# sysctl -p  #让配置生效
2)配置网络环境
虚拟机添加网卡桥接VIP和DIP,在服务器 0 中[root@]# setup 设置网卡   #设置后重启
eth0 192.168.1.63 模式:br0 模拟公网 VIP
DIP：eth3 192.168.2.62 模拟分发器 网卡模式 VMnet4
网关设置为 255.255.255.0
#一下两个为新建网卡
eth1 192.168.2.63 模式：VMnet4  模拟独立网络,realserver  RIP
eth2 192.168.2.64 模式：VMnet4 模拟独立网路,realserver  RIP
安装LVS管理工具：ipvadmin 
[root@0 ~]# yum -y install ipvadm #安装 
[root@0 ~]# ipvsdamin -A -t 192.168.1.63:80 -s rr 
选项：
	-A 添加 
	-t: TCP协议的集群 
    -u: UDP协议的集群 
    service-address:     IP:PORT 
    -f: FWM: 防火墙标记 
    service-address: Mark Number
	VIP:PORT 
	-s 指定调度算法
	rr 表示round-robin 轮询
[root@0 ~]# ipvsdamin -a -t 192.168.1.63:80 -r 192.168.2.63 -m  #转发
[root@0 ~]# ipvsdamin -a -t 192.168.1.63:80 -r 192.168.2.64 -m  #转发 
[root@0 ~]# ipvsadm -D -t   192.168.1.63:80  #删除集群
选项：
	-a 表示添加real server 地址
	-r 指定real server地址
	-m 表示masquerade也就是NAT方式的LVS
[root@0 ~]# ipvsadm -L -n  #查看转发
参数：
	-L -n --stats  #查看分发情况
	-L -n --rate   #查看速率
[root@0 ~]# /etc/init.d/ipvsadm save  #保存修改内容



服务池：网关地址为分发器的IP地址
配置real server IP:
主机1：eth1 :VMnet4  192.168.2.63  网关：192.168.2.62
主机2：eth2：VMnet4  192.168.2.64  网关：192.168.2.62
将桥接模式改为VMnet4
通过ssh 192.168.2.63 连接主机

[root@1 ~]# yum -y install httpd   #安装Apache
[root@1 ~]# service httpd restart   #重启
[root@1 ~]# vim /etc/httpd/conf/httpd.conf  #找到ServerName 改为 192.168.2.63:80
[root@1 ~]# service httpd restart #重启
[root@1 ~]# echo "192.168.2.63" > /var/www/html/index/html #添加数据 

[root@2 ~]# yum -y install httpd   #安装Apache
[root@2 ~]# service httpd restart   #重启
[root@2 ~]# vim /etc/httpd/conf/httpd.conf #找到ServerName 改为 192.168.2.64:80
[root@2 ~]# service httpd restart #重启
[root@2 ~]# echo "192.168.2.64" > /var/www/html/index/html #添加数据 

测试realserver：
[root@1 ~]# yum install elinks  #安装文本浏览器 
[root@1 ~]# elinks 192.168.2.63  #直接浏览测试
测试VIP：
[root@1 ~]#elinks 192.168.1.63