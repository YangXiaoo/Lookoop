<?php
/**
 * @todo  均衡负载
 * @time(2018-3-17)
 */
准备：每台服务器都要安装nginx，至少三台服务器
1. 关闭防火墙
	service iptables stop
2. 关闭selinux
	setenforce 0
3.安装基本依赖
	yum install -y gcc pcre-devel openssl-devel
4.安装nginx
	useradd www -s /sbin/nologin #创建nginx运行账户www，不允许直接登录系统
	tar -zxvf nginx-1.11.5.tar.gz
	cd nginx-1.11.5

	./congigure --prefix=/usr/local/nginx --without-http-memcached_module --user=www --group=www --with-http_stub_status_module --with-http_ssl_module
	make && make install

	设置nginx开机启动
	cp /lnmp/src/nginx /etc/rc.d/init.d/ #拷贝启动文件
	chmod 775 /etc/rc.d/init.d/nginx     #赋予文件执行权限
	chkconfig nginx on 					 #设置开机启动
	service nginx start 				 #启动nginx
5.配置nginx
主机：(作为负载均衡服务器)
	cd /usr/local/nginx/html 	#存放站点更目录
	ls 
	vi index.html
	#
	#load balance
	#
	ifconfig
web-1：
	cd /usr/local/nginx/html 	#存放站点更目录
	ls 
	vi index.html
	#
	#web-1
	#
web-2：
	cd /usr/local/nginx/html 	#存放站点更目录
	ls 
	vi index.html
	#
	#web-2
	#
------------------------------------------------------
名称			|		IP 			|	功能
load balance	|		xx.x.xxx.x0	|	负责任务的分配
web-1 			|		xx.x.xxx.x1 |	实际提供服务
------------------------------------------------------
进入负载均衡服务器配置:
	cd ..	#进入上一级
	ls 
	#显示当前文件夹...
	cd conf/
	#进入文件...
	pwd 					#显示当前目录  -p完整显示
	#目录地址...
	vi nginx.conf 			#修改配置
	#...
	#gzip on;
	#---添加连接池--
	#upstream lb {
	#	service xx.x.xxx.x1 weight=5;
	#	service xx.x.xxx.x2 weight=1;
	#}---默认为轮询
	#service{
	#...
	#	location / {
	#		proxy_pass http://lb; 							#指定代理连接池
	#		proxy_set header Host $host;					#转发请求头信息
	#		proxy_set_header X-Forward-For $remote_addr;	#转发请求Ip地址
	#		
	#	--注释掉下面两行--
	#		#root html;
	#		#index index.html index.htm;
	#	}
	#}
	:wq #保存修改
	service nginx restart 
	#nginx重新启动...

	