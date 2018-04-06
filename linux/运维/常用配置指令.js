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