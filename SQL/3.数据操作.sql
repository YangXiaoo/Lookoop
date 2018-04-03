#date(2018-3-25)
<code>alter table yangxiao drop primary key;#删除键</code>
<code>alter table yangxiao add id int primary key nut null;#添加key</code>
<span class="label label-danger">蠕虫</span>
蠕虫复制：从已有的数据中获取数据将数据又进行新增操作，会使数据成倍增加。
		  可以从其他表复制，可以复制自身表。
表创建的高级操作：从已有表创建新表(复制表结构)

--复制表
<code>create table yangxiao2 like yangxiao0;</code>	#只复制结构，不复制数据

--蠕虫复制
操作：先查出数据，再将查出的数据新增一遍。复制的时候成倍增加！！
<code>insert into 表名[(字段列表)] select 字段列表|* from 数据表名</code>
--实列
<code>insert into yangxiao2 select * from yangxiao0;</code>
意义：	1.从已有表拷贝数据到新表中
		2.可以迅速的让表中的数据膨胀到一定的数量级，测试表的压力及效率
<span class="label label-default">更新数据</span>
高级：
<code>update 表名 set 字段 = 值[where条件][limit 更新数量];</code>
charset gbk 不区分大小写


<span class="label label-danger">查询数据</span>
完整语法：
<code>select[select选项] 字段列表[字段别名]|* from 数据源 [where条件句子][group by 字句] [having 字句][order by 字句][limit 字句];</code>
select选项:	对查出来的结果的处理方式
			ALL：全部(默认)
			distinct:去重,对整个字段进行去重

--example:
<pre class="brush:js;">
select * from yangxiao0;
select all * from yangxiao0;
select distinct * from yangxiao0;
</pre>
<span class="label label-default">字段别名</span>
定义：当数据进行查询出来的时候，有时候字名并不一定满足要求(多表查询时会有别名)
--语法
<code>select 字段名 as xx </code>
<span class="label label-default">数据源(from)</span>
数据源分为多种：单表数据源，多表数据源，查询语句
--单表
<code>select * from 表名;</code>
--多表
<code>select * from yangxiao0,yangxiao1,yangxiao2;</code>
定义：从一张表中取出一条记录，去另一张表中匹配所有记录，而且全部保留，将这种结果称为：笛卡尔积(交叉连接)。但用处不大，尽量避免。
--查询语句:数据的来源是二维数据
<code>select * form (select * from 表名) as xx;</code>

<span class="label label-default">group by</span>
分组，将某个字段进行分组
--根据性别分组
<code>select * from student group by sex;</code>
分组的意义：为了统计数据，按组统计，按分组字段进行数据统计SQL提供一系列统计函数(搭配group by 使用)：
	count():统计分组后的记录数，每组有多少数据
	max():最大 
	min():最小 
	avg():平均
	sum();总和
--身高高矮，年龄平均和总年龄
<code>select sex,count(*),max(height),min(height),avg(height),sum(height) from student group by sex [asc/desc];</code>
count()函数：里面可以使用两种参数，*代表统计记录，字段名代表统计对应的字段
			(null不统计)
分组会自动排序：根据字段升序排序
--多字段排序
<code>select sex,name,count(*) from yangxiao group by sex,name desc;</code>
对分组的结果中某个字段进行字符串连接(保留所有的某个字段)
group_contact(字段);
--回溯统计 with rollup:
	任何一个分组后都会有一个小组，最后都要向上级分组进行
	汇报统计：根据当前分组的字段
--实例
<code>select id,count(*) from yangxiao group by id with rollup;</code>
#多一条数据汇报count(*)总和
<code>select id,sex,count(*) from yangxiao group by id,sex with rollup;</code>
#回溯sex回溯，id 回溯
#
<span class="label label-default">Having字句</span>
与where字句一样，进行条件判断。where是针对磁盘数据进行判断，进入内存后，会进行分组操作，分组结果较高就需要having来处理。
能力：having > where 
1.分组统计的结果和函数的处理只有having能用
--求出所有班级人数大于2的学生人数
<code>select id,count(*) as total from class group by id having count(*) >=2;</code>
2.having能够使用字段别名，而where从磁盘里取出，只能是字段名不能使用别名。

<span class="label label-default">order by </span>
排序：让数据有顺序，排序所有数据;group by是分组统计，统计第一条数据排序可以进行多字段排序：先根据某个字段进行排序，然后排序好的内部，再按照某个数据进行再次排序(对上一结果进行排序)；
--多字段排序
<code>select * from class order by id,sex desc;#班级升序，sex降序</code>

<span class="label label-default">limit</span>
1.限制长度
<code>select * from yangxiao limit 2;</code>
2.限制起始位置，限制长度
<code>select * from yangxiao limit 0,2;#从0开始编号，记录两个</code>
<code>select * from yangxiao limit 3,2;</code>
实现数据的分页。




















#date(2018-3-25)<br />
<code>alter table yangxiao drop primary key;#删除键</code><br>
<code>alter table yangxiao add id int primary key nut null;#添加key</code><br>
<span class="label label-danger">蠕虫</span>&nbsp;<br>
	蠕虫复制：从已有的数据中获取数据将数据又进行新增操作，会使数据成倍增加。可以从其他表复制，可以复制自身表。
