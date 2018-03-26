--视图(view)
--date(2018-3-25)
视图：一种有结构(有行有列)但没有结果(结构中不真实存放数据)的“虚拟表”，虚拟表的
	  结构来源不是自己定义，而是对应的基表中产生(视图的数据来源)。视图不保存，
	  但能够提取数据。
创建视图：
	基本语法：
		create view 视图名 as select 语句；
		--select 语句可以是普通查询，可以是联合查询，可以使子查询；

	创建单标视图
	create view my_v1 as 
	select * from student;

	create view my_v2 as 
	select * from class;

	create view my_v3 as 
	select s.*,c.name,c.room from student 
	as s left join class as c 
	on s.c_id = c.id;

查看视图：查看结构
视图是虚拟表，不影响基表存在。地基与房屋的关系
表的所有方式都适用于视图:
	show tables[like];  
	desc tables;
视图与表有一个关键区别view，查看表(view)可以使用关键字
--查看视图创建语句
show create view my_v3\G #列变行
视图一旦创建，系统会在对应的数据库文件创建一个 .frm 结构文件

==========使用视图
使用视图主要用于查询，将视图当做表一样查询
--视图使用
select * from my_v1;
视图的执行本质就是执行封装的select语句

==========修改视图
视图本身不可以修改，但视图来源可以修改，修改视图本身来源语句(select语句)
--修改视图
alter view my_v1 as 
select id,name,age,sex,height,c_id from student;

==========删除视图
drop view 视图名称;

==========视图的意义
1.	视图可以节省SQL语句，将一条复杂的查询语句使用视图进行保存，以后可以直接
	对视图操作
2.	数据安全：视图操作主要针对查询，如果对视图结构进行处理(删除)，不会影响基表
	数据(相对安全)。 
3. 	视图往往是在大项目，而且是在多系统使用，可以对外提供有用的数据，并且隐藏
	关键(无用)的数据，数据安全。--隐藏某些数据防止别人看到
4.	视图可以对外提供友好型：不同的视图提供不同的数据，对外专门设计
5. 	视图更好的(更容易)的进行权限控制，对外隐藏表名

==========视图数据操作
视图可以进行数据操作，但限制多
新增数据(单表基图)：
	1.多表数据不能插入数据
	2.可以向单表视图插入数据，视图中包含的字段必须有基表中所有不能为
	空(或者默认字段)，插入顺序按照基表顺序插入
	3.视图可以向基表插入数据
	4.对视图的操作同步到基表
删除数据：
	多表视图不能删除数据。
更新数据：
	1.理论上无论单表视图还是多表视图都可以更新。
	--多表视图更新数据
	update my_v3 set c_id = 3 where id = 5;
	2.更新限制:with check option，如果对视图在新增的时候，某个字段有限制，
	更新数据时，系统会进行验证：保证更新后数据依然可以被视图查询，否则不允
	许更新。
	--age 字段限制
	create view my_v4 as 
	select * form student where age > 30 with check option;
	--表示视图的数据来源有限制
	--with check option表示更新视图的时候，不能将限制的数据修改为超出限制
==========视图算法
--获取班级中最高的一个学生(前面用的是表子查询)
--以下不能排列成功
create  view my_v5 as 
select * from student order by height desc;
select * from my_v5 group by c_id;
--类似于select * from student group by height desc;
视图算法：系统对视图以及外部查询视图的select语句的一种解析方式
视图算法分为三种：
	undefine:未定义(默认)，不是实际算法，告诉系统未定义算法，由系统决定
	temptable:临时表算法，系统应该先执行视图的select语句，后执行查询算法
	merge:合并算法，系统应该现将视图对应的select语句与外部查询视图的select
		语句进行合并，然后执行(高效，常态)，一般未定义时选取此算法
show create view 视图名;--查看结构 
算法指定：
--以下排序可以成功
create algorithm=temptable view my_v6 as
select *from student order by height desc;
select * from my_v6 group by c_id;

视图算法选择：如果视图的select语句中会包含一个查询字句(五子句)，而且很有可能
	顺序比外部的查询语句要靠后，一定要使用算法temotable，其它情况可以不用指定
	(使用默认值)。
