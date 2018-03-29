#date(2018-3-26)
#函数
#定义：将一段代码封装到一个结构中，在需要执行代码块的时候，调用结构执行即可。
函数分为两类：系统函数和自定义函数
任何函数都有返回值，因此函数的调用是通过select调用
mysql中字符串基本操作单位(最常见的是字符)
==============================================内置函数：(不改变源数据本身)
1.substring：字符串截取(字符为单位)substring(str,position,length)
mysql> set @cn = '世界你好';

mysql> set @en = 'hello world';

mysql> select substring(@cn,1,1);
+--------------------+
| substring(@cn,1,1) |
+--------------------+
| 世                 |
+--------------------+
mysql> select substring(@en,1,1);
+--------------------+
| substring(@en,1,1) |
+--------------------+
| h                  |
+--------------------+

2.select char_length(@cn),char_length(@en),length(@cn),length(@en);
+------------------+------------------+-------------+-------------+
| char_length(@cn) | char_length(@en) | length(@cn) | length(@en) |
+------------------+------------------+-------------+-------------+
|                4 |               11 |          12 |          11 |
+------------------+------------------+-------------+-------------+

3.instr:判断字符串是否在某个具体字符串中存在，存在返回位置

select instr(@cn, '界'),instr(@en,'ll'),instr(@cn,'白边');
+-------------------+-----------------+---------------------+
| instr(@cn, '界')  | instr(@en,'ll') | instr(@cn,'白边')   |
+-------------------+-----------------+---------------------+
|                 2 |               3 |                   0 |
+-------------------+-----------------+---------------------+
0代表没有找到。
4.lpad(str,length,padstr):代表左填充，将字符串按照某个指定的填充方式，填充到指定的长度(字符为单位)
select lpad(@cn,20,'欢迎'),lpad(@en,20,'hi');

5.insert(str,pos,len,newstr),替换，找到目标位置，将目标位置替换
select insert(@en,3,3,'y');
 
6.strcmp:字符串比较
set @f = 'hello';
set @s = 'hey';
set @t = 'HEY';
select strcmp(@f,@s),strcmp(@t,@f),strcmp(@s,@t);
+---------------+---------------+---------------+
| strcmp(@f,@s) | strcmp(@t,@f) | strcmp(@s,@t) |
+---------------+---------------+---------------+
|            -1 |             1 |             0 |
+---------------+---------------+---------------+
结论：不区分大小写


===========================自定义函数================================================
函数要素：函数名，参数列表(形参和实参)，返回值，函数体(作用域)
创建函数：
create funtion 函数名([形参列表])returns 数据类型--规定要返回的数据类型
begin
	--函数体
	--返回值，return规定的烈性(指定数据类型)
end

--创建函数
create function display() returns int
	return 100;
-----------------------------------若出现以下错误--------------------
ERROR 1418 (HY000): This function has none of DETERMINISTIC, NO SQL, or READS SQL DATA in its declaration and binary logging is enabled (you *might* want to use the less safe log_bin_trust_function_creators variable)
==则修改系统变量
mysql> show variables like 'log_bin_trust_function_creators';
+---------------------------------+-------+
| Variable_name                   | Value |
+---------------------------------+-------+
| log_bin_trust_function_creators | OFF   |
+---------------------------------+-------+
mysql> set global log_bin_trust_function_creators=1;
--------------------------ok--------------------------------------

=============查看函数
查看所有函数：
show function status\G 

查看函数创建语句
show create function display\G

==========修改函数(不可以)&删除
drop function 函数名;
--删除
drop function display;


==========函数参数 
两种：定义时的参数叫做形参，调用的时的参数叫实参(实参可以是数值也可以是变量)

--计算1到指定数之间的和

delimiter $$
create function display(int_1 int) returns int 
begin 
	set @i = 1;#@定义的变量时全局变量，在函数外部也可以访问
	set @res = 0;
	while @i <= int_1 do 
	--任何变量修改必须用set
		set @res = @res + @i;
		set @i = @i + 1;
	end while;
	return @res;
end 
$$

delimiter ;
--------------------------------
select diaplay(3);
+-------------+
| display(@i) |
+-------------+
|          10 |
+-------------+
mysql> select @i,@res;
+------+------+
| @i   | @res |
+------+------+
|    4 |    6 |
+------+------+
-----------------------------------
====作用域
Mysql中的作用域与js中的作用域完全一样
全局变量可以在任何地方使用，全局变量只能在函数内部使用

全局变量：set @变量名; 使用@
局部变量：declear 关键字声明; 不使用@，所有局部变量的声明必须在函数体之前

--求和：1-指定数之和，要求5的倍数不能加
delimiter $$
create function display1(int_1 int) returns int 
begin 
	declare i int default 1;
	declare res int default 0;
	mywhile:while i <= int_1 do 
		if i % 5 = 0 then 
			set i = i + 1;
			iterate mywhile;
		end if;
		set res = res + i;
		set i = i + 1;
	end while;

	return res;
end 
$$

delimiter ;