表创建的高级操作：从已有表创建新表(复制表结构)<br />
<br />
--复制表<br />
<code>create table yangxiao2 like yangxiao0;#只复制结构，不复制数据</code> <br />
--蠕虫复制<br />
操作：先查出数据，再将查出的数据新增一遍。复制的时候成倍增加！！<br />
<code>insert into 表名[(字段列表)] select 字段列表|* from 数据表名</code>
<br>--实列<br />
<code>insert into yangxiao2 select * from yangxiao0;</code><br>
意义：<br>
1.从已有表拷贝数据到新表中<br />
2.可以迅速的让表中的数据膨胀到一定的数量级，测试表的压力及效率<br />
<span class="label label-default">更新数据</span>
<br> 高级：<br />
<code>update 表名 set 字段 = 值[where条件][limit 更新数量];</code><br />
charset gbk 不区分大小写<br />
<br />
<span class="label label-danger">查询数据</span><br>
 完整语法：<br />
	<code>select[select选项] 字段列表[字段别名]|* from 数据源 [where条件句子][group by 字句] [having 字句][order by 字句][limit 字句];</code>
<br>select选项:<span> </span>对查出来的结果的处理方式<br>
ALL：全部(默认)<br />
distinct:去重,对整个字段进行去重<br />
<br />
--example:<br />
<pre class="brush:js;">select * from yangxiao0;
select all * from yangxiao0;
select distinct * from yangxiao0;
</pre>
<span class="label label-default">字段别名</span> <br>
定义：当数据进行查询出来的时候，有时候字名并不一定满足要求(多表查询时会有别名)<br />
--语法<br />
<code>select 字段名 as xx;</code><br>
<span class="label label-default">数据源(from)</span> <br>
数据源分为多种：单表数据源，多表数据源，查询语句<br />
--单表<br />
<code>select * from 表名;--多表</code><br />
	<code>select * from yangxiao0,yangxiao1,yangxiao2;</code><br>
	定义：从一张表中取出一条记录，去另一张表中匹配所有记录，而且全部保留，将这种结果称为：笛卡尔积(交叉连接)。但用处不大，尽量避免。
<br>--查询语句:数据的来源是二维数据<br />
	<code>select * form (select * from 表名) as xx;</code>
<br>
	<span class="label label-default">group by</span> 分组，将某个字段进行分组
<br>
--根据性别分组<br />

	<code>select * from student group by sex;</code>

<p>
	分组的意义：为了统计数据，按组统计，按分组字段进行数据统计SQL提供一系列统计函数(搭配group by 使用)：
</p>
<code>count()</code>:统计分组后的记录数，每组有多少数据<br />
<code>max()</code>:最大&nbsp;<br />
<code>min()</code>:最小&nbsp;<br />
<code>avg()</code>:平均<br />
<code>sum()</code>;总和<br />
--身高高矮，年龄平均和总年龄<br />
<code>select sex,count(*),max(height),
min(height),avg(height),sum(height)
 from student group by sex [asc/desc];</code>

<p>
	count()函数：里面可以使用两种参数，*代表统计记录，字段名代表统计对应的字段
</p>
<span> </span>(null不统计)<br />
分组会自动排序：根据字段升序排序<br />
--多字段排序<br />

	<code>select sex,name,count(*) from yangxiao group by sex,name desc;</code>

<p>
	对分组的结果中某个字段进行字符串连接(保留所有的某个字段)
</p>
group_contact(字段);<br />
--回溯统计 with rollup:<br />
<span> </span>任何一个分组后都会有一个小组，最后都要向上级分组进行<br />
<span> </span>汇报统计：根据当前分组的字段<br />
--实例<br />
<code>select id,count(*) from yangxiao group by id with rollup;#多一条数据汇报count(*)总和</code><br />
<code>select id,sex,count(*) from yangxiao group by id,sex with rollup;#回溯sex回溯，id 回溯</code><br />

<span class="label label-default">Having字句</span> 与where字句一样，进行条件判断。where是针对磁盘数据进行判断，进入内存后，会进行分组操作，分组结果较高就需要having来处理。<br />
能力：having &gt; where&nbsp;<br />
1.分组统计的结果和函数的处理只有having能用<br />
--求出所有班级人数大于2的学生人数<br />

	<code>select id,count(*) as total from class group by id having count(*) &gt;=2;</code>

<br>
	2.having能够使用字段别名，而where从磁盘里取出，只能是字段名不能使用别名。<br>


	<span class="label label-default">order by </span> 排序：让数据有顺序，排序所有数据;

<p>
	group by是分组统计，统计第一条数据排序可以进行多字段排序：先根据某个字段进行排序，然后排序好的内部，再按照某个数据进行再次排序(对上一结果进行排序)；
</p>
--多字段排序<br />
<code>select * from class order by id,sex desc;#班级升序，sex降序</code><br />
<span class="label label-default">limit</span> <br>
1.限制长度<br />
	<code>select * from yangxiao limit 2;</code><br>
	2.限制起始位置，限制长度<br>
	<code>select * from yangxiao limit 0,2;#从0开始编号，记录两个</code>
<br>
	<code>select * from yangxiao limit 3,2;</code><br>实现数据的分页。
