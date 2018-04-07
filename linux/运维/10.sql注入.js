//date(2018-4-7)
SQLmap
sql注入点：能够提高sql语句的地方
防sql注入：验证码

安装SQLmap
DVWA(Dam Vulnerable Web Applicaotion)
搭建并登录

实战：实战sqlmap探测
1.实战枚举登录sql数据库的用户名与当前使用数据库


	进入sql injection，输入任意值，并提交。
	通过80端口。
2.枚举指定数据库的数据表
	mysql超级管理员root加密了，
	md5暴力破解
	hash值还原成明文
3.获取dvwa库中users表所有名
4.获取并dumo