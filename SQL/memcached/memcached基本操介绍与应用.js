//date(2018-4-4)
NoSQL:not only sql
memcached和redis都是key-value存储
mongadb：文档为单位来存储；
{
	title:'写文章',
	content:'啊啊啊'
}

安装：
[root]# cd /usr/local/src/
[root]# wget http://www.memcached.org/files/memcached-1.5.7.tar.gz #官网获得的下载链接
[root]# tar -zxvf memcached-1.5.7.tar.gz #解压
[root]# cd memcached-1.5.7 #进入目录 
[root]# ./configure --prefix=/usr/locl/memcached  #配置
[root]# make & make install  #预编译并安装

开启： 
#-m 内存分配, -p 端口 ,-vv 打印调试信息, -c 最大链接数
[root]# /usr/local/memcached/bin/memcached -m 64 -p 11211 -u root -vv #临时使用

连接：
memcached 客户端与服务器端的通信比较简单,使用的基于文本的协议,而不是二进制协议.
(http 协议也是这样), 因此我们通过 telnet 即可与 memcached 作交互。
#另开一个界面运行以下指令，并且之前开启的会话不要关闭
[root]# telnet localhost 11211 #此处填自己服务器ip地址没有用，因为本来就是在同一台服务器上运行
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
#显示上面结果则表示连接成功



memcached操作命令：
add 语法: add key flag expire length 回车 
	key 给值起一个独特的名字
	flag 标志,要求为一个正整数。1 就是字符串, 2 反转成数组 3,反序列化对象
	expire 有效期。设置缓存的有效期,有 3 种格式
				1:设置秒数, 从设定开始数,第 n 秒后失效.当秒数大于30天时系统理解为绝对时间戳
				2:时间戳, 到指定的时间戳后失效.
				比如在团购网站,缓存的某团到中午 12:00 失效. add key 0 1379209999 6
				3: 设为 0. 不自动失效.
	length 缓存的长度(字节为单位)
实例
add name 0 0 5 #添加记录
what #值
STORED #表示存储成功
get name #获得name
VALUE name 0 5 #得到的结果
what  #结果
END #结束标识符

* delete 语法：delete key [time seconds]
	删除指定的 key. 如加可选参数 time,则指删除 key,并在删除 key 后的 time 秒内,不允许
	get,add,replace 操作此 key.

* replace 语法：replace key flag expire length
	参数和 add 完全一样,不单独写

* get 语法：get key
	返回 key 的值 

* set：用法与add,replace一样，功能如下
	如果服务器无此键 ---> 增加的效果
	如果服务器有此键 ---> 修改的效果

*  incr ,decr 命令:增加/减少值的大小
	语法: incr/decr key num
	注意:incr,decr 操作是把值理解为 32 位无符号来+-操作的. 值在[0-2^32-1]范围内，最小为零

应用：秒杀功能，拆分业务，利用memecacehd存储库存数量，生成订单号，两小时之内执行。







php扩展安装：
[root]# wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
#下载依赖包
[root]# tar -zxvf libmemcached-1.0.18.tar.gz #解压
[root]# cd libmemcached-1.0.18
[root]# ./configure --prefix=/usr/local/libmemcached --with-memcached #配置
[root]# make & make install #编译安装

[root]# wget http://pecl.php.net/get/memcached-3.0.4.tgz #memcached扩展包
[root]# tar -zxvf memcached-3.0.4.tgz #解压
[root]# cd memcached-3.0.4 #进入目录
[root]# ./configure --with-php-config=/usr/local/php/bin/php-config --with-libmemcached-dir=/usr/local/libmemcached --disable-memcached-sasl #安装配置
[root]# make & make install #预编译并安装，复制末行结果如下
Installing shared extensions:     /usr/local/php/lib/php/extensions/no-debug-non-zts-20151012/
[root]# vim /usr/local/php/etc/php.ini #末尾添加如下信息
[Memcache]
extension_dir = "/usr/local/php/lib/php/extensions/no-debug-non-zts-20151012/" 
extension = memcached.so

[root]# nginx -s reload #服务器重启
[root]# killall php-fpm  #关闭Php 另一种方法:pkill -9 php 
[root]# /usr/local/php/sbin/php-fpm #启动php
[root]# /usr/local/php/bin/php -m | grep memcache #查看是否扩展

查看mysql连接信息：
mysql> show processlist;
mysql> stats;
mysql> show status like '%connect%';



