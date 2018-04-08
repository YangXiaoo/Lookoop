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
虚拟机添加网卡桥接VIP和DIP,在服务器[root@0 ~]# setup 设置网卡   #设置后重启
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
--以下为指令实例
[root@]# ipvsadm -D -t   192.168.1.63:80  #删除集群
[root@]# ipvsadm -C  #清空所有设置
[root@]# ipvsdamin -d -t 192.168.1.63:80 -r 192.168.2.64  #删除一条记录 
选项：
	-a 表示添加real server 地址
	-r 指定real server地址
	-m 表示masquerade也就是NAT方式的LVS
[root@0 ~]# ipvsadm -L -n  #查看转发
[root@0 ~]# ipvsadm -L -n -c #查看链接数
参数：
	-L -n --stats  #查看分发情况
	-L -n --rate   #查看速率
[root@0 ~]# /etc/init.d/ipvsadm save  #保存修改内容
规则存储文件：
[root]# cat /etc/sysconfig/ipvsadm #查看配置文件信息,可以在此处修改配置


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
[root@1 ~]# elinks 192.168.2.63 --dump #直接浏览测试
测试VIP：
[root@1 ~]#elinks 192.168.1.63


==========================================================================
LVS-DR和LVS-IP TUN集群

DR模式(Direct Routing)：director分配请求到不同的real server。real service处理请求后直
接回应给用户，这样director负载均衡器仅处理客户机与服务器的一半连接。负载均衡器仅处理一
半的瓶颈，避免了新的性能瓶颈，同样增加了系统的可伸缩性。Director Routing 由于采用物理层
(修改MAC地址)技术，因此所有服务器都必须在一个物理网段。
IP Tunneling(IP隧道):director分配请求到不同的real server。real service处理请求后直接回
应给用户，这样director负载均衡器仅处理客户机与服务器的一半连接。IP Tunneling技术极大地
提高了director的调度处理能力，同时极大地提高了系统能容纳的最大节点数，可以超过100个节点。real server可以在任何LAN或WAN上运行，这意味着允许地理上的分布，在灾难恢复中有重要意义。服务器必须拥有正式的公网IP地址用于与客户机直接通信，并且所有服务器必须支持IP隧道协议。
Direct Routing和IP Tunneling区别：DR和IP TUN相比，没有IP封装的开销，但由于采用物理层
(修改MAC地址)技术，所有服务器都必须在一个物理网段。

DR实际拓扑结构：
客户端->分发器->real server ->公网->客户端
DR工作原理：MAC地址转换过程.
实战：
---------[root@1 ~]配置---------
[root@1 ~]为分发器主机
1.配置IP
方法一：
[root@1 ~]# ifconfig eth0 192.168.1.70  #直接添加分发器DIP
[root@1 ~]# ifconfig eth0:1 192.168.1.63  #直接添加负载均衡器虚拟IP
方法二：
[root@1 ~]# vim /etc/sysconfig/network-scripts  #进入配置文件所在目录
[root@1 ~]# vim ifcfg-eth0  #配置以下信息
IPADDR=192.168.1.70
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=202.106.46.151
[root@1 ~]# cp ifcfg-eth0 ifcfg-eth0:1 #配置VIP
DEVICE=eth0:1
NM_CONTROLLER=yes
IPADDR=192.168.1.63
ONBOOT=yes 



2.配置规则(提前安装ipvsadm)
[root@1 ~]# ipvsdamin -A -t 192.168.1.63:80 -s rr 
#[root@1 ~]# ipvsdamin -a -t 192.168.1.63:80 -s rr #错误代码

[root@1 ~]# ipvsdamin -a -t 192.168.1.63:80 -r 192.168.1.62 -g  #直接路由real server
[root@1 ~]# ipvsdamin -a -t 192.168.1.63:80 -r 192.168.1.64 -g  #直接路由
#-g 表示DR模式
[root@1 ~]# ipvsadm -L -n  #查看配置情况

2.1[root@2 ~]real server配置
1).配置ip eth0,桥接模式
[root@2 ~]# ifconfig eth0 192.168.1.62/24
lo 回环口
#[root@2 ~]# ifconfig lo:1 192.168.1.63 netmask 255.255.255.255 #lo:1为分发器VIP地址
#用以下方法生成
生成回环口配置文件：
[root@2 ~]# vim /etc/sysconfig/network-scripts  #进入配置文件所在目录
[root@2 ~]# cp ifcfg-lo ifcfg-lo:1
[root@2 ~]# vim ifcfg-lo:1
DEVICE=lo:1
IPADDR=192.168.1.63
NETMASK=255.255.255.0  #NETMASK=255.255.255.255为全匹配
#NETWORK=127.0.0.0  #注释掉或删掉
#BRODACAST=127.255.255.255  #删除或注释掉

