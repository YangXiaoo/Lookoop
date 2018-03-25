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





