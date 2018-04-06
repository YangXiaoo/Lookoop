#date(2018-4-6)
redies(Redies Dictionary Server)远程数据服务
key-value:string,list,hash,set,sorted set 

可持久化，保证数据安全。一边运行一边存储到磁盘

redies单个value限制为1GB，memcached为1M。
不仅支持key-value，还支持其它类型
支持主从模式(master-slave)

基本讲解
--------
编辑安装：
[root]# cd /usr/local/src #进入软件包存放路径
[root]# wget http://download.redis.io/releases/redis-4.0.9.tar.gz #下载
[root]# tar -zxvf redis-4.0.9.tar.gz #解压
[root]#  cd redis-4.0.9 #进入目录
[root]# make #编译
[root]# cd src #进入程序目录
[root]# mkdir /usr/local/redis #创建运行目录
[root]# cp redis-cli redis-server /usr/local/redis #复制运行程序
[root]# cd .. #进入上一级目录，复制另一个配置
[root]# cp redis.conf /usr/local/redis #复制配置 
[root]# ./redis-server #启动程序--前端方式，结束ctrl+c

#daemon 进程的意思
[root]# vim redis.conf #设置后台启动。进入配置文件/daemonize搜索配置,修改如下：
136 daemonize yes
[root]# ./redis-server redis.conf #开启进程
[root]# ps -A | grep redis #查看进程

#启动：
[root]# ./redis-cli #出现以下信息则启动成功
127.0.0.1:6379>


操作
-----
1)KEY
key 除了"\n"和空格不能做成名字内容，其它都可以，长度不限制
set key 	#设置key
get key 	#获得key
keys *	 	#匹配所有
exists key  #是否存在
type key 	#返回类型
rename oldkey newkey #重命名
expire key seconds   #设置有效期 
ttl key 			 #key剩余的有效期
select db-index 	 #选择数据库
move key db-index 	 #把key移动到指定标数据库里
[root]# move name 2  #移动到第二个数据库
flushdb 	#删除所有key
fulshall 	#删除所有数据库

[root]# vim /usr/local/redis/redis.conf #搜索databse查看有多少个数据库

2)String 类型
string可以包含任何数据，包括jpg图片或序列化对象，单个value最大上限1G。
如果只用string类型，redis可以看做持久化的memcached

set key value 		#设置key对应的值
mset key1 value1 key2 value2 ... 	#设置多个key
mget key2 key2 ...	#获得多个值
incr key 			#加操作，＋1
decr key 			#减操作，-1
incrby key integet 	#加指定数
decrby key integet 	#减指定
append key value 	#给key字符串追加value
substr key start end 	#返回截取过的key的字符串值，开始位置和结尾位置都包括

3)List 列表
双向链表，通过Push和pop操作从链表的头部或尾部添加删除元素。使得list既可以用于栈操作也可以用于列队操作。
上进上出为栈，上进下出为列
应用场景：
	获得最新登录系统的前10个用户信息。
	select * from user order by logintime desc limit 10;
	对于数据信息数据多的时候，全部数据都会受到影响，对数据库负载高。
	通过list则只会在list链表中保留最新的10个数据。极大节省资源消耗。

lpush key value #key对应的头部添加字符串元素
rpop key #在list的尾部删除元素并返回删除元素
llen key #对应list长度，key不存在返回0，若key对应类型不是list返回错误
lrange key start end #返回指定区间的元素，下表从0开始
rpush key string #在key尾部添加字符串元素
lpop key #list头部删除元素
ltrim ket start end #截取list保留区间内元素

[root]# lpush line a #依次添加b,c,d,e,f共六个
[root]# rpop line #删除a

4)Set 集合
包括union,intersection,difference

sadd key member 			#添加一个string元素key对应的set集合中，成功返回1
srem key member [member] 	#从key对应的set中移除给定元素，成功返回1
smove p1 p2 member 			#从p1对应set中移除member并添加到p2对应set中
scard key 				#返回set元素的个数
sismember key member 	#判断member是否在set中
sinter key1 key2 ... 	#返回所有给定key的交集
sunion key1 key2 ... 	#返回所有给定key的并集
sdiff key1 key2 ...  	#返回所有给定key的差集
smember key 			#返回key对应set的所有元素，结果是无序的

5)Sort set 排序集合类型
和set一样也是string类型的元素集合，但每个元素都会关联一个权值，通过权值可以有序地获取集合中的元素

