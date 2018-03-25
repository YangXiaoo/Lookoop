#date(2018-3-25)
alter table yangxiao drop primary key;#删除键
alter table yangxiao add id int primary key nut null;#添加key
========================蠕虫===========================
蠕虫复制：从已有的数据中获取数据将数据又进行新增操作，会使数据成倍增加。
		  可以从其他表复制，可以复制自身表。
表创建的高级操作：从已有表创建新表(复制表结构)
--复制表
create table yangxiao2 like yangxiao0;	#只复制结构，不复制数据
--蠕虫复制
操作：先查出数据，再将查出的数据新增一遍。复制的时候成倍增加！！
insert into 表名[(字段列表)] select 字段列表|* from 数据表名
--实列
insert into yangxiao2 select * from yangxiao0;
意义：	1.从已有表拷贝数据到新表中
		2.可以迅速的让表中的数据膨胀到一定的数量级，测试表的压力及效率



==========================更新数据====================
高级：
update 表名 set 字段 = 值[where条件][limit 更新数量];
charset gbk 不区分大小写


=========================查询数据=====================
完整语法：
select[select选项] 字段列表[字段别名]|* from 数据源 
	[where条件句子][group by 字句] [having 字句][order by 字句][limit 字句];
select选项:	对查出来的结果的处理方式
			ALL：全部(默认)
			distinct:去重,对整个字段进行去重
--example:
select * from yangxiao0;
select all * from yangxiao0;
select distinct * from yangxiao0;
============字段别名
定义：当数据进行查询出来的时候，有时候字名并不一定满足要求(多表查询时会有别名)
--语法
select 字段名 as xx 
============数据源(from)
数据源分为多种：单表数据源，多表数据源，查询语句
--单表
select * from 表名;
--多表
select * from yangxiao0,yangxiao1,yangxiao2;
定义：从一张表中取出一条记录，去另一张表中匹配所有记录，而且全部保留，
将这种结果称为：笛卡尔积(交叉连接)。但用处不大，尽量避免。
--查询语句:数据的来源是二维数据
select * form (select * from 表名) as xx;
===========group by
分组，将某个字段进行分组
--根据性别分组
select * from yangxiao1 group by sex;
分组的意义：为了统计数据，按组统计，按分组字段进行数据统计
SQL提供一系列统计函数(搭配group by 使用)：
	count():统计分组后的记录数，每组有多少数据
	max():最大 
	min():最小 
	avg():平均
	sum();总和
--身高高矮，年龄平均和总年龄
select sex,count(*),max(height),min(height),avg(height),sum(height) group by sex [asc/desc];
count()函数：里面可以使用两种参数，*代表统计记录，字段名代表统计对应的字段
			(null不统计)
分组会自动排序：根据字段升序排序
--多字段排序
select sex,name,count(*) from yangxiao group by sex,name desc;
对分组的结果中某个字段进行字符串连接(保留所有的某个字段)
group_contact(字段);
--回溯统计 with rollup:
						任何一个分组后都会有一个小组，最后都要向上级分组进行
						汇报统计：根据当前分组的字段
--实例
select id,count(*) from yangxiao group by id with rollup;
#多一条数据汇报count(*)总和
select id,sex,count(*) from yangxiao group by id,sex with rollup;
#回溯sex回溯，id 回溯
===============Having字句
与where字句一样，进行条件判断
where是针对磁盘数据进行判断，进入内存后，会进行分组操作，分组结果较高就
需要having来处理。
能力：having > where 
1.分组统计的结果和函数的处理只有having能用
--求出所有班级人数大于2的学生人数
select id,count(*) as total from yangxiao group by id having count(*) >=2;
2.having能够使用字段别名，而where从磁盘里取出，只能是字段名不能使用别名。
==================order by 
排序：让数据有顺序，排序所有数据;group by是分组统计，统计第一条数据
排序可以进行多字段排序：先根据某个字段进行排序，然后排序好的内部，再按照
						某个数据进行再次排序(对上一结果进行排序)；
--多字段排序
select * from yangxiao order by id,sex desc;#班级升序，sex降序
===============limit
1.限制长度
select * from yangxiao limit 2;
2.限制起始位置，限制长度
select * from yangxiao limit 0,2;#从0开始编号，记录两个
select * from yangxiao limit 3,2;
实现数据的分页。
