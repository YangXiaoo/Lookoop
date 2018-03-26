#联合查询
#date(2018-3-25)
联合查询：讲多次查询(多条select语句)，在记录上进行拼接(字段不会增加)

基本语法：
	多条select语句构成：每一条select语句获取的字段数必须严格一
	致(但是字段类型无关)。

	select 语句1
	union [union选项]
	select 语句2...

	union 选项：与select选项一样有两个
		ALL:保留所有字段
		distinct：去除重复，默认
--联合查询
select * from yangxiao
union all--不去重
select * from yangxiao;
只要求字段数相同，不要求数据相同

===========意义===================================
1. 查询同一张表，但需求不同，如查询学生信息，男生身高升序，女生升高降序
--男生升序女生降序!!!!!!!!!!!!!!!!!!!!以下错误操作
select * from student where sex = '男' order by age asc 
union
select * from student where sex = '女' order by age desc; 
----正确
联合查询order by 必须要搭配limit
(select * from student where sex = '男' order by age asc limit 999999)
union
(select * from student where sex = '女' order by age desc limit 999999);
2. 多表查询：多张表的结构是完全一样的，保存的数据(结构)也是一样的
			qq号根据自身特性分表

===========子查询  sub query=====================================
定义：某一查询结果之上进行的(一条select语句内部包含另一个select语句)
两种方式：按位置分类，按结果分类
	按位置分类：子查询(select语句)在外部查询(select语句)中出现的位置
		from 子查询：子查询跟在from之后
		where子查询：子查询出现在where之后
		exists 子查询： 子查询出现在exists里面

	按结果分类：根据子查询得到的数据进行分类(理论上任何一个查询得到
		的结果都可以理解为二维表)
--------------------------------------------------------------
		1.标量子查询：子查询得到的结果是一行一列的(字符串)
			需求：知道班级名字xx想获取该班的所有学生
			->确定数据源，获取所有学生
			select * from student c_id=?;
			->获取班级ID，可以通过班级名确定
			select id from class where c_name='xx';#id一定只有一个值
			--结合：
		select * from student c_id=(select id from class where c_name='xx')

-----------------------------------------------------------------
		2.列子查询： 子查询得到的结果是一列多行.(集合)
			需求：查询所在读班级的学生(班级表中存在的班级)
			->确定数据源：学生
			select * from student where c_id in(?);
			->确定有效班级的Id：所有班级id
			select id from class;
			--结合
			select * from student where c_id in(select id from class);
		使用in作为条件匹配，mysql中还有其它类似条件：all,some,any
	select * from student where c_id =some(select id from class);#v
	select * from student where c_id =any(select id from class);#v
	select * from student where c_id =all(select id from class);#x
	select * from student where c_id !=some(select id from class);#所有结果(null除外，不参与搜索)
	select * from student where c_id !=any(select id from class);#所有结果(null除外，不参与搜索)
	select * from student where c_id !=all(select id from class);#x
-----------------------------------------------------------------------

		3.行子查询 ： 子查询得到的结果是多列一行(多行多列)(一行)
		需求：要求查询整个学生中，年龄最大且身高最高的学生???
		->确定数据源 
		select * from student having age =? and height=?;
		->确定最大的年龄和最高身高
		select max(age),max(height) form student;
		--行子查询
		select * from student where
			(age,height) = (select max(age),max(height) from student);
		--以下只能出现一条数据
		select * from student order by age desc,height desc limit 2;


		----上面几个出现的位置都是where之后

-----------------------------------------------------------------------
		4.表子查询： 子查询的结果是多行多列(出现的位置是from之后)
		子查询的结果是多行多列的二维表：子查询返回的结果当做二维表使用
		需求：找出每一个班最高的学生
		->确定数据源 ：先将学生按身高进行降序排序
		select * from student order by height desc;
		->从每个班选出第一个学生
		select * from student group by c_id;#每个班选出第一个学生
		表子查询：from 子查询：得到的结果作为from的数据源

		select * from  (select * from student order by height desc) as student group by c_id ;
------------------------- -----------------------------
		form之后必须跟表名
		什么时候用子查询而不要纠结于用了什么子查询
-------------------------------------------------------
					exists子查询
exists子查询就是用来判断某些条件是否满足(跨表),exists是接在where之后，
exists返回的结果只有0和1。
需求：查询所有的学生：前提条件是班级存在
->确定数据源
select * from student where?;
->确定条件是否满足
exists(select * from class where id = x);
->合并
select *  from student where exists(select * from class where id = x);

