#date(2018-3-26)
#触发器
需求：有两张表，一张订单表，一张商品表，每生成一个订单，意味着商品的库存要减少。
触发器：事先为表绑定一段代码，当表中的某些内容发生改变的时候(增删改)，系统会自动
触发代码执行。

触发器：事件类型，触发时间，触发对象
	事件类型：增删改，三种类型insert,delete,update
	触发时间：前后:before和after
	触发对象：表中的每一条记录

一张表中只能拥有一种触发时间的一种类型的触发器：一张表最多能有6个触发器。


==========创建触发器：
在mysql高级结构中没有大括号，有小括号，都是用对应的字母符号代替
==基本语法
--临时修改语句结束符
delimiter; 自定义符号：后续代码中只有碰到自定义符号才算结束
create trigger 触发器名字 触发时间 事件类型 on 表名 for each row
begin --代表左大括号:{,开始
--触发器内容，每行都必须使用语句结束符：分号
end --代表右大括号：}，结束
--将临时自定义符号修改过来
delimiter;


--创建表
create table my_goods(
id int primary key auto_increment,
name varchar(20) not null,
price decimal(10,2) default 1,
inv int comment '库存'
)charset utf8;

insert into my_goods values(null,'iphone8',8888,100),(null,'iphone7',6666,100);

create table my_order(
id int primary key auto_increment,
g_id int not null comment '商品id',
g_number int comment '商品数量'
)charset utf8;

--触发器
--修改临时符号
delimiter $$ 
create  trigger after_order after insert on my_order for each row
begin 
--触发器开始
	update my_goods set inv = inv - 1 where id = 2;
end
$$
--执行面代码，成功后执行下列代码
delimiter  ;--中间有空格

====查看触发器
show trigger [like 'pattern'];
show triggers;--所有触发器，一下为结果
----------------------------------------------------------------------
             Trigger: after_order
               Event: INSERT
               Table: my_order
           Statement: begin update my_goods set inv = inv - 1 where id = 2;
end
              Timing: AFTER
             Created: 2018-03-26 21:16:10.05
            sql_mode: ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
             Definer: root@localhost
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: utf8mb4_general_ci
----------------------------------------------------------------------
查看触发器创建语句
show create triger after_order;

所有信息存储在information_schema.triggers中
select * from information_schema.triggers\G
--结果如下
----------------------------------------------------------------------
           TRIGGER_CATALOG: def
            TRIGGER_SCHEMA: test
              TRIGGER_NAME: after_order
        EVENT_MANIPULATION: INSERT
      EVENT_OBJECT_CATALOG: def
       EVENT_OBJECT_SCHEMA: test
        EVENT_OBJECT_TABLE: my_order
              ACTION_ORDER: 1
          ACTION_CONDITION: NULL
          ACTION_STATEMENT: begin update my_goods set inv = inv - 1 where id = 2;
end
        ACTION_ORIENTATION: ROW
             ACTION_TIMING: AFTER
ACTION_REFERENCE_OLD_TABLE: NULL
ACTION_REFERENCE_NEW_TABLE: NULL
  ACTION_REFERENCE_OLD_ROW: OLD
  ACTION_REFERENCE_NEW_ROW: NEW
                   CREATED: 2018-03-26 21:16:10.05
                  SQL_MODE: ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
                   DEFINER: root@localhost
      CHARACTER_SET_CLIENT: utf8
      COLLATION_CONNECTION: utf8_general_ci
        DATABASE_COLLATION: utf8mb4_general_ci

----------------------------------------------------------------------

===================触发器使用
上述触发器只会固定修改
insert into my_order values (null,2,1);--插入
mysql> select * from my_goods;
+----+---------+---------+------+
| id | name    | price   | inv  |
+----+---------+---------+------+
|  1 | iphone8 | 8888.00 |  100 |
|  2 | iphone7 | 6666.00 |   99 |
+----+---------+---------+------+

============修改触发器&删除触发器
drop trigger 触发器名字;

============触发器记录
定义：不管触发器是否触发，只要当前某种操作准备执行，系统就会将当前要操作
的记录的状态和即将及执行之后新的状态分别保留下来，触发器使用：其中，要操作
的当前状态保存到old中，操作之后的可能形态保存到new中。
old 代表旧记录，new代表新记录(假设发生的结果)
	删除之后没有new，插入没有old
old和new都是记录本身，任何一条记录除了数据还有字段名称
使用方法：old.字段名 | new.字段名

----重新设计触发器
delimiter $$ 
create  trigger after_order after insert on my_order for each row
begin 
--触发器开始：新增一条订单,old没有，new代表新订单有记录
	update my_goods set inv = inv - new.g_number where id = new.g_id;
end
$$
--执行面代码，成功后执行下列代码
delimiter  ;--中间有空格


删除的话就用old。

