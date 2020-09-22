# 数据类型
# 整数
TINYINT 	-128~127
SMALLINT	-32768 - 32767
MEDIUMINT	-2^23 - 2^23-1
INT			-2^31 - 2^31-1
BIGINT		-2^63 - 2^63-1

# 字符串
CHAR(n)		0 - 255字节		定长字符串
VARCHAR(n)	0 - 65535字节	变长字符串
TEXT		0 - 65535字节	长文本数据
LONGTEXT	0 - 2^32-1字节	极大文本数据
BLOB		0 - 65535字节	二进制长文本数据
LONGBLOB	0 - 2^32-1字节	二进制极大文本数据

效率：CHAR>VARCHAR>TEXT
InnoDB中推荐使用VARCHAR
--
# 小数类型（m 表示浮点数的总长度，n 表示小数点后有效位数）
Float	Float(m,n)		7位有效数
Double	Double(m,n)		15位有效数
Decimal	Decimal(m,n)	28位有效数

# 时间类型
DATE		YYYY-MM-DD			日期
TIME		HH:MM:SS			时间
YEAR		YYYY				年份
DATETIME	YYYY-MM-DD HH:MM:SS	日期和时间
TIMESTAMP	10位或13位整数（秒数）时间戳

--------------------------------基本操作命令--------------------------------
# 创建数据库
create database xx;

# 修改数据库编码
alter database xx character set utf8mb4;

# 显示表信息
show create table xx;

# 显示表
desc table;

# 给表增加字段
alter table xx add new_col CHAR(20);

# 删除表的字段
alter table xx drop new_col;

# 修改字段的数据类型
alter table xx modify new_col VARCHAR(12);

# 修改字段数据类型并且改名
alter table xx change new_col new_col_new_name CHAR(10);

# 修改默认值
alter table article alter column category_id set default 0;

# 创建索引
create table xx (
	`id` char(20) not null,
	`uid` char(20) not null,
	key (`uid`)
)
--------------------------------使用技巧--------------------------------
# 索引优化
-- 列不要计算
-- 最左前缀原则
-- 索引覆盖
-- 少用like
-- 字段尽量不要用NULL
-- 索引使用varchar时，需要用''将字段括起来
-- 主键避免使用varchar
-- 自增ID替换UUID，使用雪花算法

# 唯一索引(UNIQUE  INDEX)和普通索引(INDEX)
-- 一般使用普通索引INDEX

# 索引
-- PRIMARY KEY
-- UNIQUE
-- NOT NULL
-- DEFAULT