3.关闭ARP(原因为VIP地址冲突)
#以下为关闭默认设置
#只回答目标IP地址是访问本网络接口(eth0)的APR请求查询，默认为0表示只要这台机器上
任何一个网卡设备上面有这个ip，就响应arp请求，并发送mac地址
[root@2 ~]# echo 1 > /proc/sys/net/ipv4/conf/eth0/arp_ignore
[root@2 ~]# echo 2 > /proc/sys/net/ipv4/conf/eth0/arp_announce
#对查询目标使用最适当的本地地址
[root@2 ~]# vim /etc/sysctl.conf #永久生效，在末尾添加一下内容
net.ipv4.conf.eth0.arp_ignore=1
net.ipv4.conf.eth0.arp_announce=2
[root@2 ~]# sysctl -p #设置内核生效


4.网关指向公网出口的路由器IP地址
[root@2 ~]# route -n #查看网关出口ip地址
[root@2 ~]# vim /etc/sysconfig/network-scripts/ifcfg-eth0 #修改网关地址
GATEWAY=192.168.1.1
[root@2 ~]# vim /etc/host
192.168.1.64 lxa.kim  #服务器域名
[root@2 ~]# echo '192.168.1.64' > /var/www/html/index.html #写入数据
[root@2 ~]# service httpd restart #重启或以下重启
[root@2 ~]# service network restart #重启

接下来配置另一个real server[root@3 ~]，重复2.1到3步骤

完成配置后测试！在分发器上测试不会成功！

========================================================================
LVS调度算法：
[root]# ipvsadm -h #算法
-s rr 轮询法
-s wrr 带权重的循环法
-s lc 最少连接法
-s wlc 带权重的最少连接法
-s sh 源散列法，同源同机器
---以下用的少
-s lblc 基于本地的最少连接法
-s dh 目标散列法
-s sed 最短预期延迟法
-s nq 永不排队法

调度算法配置成功后立即生效
1.rr round robin 
	在服务器池中无穷的循环遍历
2.wrr Weight Round Robin 
	基于集群节点可以处理多少来分配给每一个节点的权重值，权重值为2的服务器将受到权重值
	为1的服务器的两倍连接数量。如果服务器的权重为0，则不会收到新的连接请求(但当前已经建立的连接不会丢失)
3.lc Least Connection 
	当新的请求达到director时，director查看活动和非活动的连接数量，得到节点的开销值。最低开销
	值得节点胜出，被分给新的入战请求。
4.sh source hashing
	同一个Ip的客户端总是分发给一个real server
高级的用法是使用基于客户端session id 来保持会话。
haproxy可以实现基于会话信息来判断保持会话。
如何保持会话一致：
	1.如果总是保持和一个RS会话，这台RS如果故障了，要确定另一个RS也有会话信息，所有的RS保持数据同步
	方法：所有的RS把自己的会话信息保存到数据库中(memcached中)
......
HTTP的会话(session)信息：cookie，session

测试LVS多种调度算法如：LVS-DR wrr

[root@1 ~]# ipvsdamin -C #删除配置
[root@1 ~]# ipvsdamin -A -t 192.168.1.63:80 -s wrr 

[root@1 ~]# ipvsdamin -a -t 192.168.1.63:80 -r 192.168.1.62 -g -w 10 #直接路由real server
[root@1 ~]# ipvsdamin -a -t 192.168.1.63:80 -r 192.168.1.64 -g -w 20 #直接路由

[root@1 ~]# ipvsdamin -L -n --stats  #测试后查看状态,实测比值大概为配置的值



=================	
LINUX下ab网站压力测试命令
参数：
-n requests number of requests to perform 
	在测试会话中执行的请求总个数，默认时，仅执行一个请求
-c concurrency number of multiple requests to make 
	一次产生的请求个数，默认时一次一个。并发数

语法：ab -n 数字 -c 数字 连接
2000并发的情况下访问1000次
[root]# ab -n 1000 -c 2000 http://lxa.kim/index/html #测试并发
apr_socket_recv: Connection reset by peer (104) #若出现此信息则进行以下修改

#参考博客：https://www.cnblogs.com/archoncap/p/5883723.html
[root]# vim /etc/sysctl.conf 
net.ipv4.tcp_syncookies = 0
[root]# sysctl -p

测试得到的结果：
Requests per second:    13.32 [#/sec] (mean) #服务器每秒事务数
Time per request:       75053.987 [ms] (mean) #平均请求响应时间
Time per request:       75.054 [ms] (mean, across all concurrent requests) #每个请求时间
Transfer rate:          30.68 [Kbytes/sec] received #传输速率 可以帮助排除是否存在网络流量过大导致响应时间延长问题

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0 1964 2963.1      0    8610
Processing:     0 23929 29725.5  12634   75038
Waiting:        0 5371 8088.1    213   25858
Total:          0 25893 29200.9  15289   75038


\===============================================================================/
根据应用的不同使用LB七层，在应用层根据不同的应用分发。

工作中：nginx或apache
动态文件：apache,tomcat
图片文件：squid

使用nginx动态分离的负载均衡集群

1)基本知识
ngin的upstream目前最常用的3种方式分配
	1.轮询(默认)
		每个请求按时间顺序逐一分配到不同的后端服务器，如后端服务器down掉，能自动清除
	2.weight 
	用于后端服务器性能不均
	3.ip_hash
	每个请求按防访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。
	4.fair
	后端服务器响应时间来分配请求，响应时间短的优先分配
	5.url_hash

实例
----
