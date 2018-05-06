[root]# nginx -s stop #停止服务
[root]# vim /usr/local/nginx/conf/nginx.conf
[root]# nginx -t #同步配置
[root]# /usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf #启动nginx 