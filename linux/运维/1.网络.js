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

[root]# ping 指令
-c 数目 在发送指定的包后停止
-i 秒数 设定隔几秒送一个网络封装包给一台机器，预设值是一秒一次