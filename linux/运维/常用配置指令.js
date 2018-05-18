[root]# vim /usr/locl/nginx/conf/nginx.conf #nginx配置文件
[root]# nginx -s reload #服务器重启
[root]# killall php-fpm  #关闭Php 另一种方法:pkill -9 php 
[root]# /usr/local/php/sbin/php-fpm #启动php
[root]# /usr/local/php/bin/php -m | grep memcache #查看是否扩展

查看mysql连接信息：
mysql> show processlist;
mysql> stats;
mysql> show status like '%connect%';

[root]# /usr/local/memcached/bin/memcached -m 64 -p 11211 -u root -vv #memcached 
[root]# telnet localhost 11211 #连接memcached


隐藏路径：
http://www.lxa.kim/Tp5/pulic/index/index/index
http://www.lxa.kim/pulic/index/index/index
# 匹配/public/开头的任何查询并且停止搜索。任何正则表达式将不会被测试。
location ^~ /public/ {
    #将public指向/Tp5/public目录
    #测试过程中，可以用 在结尾加上 redirect 查看跳转结果
    #rewrite ^/service/(.*)$  /Tp5/public/$1$2 redirect;
    rewrite ^/public/(.*)$  /Tp5/public/$1$2;
}

vim黄底解决：esc :nohl

代码录制：
[root]#  yum install -y asciinema
[root]# asciinema rec #ctrl+D结束

ssh配置：
[root]# passwd yangxiao #修改密码

以下方法错误：
[root]# vim /etc/ssh/sshd_config # 添加配置
AllowUsers:yangxiao
[root]# service sshd restart # 重启ssh 方法一
[root]# /bin/systemctl restart  sshd.service # 重启方法二

[root]# vim /etc/sudoers 
## Allows people in group wheel to run all commands
%wheel    ALL=(ALL)    ALL
[root]# usermod -g root yangxiao


--------------------------------------------------------
系统网络服务关闭
[root]# killall php-fpm 
[root]# nginx -s stop 
or [root]# /usr/local/nginx/sbin/nginx -s stop
[root]# service httpd stop


-------------------------------------------------------- 
Django 基本操作命令

1.7以下版本数据库同步
[root]# python manage.py syncdb