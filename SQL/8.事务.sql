#date(2018-3-26)
#事务(前提是innodb引擎)
定义：一系列要发生的连续操作，为了保证数据的完整性。针对数据操作，不针对表结构操作。

--创建表
create table count (
number char(16) not null unique comment '账户',
name varchar(20) not null,
money decimal(10,2) default 0.0 comment '账户余额'
)charset utf8;
--插入数据
insert into count values ('11111','张三',1000),('11123','李四',2000);

alter table count add id int primary key auto_increment first;

事务操作：自动操作(默认),手动事务
===========手动操作==========================================================
1.	开启事务：告诉系统以下所有操作不要直接写入数据表中,先存放到事务日志
start transaction;--开启事务
2.	进行事务操作：一系列操作
	a)李四账户减少
	b)张三账户增加少
uptade count set money = money - 1000 where id = 2; --李四钱减少
uptade count set money = money + 1000 where id = 1;--张三钱增加
3.	结束事务，选择性地将日志文件中操作的结果保存到数据表(同步)或者说直接清空
	事务日志。
	a)提交事务：同步数据表
commit;--提交事务
	b)回滚事务：操作失败
rollback;--回滚事务

=====事务原理
事务开启后，所有的操作都会临时保存到事务日志中，事务日志只有在得到commit命令
才会同步到数据表，其它任何情况都会清空。

=====回滚点
在某一个成功的操作完成后，后续成功不管成功还是失败：可以在当前成功的位置设置
一个点，已提供后续操作失败返回到前一个操作成功的位置，该点成为回滚点。

设置回滚点：savepoint 回滚点名称
回到回滚点： rollback to 回滚点名称 
--回滚点操作
start transaction;
uptade count set money = money + 1000 where id = 2; --李四发工资
--设置回滚点
savepoint sp1;
uptade count set money = money - 1000*0.05 where id = 1;--扣税
--回滚
rollback to sp1;
commit;

==========自动事务==========================================================
mysql默认为自动事务处理，用户操作完后会立即同步到数据表中

自动事务：系统通过autocommit
show variable `autocommit`;--查看自动提交状态
关闭自动事务：
set autocommit = 0;

再次直接写操作：
uptade count set money = money + 1000 where id = 1; --张三发工资

此时不会自动同步到数据表中，需要手动选择处理，commit或rollback to 处理

set autocommit = 1;
show variable autocommit;

==========================================================================
事务特性：ACID
A：Atomic 原子性
C：Consistency 一致性，事务操作前后数据表中的数据没有变化，数据表中的日志不会对表进行操作
I: Isolation 隔离性，相互操作不受影响。开启多个事务对同一表进行操作，之间不受影响
D：Durability 持久性，数据一旦提交不可改变

锁机制：innodb默认为行锁，但如果在事务操作中没有使用索引(primary key)，系统会全表
检索数据，系统会自动升级为表锁。
	行锁：只有当前行，其余用于不能操作
	表锁：一张表，其余用户不能操作,没有使用索引，用的为字段
start transaction;
update count set money = money +1000 where name ='张三';
--此时表count被锁住,其余用户不能进行操作
