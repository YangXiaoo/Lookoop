<?php
/**
 * @todo  mysql主从服务器
 * @time(2018-3-17)
 */
1.需要假设两台服务器
主服务器写 从服务器读
主服务器：
	ps -ef | grep mysql主从服务器	#运行状态
/**
 * ps:将某个进程显示出来
 * -A 　显示所有程序。 
 * -e 　此参数的效果和指定"A"参数相同。
 * -f 　显示UID,PPIP,C与STIME栏位。 
 * grep 命令是查找
 * 中间的|是管道命令 是指ps命令与grep同时执行
 */
2.	关闭防火墙，关闭selinux
	service iptables stop
	setenforce 0
3.修改/etc/my.cnf 
	vi /etc/my.cnf #主从服务器都要修改
	#service-id = 1 #主机可以设置为1，从机可以设置为IP最后一段（保证唯一）
	#log-bin=mysql-bin	#主从服务的核心，主服务器记录写操作日志。从服务器读取日志进行同步操作
	service mysqld restart #重启服务器

4.主服务器和从服务器数据库和表保持一致
	1) 登录数据库服务器
	mysql -uroot -p 
	#输入密码
	2) 创建测试数据
	create database test;
	3) 选择test数据库
	use test;
	4) 创建用于主从测试的数据表user
	create table user(
		id int(11) auto_increment primary key,
		name varchar(30)
		)
	engine=innodb,default charset=utf8;
------------前四步都一样操作--------------------
5.主服务器配置(创建一个专门用来同步数据的账号)
	mysql > grant replication salve on *.* to 'mysync'@'%' identified by '12345678'; #*.*:任意库任意表
	mysql > show master status; #查看状态，以后不要再进行任何操作
	#--得到的表有File 和Position 与6中配置的[File]和[Position]要一致
6.从服务器配置
	mysql > change master to master_host="xx.x.xxx.xx",master_user='mysync',
	master_password='123456',master_log_file='mysql-bin.[File]',master_log_pos=[Position];
	#[File]和[Position]要与主机状态显示的一致
	mysql > start slave 	#开启从服务器
	mysql > show slave status\G #查看从服务器状态，如下两项都为Yes表明从从成功.G-查看所有
		# 查看结果中：
		# Slave_IO_Running: Yes
		# Slave_SQL_Running: Yes
7.主服务器上进行插入数据测试
	mysql > insert into user(name) values('yangxiao');
	从服务器查看:
	mysql > select * from user;
	==============结束===========