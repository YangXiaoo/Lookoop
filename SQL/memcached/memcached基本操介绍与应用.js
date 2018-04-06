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
[root]# /usr/local/memcached/bin/memcached -m 64 -p 11215 -u root & #后台打开
#可以在同一台机器开多个端口，然后不同客户端使用不同内存

连接：
memcached 客户端与服务器端的通信比较简单,使用的基于文本的协议,而不是二进制协议.
(http 协议也是这样), 因此我们通过 telnet 即可与 memcached 作交互。
#另开一个界面运行以下指令，并且之前开启的会话不要关闭
[root]# telnet localhost 11211 #此处填自己服务器ip地址没有用，因为本来就是在同一台服务器上运行
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
#显示上面结果则表示连接成功

[root]# netstat -lp | grep memcached #查看进程


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

==========================经典现象与问题=====================================
(1)雪崩现象：缓存雪崩一般是由某个缓存节点失效,导致其他节点的缓存命中率下降, 缓存中缺失的数据
去数据库查询.短时间内,造成数据库服务器崩溃


(2)multiget-hole ：无底洞现象，数据太分散
解决方案：nosql键的设计

哈希算法根据键自动分配所使用的服务器

mysql的计算为：
表：主键字段：主键值：字段名
my_goods:id:1:name  PKU
计算key->server时根据 主键字段：主键值  来分发
----------------------------------------------------------------------------------
NoSQL 和传统的 RDBMS,并不是水火不容,两者在某些设计上,是可以相互参考的.
对于 memcached, redis 这种 kv 存储, key 的设计,可以参考 MySQL 中表/列的设计.
比如: user 表下,有 age 列,name 列,身高列,
对应的 key,可以用 user:133:age = 23, user:133:name = ‘lisi’, user:133:height = 168;
-----------------------------------------------------------------------------------
nosql:
my_goods:name:iphone7:id , 1
此时根据name查询

此时查询：
select id from my_goods where name=iphone7;
select * from my_goods where id=1;

其意义就是为了让同一组数据分发到同一个服务器，减少客服端对不同服务器多次请求，减压

(3)永久数据被踢现象
1:如果 slab 里的很多 chunk,已经过期,但过期后没有被 get 过, 系统不知他们已经过期.
2:永久数据很久没 get 了,不活跃,如果新增item,则永久数据被踢了.
3: 当然,如果那些非永久数据被 get,也会被标识为 expire,从而不会再踢掉永久数据

解决方法：永久性数据与非永久性数据分离
惰性删除：get后才删除过期的数据
memcache每get一次活跃度加1，使用的是lru机制(least recently used),即使某个key设置永久有效，也一样会被踢出。
其它数据库有fifo(first in, first out),rand。

(4)内存碎片化
memcached 用 slab allocator 机制来管理内存.
slab allocator 原理: 预告把内存划分成数个 slab class 仓库.{每个 slab class 大小 1M}
各仓库,再切分成不同尺寸的小块(chunk). 
需要存内容时,判断内容的大小,为其选取合理的仓库。
在启动memcached的时候就可以看到切出的块：
[root]# /usr/local/memcached/bin/memcached -m 64 -p 11211 -u root -vv
chunk切片增长速度叫做grow factor,使用方法如下：
[root]# /usr/local/memcached/bin/memcached ­f 2 -vv

(5)参数限制
key 的长度: 250 字节, (二进制协议支持 65536 个字节)
value 的限制: 1m, 一般都是存储一些文本,如新闻列表等等,这个值足够了.
内存的限制: 32 位下最大设置到 2g.
如果有 30g 数据要缓存,一般也不会单实例装 30g, (不要把鸡蛋装在一个篮子里),
一般建议 开启多个实例(可以在不同的机器,或同台机器上的不同端口)

(6)分布式缓存