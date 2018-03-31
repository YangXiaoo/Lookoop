//date(2018-3-30)
DNS(Domain Name System)域名系统，在TCP/IP中提供域名与IP地址的解析服务。
NDS是一个分布式数据库，命名系统采用层次的逻辑结构，如同一棵倒置的树，逻辑树形结构成为域名空间
由于DNS划分了域名空间，所以各机构可以使用自己的域名空间创建NDS信息。
注：DNS域名空间中，书的最大深度不超过127层，数中每个节点最长可以存储63个字符。
1)域和域名
	NDS树的每一个节点代表一个域，通过这些节点，对整个域名空间划分，成为一个层次结构。
	域名：通常由一个完全合格域名(FQDN)标识。FQDN能准确标识出相对于DNS域树根的位置，
	也就是节点到DNS树根的完整表述方式，从节点到树根采用反向书写，并将每个节点用"."分隔。
	通常：FQDN有严格的命名限制，长度不超过256字节，只允许a-z,0-9,A-Z和减号(-)。 
由最顶层到下层：根域，顶级域，二级域，子域

"."全球有13个根(root)服务器	
顶级域：
	组织域 采用三个字符代表如com，edu,gov,mil,net,org(非盈利组织),int(国际机构组织)
	地址域 采用两个字符的国家或地区代号。如cn,kr,us 
	反向域 特殊域
区(zone)：DNS名称空间的一部分，包含了一组存储在DNS服务器上的资源

主域名服务器和辅助域名服务器: 防止主服务器崩溃
特点 容错能力，减少广域链路的通信量，减轻主服务器的负载

DNS服务器 
	运行DNS服务器程序的计算机，存储NDS数据库信息，尝试解析客户机的请求。
DNS缓存 有请求若本地没有查询其它服务器，得到结果缓存到本地服务。

DNS查询方式：递归查询和迭代查询
递归查询：一次性沟通完，是一种DNS查询模式，该模式下服务器接到客户机请求，必须使用一个
	精准的查询结果回复客户机，若没有查询到，会从其他服务器并将结果提交给客户机。
	客户端与本地服务器的传输。
迭代查询：不会具体的查询结果，接受请求时，告诉客户机另一台DNS服务器地址，依次查询。NDS
	服务器之间的交互查询。

正向解析：域名到IP
反向解析：IP到域名

DNS资源记录：
	1)SOA资源记录(Start of Authority Record)
	2)NS资源记录
		NS(Name Server)记录是域名服务器记录，用来指定该域名由哪个DNS服务器来进行解析。
	3)A资源记录(Address)
		地址A资源记录把FQDN映射到IP地址
	4) PTR资源记录
		相当于A资源记录，指针(PTR)记录把IP地址映射到FQDN，用于反向查询，通过IP地址，找到域名。
	5)CNAME资源记录
		别名记录(CNAE)资源记录创建特定FQND的别名。用户可以使用CNAME记录来隐藏用户网络的实现
		细节，使连接的客户机无法知道真正的域名。
	6)MX资源记录
		邮件交换(MX)资源记录。为DNS域名指定邮件交换服务器。

模式：C/S模式

端口号：
tcp/53 udp/53	#客户端查询
tcp/93 udp/93  #用于DNS主从同步

======安装NDS
BIND软件
[root]# yum -y install bind*	#安装bind
[root]# systemctl start named.service  #开启named
[root]# ps -aux | grep named #查看named进程
[root]# netstat -an|grep :53 #检查named工作是否正常，监口为53
[root]# ls /var/named/chroot/etc/  #查看文件
[root]#
[root]#
[root]#

例：配置服务器解析：lxxx.site
[root]# vim /etc/named.conf #修改文件配置
整体分三段：
options 对全局生效
zone 针对某个区域

配置正向解析区域
授权DNS服务器管理lxa.kim区域，并把该区域的区域文件命名为lxxx.site

[root]# vim /etc/named.conf 
[root]# vim /etc/named/chroot/etc/named.conf
--------------------
13 listen-on port 53 { any; };  #改为any
14        listen-on-v6 port 53 { any; };  #改为any
19       allow-query     { any; };  #改为any
31        recursion no;  #公网关闭递归
57 zone "lxxx.site" IN {   #插入zone，创建区域
58         type master;
59         file "lxxx.site.zone";
60 };
--------------------
[root]# cp -p /var/named/named.localhost  /var/named/lxxx.site.zone
[root]# vim /var/named/lxxx.site.zone  #配置文件
--------------------------------------
  1 $TTL 1D   
  2 lxxx.site.      IN SOA  dns.lxxx.site. root.lxxx.site. (  
  3                                         0       ; serial
  4                                         1D      ; refresh
  5                                         1H      ; retry
  6                                         1W      ; expire
  7                                         3H )    ; minimum
  8 lxxx.site.      NS      dns.lxxx.site.
  9 dns.lxx.site.   A       121.42.124.167
 10 www.lxxx.site.   A       121.42.124.167
 11 www1.lx.site.    CNAME   www.lxa.kim
--------------------------------------
$TTL 1D
@	IN SOA	@ rname.invalid. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	@
	A	127.0.0.1   
	AAAA	::1

---------------------------------------
$TTL 1D  #设置有效地址解析记录的默认缓存时间，默认时间为1D，也就是一天
原来的@表示当前的域 lxxx.site.
设置SOA记录为：dns.lxxx.site.  #配置时要把根 . 写上
域名地址邮箱 root.lxxx.site.cn ，由于@有其它含义，所以用"."代替@
0	; serial  跟新序列号，用于标记数据库的变换，可以在10位内
1D	; refresh  刷新时间，从域名服务器更新改地址数据库文件的间隔时间，默认为1天
1H	; retry  重试延时，从域名服务器更新地址数据库失败以后，等待多长时间，默认为一小时
1W	; expire  到期，失效时间，超过该时间仍无法更新地址数据库，则不再尝试，默认为一周
3H 设置无效地址解析记录(该数据库中不存在的地址)默认缓存时间。设置无效记录最少缓存时间为3小时
SOA资源记录
NS 域的授权名称服务器
MX 域的邮件交换器，要跟一个优先级，越小越高
A IPV4主机地址
AAAA IPV6主机地址
PIR 解析IP的指针
CNMAE 权威(正式)名称，定义别名记录

[root]# systemctl restart named.service   #重启
[root]# vim /etc/sysconfig/network-scripts/eth0  #添加
DNS1=121.42.124.167
[root]# systemctl restart network   #重启网络服务
[root]# ping www.lxxxa.site -c -3  #查看是否成功



======递归查询 
[root]# vim /etc/named.conf   #修改文件配置,注释下面两行代码
#   dnssec-enable yes;
#  dnssec-validation yes;
重启修改DNS生效


======搭建DNS转发服务器
[root]# vim /etc/named.conf  #添加下列两行
forward only;			#only只转发，first先查找本地zone，再转发
forwarders {8.8.8.8};  #转发的服务器



=====主从服务器
[root]# vim /etc/named.conf  #主服务器配置
57 zone "lxxx.site" IN {   #插入zone，创建区域
58         type master;
59         file "lxxx.site.zone";
           allow-trnsfer {192.168.1.0/24;}; #指定允许哪个网段的从DNS服务器，
           									#可以同步主DNS服务器
60 };

[root]# vim /etc/named.conf  #从服务器配置
57 zone "lxxx.site" IN {   #插入zone，创建区域
58         type slave;
59         file "slave/lxxx.site.zone.file";
           master {192.168.1.63;}; #指定主服务器
60 };
