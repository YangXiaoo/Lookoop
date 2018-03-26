#date(2018-3-26)
#系统变量
定义：系统定义好的变量，大部分时用户不需要使用系统变量，系统变量用来控制服务器的表现
如：autocommit,auto_increment

查看系统变量：
show variables;--查看所有系统变量
show warnings;--查看错误报警

select @@version,@@autocommit,@@auto_increment_offset,@@character_set_results;
+------------+--------------+-------------------------+-------------------------+
| @@version  | @@autocommit | @@auto_increment_offset | @@character_set_results |
+------------+--------------+-------------------------+-------------------------+
| 5.7.18-log |            1 |                       1 | utf8                    |
+------------+--------------+-------------------------+-------------------------+

--修改会话级别变量：
set autocommit = 1;--只会对当前操作有影响

--全局修改：
set @@变量名 = 值;
set globle 变量名 = 值;

set gloab autocommit = 1;

全局修改退出mysql客户端后才能生效。

===================自定义变量===============
系统为了区分系统变量，规定用户自定义变量必须使用一个@符号。
所有自定义变量只有当前会话会保存。

--定义自定义变量
set @name = '杨潇';
mysql> select @name;
+--------+
| @name  |
+--------+
| 杨潇   |
+--------+

在mysql中，'='会默认为比较符号处理，为区分比较符号和赋值符号，重新定义了赋值符号
赋值：set @age := '23';

mysql允许从数据表中获取数据，然后赋给变量，有两种：
1.边赋值，查看结果
--从表中赋值获取赋值变量
select @name := name,name from student;
2.只有赋值，不看结果，数据记录只允许获取一条，因为mysql不支持数组
select name,age from student where id = 1 into @name,@age;
