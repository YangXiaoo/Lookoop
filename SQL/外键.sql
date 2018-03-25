#date(2018-3-25)
外键：	foreign ，外面的键(键不在自己表中)，如果一张表中有一个字段(非主键)
		指向另一个表的主键，那么称该字段为外键。一张表可以有多个外键。
创建表的时候增加外键：	在所有的表字段之后，用foreign key(外键)
--
create tabel yangxiao3(
	id  int primary key auto_increment,
	name varchar(10) not null ,
	y_id int ,
	--增加外键
	foreign key(y_id) references yangxiao(id)
)charset utf8;
-----------------
创造后有两个键和一个限制
primary key(id)
key(y_id)
constraint `yangxiao3_foreign` foreign key (y_id) references yangxiao(id)
==============增加外键
--增加外键
alter table yangxiao1 add 
--指定外键
constraint y_foreign 
--指定外键字段
foreign key(y_id)
--引用父表主键
references yangxiao(id);
---------------------
desc yangxiao1;结果y_id的可以为MUL
==========删除外键
alter table yangxiao2 drop foreign key (y_foreign);#外键名
--删除外键无法从结构上看出来
==========外键作用
外键默认的作用：	一个父表一个子表(外键字段所在的表)
对子表约束:资表数据进行写操作时，若对应外键字段在父表中找不到对应的匹配，
操作失败。(约束子表数据操作)

若子表与父表有关联，则父表中被引用的键不可以修改。
===========外键存在条件
1.条件：保证表的存储引擎为innoDb,若不是该引擎，外键可以创建成功但没有约束效果。
2.外键字段类型必须与父表主键类型完全一致。
3.一张表中的外键名字不能重复
4.增加的外键的字段(数据已经存在)，必须保证数据与父表的主键要求对应
============外键约束
可以通过对外键的需求进行定制操作
外键约束有3中约束模式(针对父表的约束)：
	district:严格模式(默认)，父表不能删除或更新一个已经被子表数据引用的记录
	cascade:级联模式：父表的操作，对应子表关联的数据也跟着操作
	setnull:置空模式，父表操作后，子表对应的数据(外键字段)被置空
	一般：删除的时候置空，更新的时候级联
--删除置空，更新级联
create table y_foreign1(
id int primary key auto_increment,
name varchar(10) not null,
c_id int,
foreign key(c_id)
references yangxiao(id)
on delete set null
on update cascade
)charset utf8;
删除置空的前提条件，外键子弹允许为空
外键虽然很强大，能够进行各种约束，但对于Php来讲，外键的约束降低了php对数据的
可控性，实际开发中，很少使用外键来处理。
