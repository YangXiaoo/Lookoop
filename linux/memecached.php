<?php
/**
 * @todo  高性能的分布式内存对象缓存,提高数据库读写能力。内存中缓存数据和对象来减少读取数据库的次数。MySQL通过磁盘读取。
 * @date(2018-3-18)
 */
1.搭建LNMP环境
2.安装基本依赖
	yum install -y libevent-devel
3.安装memcached
	tar -zxvf memecached-1.4.33.tar.gz
	cd memecached1.4.33
	./configure --prefix=/usr/local/memecached --enable-64bit
	make && make install

	开启服务:
		cd /usr/memecached/bin 
		./memcached -u www -d 
		-p : 指定端口，默认为11211
		-m : 指定内存，根据自己硬件设置
		-u : 指定用户，不能是root
		-d : 后台运行
4.安装 libmemecaced
	tar -zxvf libmemecaced-1.0.18.tar.gz 
	cd libmemecaced-1.0.18
	./configure --prefix=/usr/local/libmemecached --with-memecached
	make && make install 
5. 安装php-memcached-php7
	phpize
	./configure --with-php-config=/usr/local/php7/bin/with-php-config
	--with-libmemecached-dir=/usr/local/libmemecached/
	make && make install
	将上不得到的路径添加到php配置文件：usr/loacl/php7/etc/php.ini 
	extension="/usr/local/php7/lib/php/extensions/no-debug-non-zts-20151012/memcached.so"
	重启Php:
	service php-fpm restart 
6. 使用memcached
	创建新对象：new Memecached 
	添加服务器：addService
	添加键值对：set
	根据键值对获取值：get
	删除键值对：delete
	增加指定数值：increment
	减去指定数值：decrement
	清空所有缓存：flush
7. 设置session使用memecached保存
	vi /usr/local/php7/etc/php.ini
	session.save_handler = memecached
	session.save_path = "127.0.0.1:11211"