应用场景：
	获得热门帖子(回复)信息，select * from message order by replynum desc limit 10;
	sql可以获得但消耗数据库资源。

zadd key source member 		#添加元素到集合，元素在集合中存在则更新对应score
zrem key member 			#删除指定元素，1表示成功，元素不存在则返回0
zincrby key incr member 	#按照incr增幅度增加对应member的score值，返回score值
zrank key member 			#返回指定元素下表，集合中元素按score从小到大排序的
zrevrank key member 		#从大到小排序
zrange key start end 		#指定区间元素
zrevrange key start end 	#同上，但结果逆序
zcard key 					#集合中元素的个数
zscore key element 			#返回给定元素对应的score
zremrangebyrank key min max #删除集合中排名在给定区间的元素(权值由小到大排序)

3)hash 类型
hash数据类型结构与mysql差不多

hset key field value 
hget key field 
hmget key field1 field2 ...
hmset key1 value1 key2 value2 ...
hincrby key field integer 
hexists key field 
hdel key field 
hlen key 
hkeys key 
hvals key 
hgetall key 


持久化
-----
将数据以文件形式保存到硬盘，服务器重启后会自动把硬盘的数据恢复到内存中，数据保存到硬盘的过程称为持久化。

1)snap shotting 快照持久化
	该持久化默认开启，一次性把redis中全部数据保存一份存储在硬盘中，如果数据非常多，就不建议。
	dump.rdb为保存的文件。	
	[root]# vim redis.conf 
	save 900 1 #900秒内1个可以发生变化就保存
	save 300 10 #300秒内10个可以发生变化就保存
	save 60 10000 #一分钟内超过10000个key发生变化就保存

	精细持久化(把修改的每个key都保存起来，并且评率可以达到秒级)

2)append only file (AOF持久化)
	本质：把用户执行的每一个写指令(添加，修改，删除)都备份到文件中，还原数据的时候就是执行具体的指令。
	开启AOF持久化会清空redis内部的数据。应该提前开启。
	[root]# vim redis.conf #打开配置进行开启，搜索/aof 
 	672 appendonly yes  #将no改为yes
	673 
 	674 # The name of the append only file (default: "appendonly.aof")
 	675 
 	676 appendfilename "appendonly.aof"
 	[root]# ps -A | grep redis #查看进程，然后用kill -9  进程号 杀死redis进程。最后启动redis

备份频率：
 	701 # appendfsync always #一直都要备份
 	702 appendfsync everysec #每秒同步备份(m默认)
	703 # appendfsync no #机器空闲时处理，容易出现数据缺失

备份文件优化处理：
	[root]# ./redis-cli -gbrewriteaof #例如多个incr指令变为set指令

其余操作指令：
bgsave #异步保存数据到磁盘
lastsave #返回上次成功保存到磁盘的linux时间戳
shutdown #同步保存到服务器并关闭redis服务
bgrewriteaof #优化aof日志文件存储

[root]# ./redis-cli -h 127.0.0.1 -p 6379 bgsave #给其余端口ip快照



主从模式
--------

主服务器写(添加、修改、删除)数据，数据同步给从服务器，从服务器读数据

[root]# vim redis.conf #搜索savleof,修改以下参数，杀死redis进程并重启redis服务器
281 # slaveof <masterip> <masterport>
salveof xxx.xxx.xx.xxx 7379 #填写主服务器的ip，和进程端口号

 301 slave-serve-stale-data yes #从服务器只能读数据



PHP扩展
-------
[root]# cd /usr/local/src 
[root]# wget http://pecl.php.net/get/redis-4.0.0.tgz #http://pecl.php.net/package/redis
[root]# tar -zxvf redis-4.0.0.tgz #解压
[root]# cd redis-4.0.0 #进入目录 
[root]# /usr/local/php/bin/phpize #将redis反安装到php中
[root]# ./configure --with-php-config=/usr/local/php/bin/php-config #配置
[root]# make & make install  #安装，成功后出现以下路径
/usr/local/php/lib/php/extensions/no-debug-non-zts-20151012/ #可以在里查看扩展包

[root]# vim /usr/local/php/etc/php.ini #末尾添加如下信息
extension = redis.so #添加扩展包

[root]# killall php-fpm #关闭Php
[root]# /usr/local/php/sbin/php-fpm #开启php



php操作redis
-----------




