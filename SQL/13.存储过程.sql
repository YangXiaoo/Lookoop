#date(2018-3-27)
#存储过程
定义：procedure,是一种处理数据的方式，存储过程是一种没有返回值得函数。

==========创建过程
create procedure 过程名字([参数列表])
begin 
	--过程体
end 

--创建过程
delimiter &&
create procedure pro1() --假设过程中需要显示数据
select * from my_goods;

==========查看过程
show procedure status\G | status[like 'pattern'];
--查看过程
show procedure status like 'pro%'\G
--查看函数
 show create procedure pro1\G

 ==========调用过程
 过程没有返回值，所以不能用select访问

 过程有专门的调用关键词：call
 --调用
 call pro1;
 ==========修改过程&删除过程
 只能删除
 drop procedure pro1;

 ==========过程参数==========
 函数的参数需要数据类型指定，过程比函数更严格。
 过程有自己的类型限定，三种：
 in: 数据只是从外部传入内部使用,可以是数值可以是变量
 out: 只允许过程内部使用(不用外部数据)，给外部使用。进入内部前，外部数据必须先清空，
 必须是变量。
 inout: 外部可以在内部使用，内部修改可以给外部使用,典型的应用传递，只能传递变量。

基本使用：
create procedure 过程名(in 参数名 数据类型,out 形参名称 数据类型,inout 形参名称 数据类型)

--过程参数
delimiter $$
create procedure pro1(in int_1 int,out int_2 int,inout int_3 int)
begin 
	select int_1,int_2,int_3;--int_2一定为null
end
$$
delimiter ;

==========调用
inout和out必须是变量,内部修改会影响外部数据

--设置变量
set @int_1 = 1;
set @int_2 = 2;
set @int_3 = 3;
select @int_1,@int_2,@int_3;
call pro1(@int_1,@int_2,@int_3);
select @int_1,@int_2,@int_3;


===存储过程对变量的操作(返回)是滞后的，是在存储过程调用结束才会将内部
参数传递给外部。
--查看局部变量与全局变量关系
delimiter $$
create procedure pro2(in int_1 int,out int_2 int,inout int_3 int)
begin 
	select int_1,int_2,int_3;
	set int_1 = 10;
	set int_2 = 20;
	set int_3 = 30;
	select int_1,int_2,int_3;
	select @int_1,@int_2,@int_3; 
	set @int_1 = 'a';
	set @int_2 = 'b';
	set @int_3 = 'd';
	select @int_1,@int_2,@int_3; 
end
$$
delimiter ;

----------------------------------------------------
mysql> call pro2(@int_1,@int_2,@int_3);
+-------+-------+-------+
| int_1 | int_2 | int_3 |
+-------+-------+-------+
|     1 |  NULL |     3 |
+-------+-------+-------+
1 row in set (0.00 sec)

+-------+-------+-------+
| int_1 | int_2 | int_3 |
+-------+-------+-------+
|    10 |    20 |    30 |
+-------+-------+-------+
1 row in set (0.00 sec)

+--------+--------+--------+
| @int_1 | @int_2 | @int_3 |
+--------+--------+--------+
|      1 |      2 |      3 |
+--------+--------+--------+
1 row in set (0.00 sec)

+--------+--------+--------+
| @int_1 | @int_2 | @int_3 |
+--------+--------+--------+
| a      | b      | d      |
+--------+--------+--------+
---------------------------------------------------------------
mysql> select @int_1,@int_2,@int_3; 
+--------+--------+--------+
| @int_1 | @int_2 | @int_3 |
+--------+--------+--------+
| a      |     20 |     30 |
+--------+--------+--------+

以上结果显示：	in不会修改，但Out inout类型会将过程内部对应局部变量的值
			 	重新返回给对应的传入全局变量。