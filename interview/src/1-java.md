> ## Java基础

## java关键字与保留字? goto, const? false, true, null, inner?
goto没有定义, 但自己也不能使用这样的变量名, 使用编译后会报错
关键字与保留字作为变量使用会报错

## String能被继承吗?
不能继承, 使用final修饰

## String底层如何实现? 不可变的好处? 采用什么设计模式? 什么是String Pool?
底层实现: 
- JDK1.8, String内部使用`private final char value[];`
- JDK1.9, String定义时使用`private final byte value[]`有些字母不需要两个字节, 节省空间

不可变的好处: 线程安全, 哈希值存储, 字符串常量池

采用享元设计模式

字符串常量池在JDK1.7时被转移到堆中, 之前在方法区的运行时常量池中.
使用字符串常量池, 每当我们使用字面量(`String s="1";`)创建字符串常量时, JVM会首先检查字符串常量池, 如果该字符串已经存在常量池中, 那么就将此字符串对象的地址赋值给引用s(引用s在Java栈中).如果字符串不存在常量池中, 就会实例化该字符串并且将其放到常量池中, 并将此字符串对象的地址赋值给引用s(引用s在Java栈中).
使用字符串常量池, 每当我们使用关键字new(`String s=new String("1");`)创建字符串常量时, JVM会首先检查字符串常量池, 如果该字符串已经存在常量池中, 那么不再在字符串常量池创建该字符串对象, 而直接堆中复制该对象的副本, 然后将堆中对象的地址赋值给引用s, 如果字符串不存在常量池中, 就会实例化该字符串并且将其放到常量池中, 然后在堆中复制该对象的副本, 然后将堆中对象的地址赋值给引用s.
[原文链接](https://blog.csdn.net/qq_34490018/article/details/82110578)

## 基本类型中的缓冲池? 什么时候使用缓冲池的数据?
对于整数(包括可以自动转型为整数的类型)来说缓冲池大小为[-128, 127], 超出该部分的不共享数据

## String, StringBuffer, StringBuilder区别?
分别是字符串常量, 字符串变量(线程安全但与StringBuilder相比效率不高), 字符串变量
StringBuilder[底层原理](https://blog.csdn.net/AlbenXie/article/details/89739172)

## 数组定义: String a[10]; 正不正确? 数组等号左边能不能出现数字?
不正确, 数组等号左边不能出现数字.

数组在new后就会为其分配空间

## `System.out.println(25 + "" + 10 + 5);` 输出什么? 
输出"25105", 字符串左边的执行运算操作, 遇到第一个字符串后执行拼接操作.

## `String.replaceAll(old, new);` 其中old是什么形式?
为正则匹配形式

## String使用"+"拼接快还是使用StringBuilder.append()快? 


## 引用类型为null, 能否找到其所属的静态类型?
可以通过声明类型来找到静态方法

## switch参数可以有哪些类型?
7之前只能是int类型以及能够自动转换为int类型的变量, 之后开始支持String

## Object有哪些方法?
getClass(), equals(), hashCode(), clone(), wait(), notify(), notifyAll(), finalize(), toString()

## 构造方法可以有哪些访问修饰符?
四种修饰符之一, 不能为abstract, static, final等, 不能有返回值

## 分析count = count++;
先将count赋予左边的count变量, 然后右边自增, 最终count值还是自增之前的值

## Math.ceil(), Math.floor(), Math.round()
- Math.round(): 将原来的数字加0.5然后向下取整
- Math.ceil(): 向上取整, 符号不变, 可以为-0
- Math.floor(): 向下取整, 符号不变

## Java平台无关性与哪些有关?
字节码技术与JVM虚拟机技术

## 运算符优先级?
单运移比按逻三赋

## lambda表达式的作用? 形参列表、代码块? 优点与缺点?
为替代匿名函数.形式为`()->{}`, 圆括号内为捕获参数, 后面为代码块.
- 优点: 书写方便, 调用速度快, 可以使用非final类型变量
- 缺点: 函数式编程违背面向对象编程; 阅读困难, 因为参数类型可以省略

## 多态定义? 抽象定义? 
编译期与运行期运行结果不一致即多态.

## 多态实现的机制是什么?
重载与重写

## Java中null值是什么?
对象的值为null指这个对象为空对象.

## 管理文件和目录的类是什么?
File, 方法有: createFile(), delete(), isFile(), exists(), listFiles(), isDirectory(), mkdir(), getName(), getPath();

## Java如何将一个Date按照某种日期格式显示?
`java.text.SimpleDateFormat`

## a += b 与 a = a + b有什么区别?
后者会强制转换

## 能不能在不进行强制转换下将double赋给long?
不行, 只可以long不强制转换为double

## 基础数据类型自动转换规则
(byte, short, char) -> int -> long -> double <- float

## 32位JVM和64位JVM最大堆内存分别是多少?
都是32位

## | 和 ||, & 和 && 的区别?
后者为短路逻辑比较

## 怎样将byte转换为string?
new String(str.getBytes(), "utf-8");

## B继承A, C继承B, 可以将B转换为C吗? 如 C = (C) B?
可以进行强制转换, 但是不推荐

## 分析以下代码?
```java
byte a1 = 1, a2 = 2;
final byte b1 = 2, b2 = 3;
a1 = b1 + b2;  	// 会不会报错
a1 = a1 + a2;	// 会不会报错
```

第一行不会报错, 因为b1, b2为final变量不会对其进行转换; 第二行会报错, 在进行运算时a1, a2会转换为int型, 其结果不能自动转换为byte型

## 分析以下代码
```java
String s1 = "abc";
String s2 = new String(s1);
s1 == s2;		// true or false
s1.equals(s2);	// true or false
```
第一行为false, 第二行为true

## 分析以下代码
```java
String s1 = "abc";
String s2 = "a" + new String("bc");
s1 == s2;	// true or false
```
结果为false, 使用new创建的都是新的对象

## Java标识符有哪些?
数字, 字母, 下划线, $; 变量方法不能以数字开头

## 一个文件里有多个接口, 编译后有几个class文件?
有多少个接口编译过后就有多少个class文件

## Java中基本类型有哪些? 大小?
- 整数类型:  byte, int, short, long
- 字符类型:  char
- 浮点类型:  double, float
- 布尔类型:  boolean

## Java中数组是基本类型吗?
数组不是基本类型, Java中除了上述的基本类型外都属于对象类型

## 类中方法可以与类同名吗?
可以同名

## Stream与Reader, Writer区别? 用代码实现一个txt文件的读写
- Stream为字节流
- Reader, Writer为字符流
见`../../java/笔记/java-深入学习/读取文件/Main.java`

## 用代码实现文件递归查询
见`../../java/笔记/java-深入学习/获取文件路径/GetFilePath.java`

## 访问修饰符作用范围?
类内部, 包, 子类, 任何地方

## Java编译过程?
1. 将代码编译成字节码
2. 将字节码载入JVM中称为可执行的代码
3. 运行时将可执行的代码编译为机器码

## Number, ClassLoader可以被继承吗?
可以被继承

---
## JDBC使用什么设计模式?
桥接模式

## 解释一下驱动在JDBC中的角色? JDBC执行大致流程?
初始化, 提供调用方法

## 类之间存在哪些关系? 
is-a, has-a, use-a

## 一般关系型和对象数据模型之间的对应关系?
ORM(Object Relation Mapping), 表对类, 数据对对象, 字段对属性

## 一个类可以同时继承和实现其它类吗? 有没有先后顺序?
先继承后实现

## JRE判断程序是否执行结束的标准是什么?
前台线程执行完毕

## JDK, JRE, JVM的区别和联系?
- JDK: java开发工具, 是java开发核心, 包括javac.exe, java.exe等工具
- JRE: 包含JVM的标准实现与Java基本类
- JVM: 虚拟机

## equals与hashCode联系? equals默认比较什么?
默认情况下hashCode相同, equals不一定相同; 而equals相同的hashCode都相同.
equals默认比较地址, 比较形式为`==`

## 为什么实现equals必须重新hashCode?
一般在集合Set中, 若equals相同则对象相同, 而重写equals不重写hashCode后可能会导致同一个对象hashCode不相同, 违背对象唯一的规则.

## Java中Arrays.sort()如何实现排序?
TIM sort, 将升序子序列找出来, 将非升序进行排序后使用归并算法

## JDK消费者生产者模型应用?
线程池

## final修饰符有什么好处? 可以修饰哪些东西?
好处: 
- 线程安全
- 共享

修饰: 
- 修饰类: 表示该类不可以被继承
- 修饰方法: 方法不可以被重写
- 修饰变量: 基本类型的变量不可以改变值, 对象类型时不可以改变对象的引用, 但可以改变对象的状态
- 修饰参数: 表示该参数只读不可以修改

## 为什么需要克隆, 直接new一个对象不行吗? 浅克隆与深克隆如何实现?
- 直接new一个对象不能保持其拥有的状态.
- 浅克隆拷贝不能拷贝对象类型的属性, 即若某个变量属于对象类型, 那么修改该变量其余地方引用改对象的状态也会变.
- [实现方法](../../java/笔记/java-深入学习/克隆)

## Java中的char可以存汉字吗? 能存所有汉字吗?
Java中能够存储汉字, 默认Unicode下中文字符2个字节.
只要字符没有超过编码范围内的字节都能存下, 而有些特殊汉字的编码超过了范围则不能存储

## RTTI? 
运行时类型信息

## 注解有什么用? 如何自定义注解?
文档, 注入属性

## Java与C++比较?
- Java没有指针, 自动回收垃圾; C++需要手动回收垃圾
- Java是面向对象语言; C++即可以面向对象也可以面向编程
- Java是解释性语言; C++是编译语言
- Java是基于C++编写的
- Java跨平台性比C++好

## public static void main(String[] args); 需要注意哪些? 一个类里面可以有多个main方法吗? main方法可以用final修饰吗? 可以用abstract修饰吗? 可以用synchronized修饰吗?
- 一个类里面可以由多个main方法, 这属于重载.
- main方法可以使用final修饰, 但作为方法入口的main方法不能使用abstract修饰.
- 能使用synchronized修饰.

## 为什么Java中有些接口没有任何方法?
标识接口, 用来表明实现它的类属于一个特定的类型

## 如何实现类似于C中的函数指针功能?
通过声明接口的方法来实现该功能.

## 面向对象和面向过程的区别?
面向对象处理方式与人类思考问题方式一致, 将问题看做一个整体.而面向过程是将问题处理方法进行逻辑抽取, 使用一个个函数来解决.

## 内部类有哪些?
局部类, 匿名内部类, 静态内部类, 成员内部类

## 为什么非静态内部类不能定义静态方法, 静态成员, 静态初始化块?
因为静态方法属于类, 如果调用一个静态方法需要提前实例化一个对象, 那么久违背了该准则.

## 什么是反射, 反射优缺点?
有点: 可扩展, 类浏览器
缺点: 性能开销, 破坏面向对象的封装性

## 反射破坏了面向对象的什么?
封装性.

## 反射创建实例的三种方法?
## 反射中Class.forName()与ClassLoader()区别?
前者会初始化, 后者不会

## 动态代理的几种实现方式? 优缺点? 可以通过类实现吗?
JDK: 通过接口, invocationHandler
cglib: 通过继承(子类可以继承父类私有方法与属性, 只是子类无法直接访问私有方法; 不能继承final修饰的方法), 速度较快.

## 如何获取父类的类名?
`this.getClass().getSuperClass().getName();`

## 什么是泛型? 限定通配符与非限定通配符? List< String > 能否传递给 List< Object >? Array可以使用泛型吗?
- 泛型是类型参数化.
- 指定范围与没有指定范围.
- 不能, 因为点不能赋给不相同的点.
- Array不能使用泛型.

## 泛型会不会导致程序执行速度下降?
不会有影响, 泛型在编译期阶段会进行泛型擦除, 不影响性能.

## 什么是泛型擦除?
编译期阶段使用指定的类进行替换

## try-catch-finally执行过程? finally是不是一定会执行?
执行过程: 先执行try,如果有异常则被catch捕获, 最后执行finally.finally一定会被执行, 即使try中有return语句, 并且如果finally中也有return语句, 则会返回finally中的return语句.

## 拆箱与装箱?
- 装箱: Integer.valueOf(),Integer.parseInt()
- 拆箱: Integer.intValue()

## UML有哪些表示?
- 依赖: ┅┄┅┄>
- 关联: ──────>
- 聚合: 空心◇──
- 组合: 实心◆──
- 泛化-继承: ◁────; 实现◁┅┄┅┄

## 有哪些处理错误的方式?
- 全局标志
- 返回类型
- 抛出异常

## PHP与Java的区别?
- php是脚本语言, java是解释性语言
- java最小单位为类, PHP最小单位为可执行语句; 
- Java内存自动回收, PHP一次创建一次销毁
- Java可常驻内存, 可以实现多线程, 而PHP无法常驻内存, 无法实现多线程

## Java类什么时候加载?
- 实例通过使用new()关键字创建或者使用class.forName()反射, 但它有可能导致ClassNotFoundException.
- 类的静态方法被调用
- 类的静态域被赋值
- 静态域被访问, 而且它不是常量
- 在顶层类中执行assert语句

## static原理?
编译期阶段初始化一次, 共享数据

## static方法能否被覆盖? private方法能不能被覆盖?
static方法属于类方法, 不能被覆盖
private被隐式声明为final, 不能被覆盖

## 类方法内需要注意什么? 类方法能引用对象变量吗?
类方法内不能使用对象方法或对象成员; 类方法不能使用this(), super();类方法可以调用其他类方法

类方法不能引用对象变量

## 什么是类成员, 对象成员?
使用static修饰的成员, 能够被类直接调用的称为类成员
一般成员, 需要通过实例化对象才能调用

## 抽象类和接口区别? 如何选择?
接口: 
- JDK1.8之前不能有方法, 只能声明; 之后可以使用default和static修饰
- 没有普通变量与方法; 变量会加public static final, 方法会加 public abstract
- 可以实现多个接口
- 孩子如果没有完全实现父类的方法不能实例化
- 不能实例化

抽象类: 
- 声明的方法可以由方法体
- 可以由普通变量
- 只能继承一个抽象类
- 孩子如果没有完全实现父类的方法不能实例化
- 不能实例化

选择: 如果确认一个类是基类, 一般让它成为接口.但如果该类需要普通变量, 那么就应该令该类为抽象类

## 面向对象的特性有哪些?
封装, 继承, 多态

## 重载与重写定义? 构成重载条件? 函数返回值的不同可以作为重载吗? 构成重写条件?
重载: 在一个类中方法名相同, 形参列表不同
重写: 子类继承父类重写父类的方法

重载构成条件: 方法名相同, 形参列表不同; 不看返回值与修饰
重写条件: 两同两小一大
- 两同:  方法名, 形参列表相同
- 两小:  返回值类型小于等于父类方法返回值类型, 抛出异常小于等于父类抛出的异常
- 一大: 访问修饰符大于等于父类访问修饰符

## 被final修饰的方法能够被重载吗? 能够被重写吗?
重载不看访问修饰符, final修饰的方法能够被重载
被final修饰的方法不能被重写

## 数组和链表数据结构描述, 各自时间复杂度?
- 真数组在内存上是一段连续区域, 链表则没有这种要求
- 对于删除元素, 数组O(N), 链表O(1)
- 插入元素数组O(1), 链表O(1)
- 搜索元素, 如果数组是排序的则O(logN), 链表为O(N)

## 异常分为哪些? 异常基类?
- Error:非检查异常, 程序无法处理的错误
- Exception: 
checked: 编译时异常属于检查异常, 如文件资源打开关闭必须捕获
Runtime: 运行时异常, 不必处理, 不必要捕获

## 类加载过程, 机制? 有什么优势? 类加载器有哪些?
过程: 加载-链接-初始化
机制: 双亲委托加载
优势: 保证核心API, 避免重复加载
类加载器: BootStrap ClassLoader, Extention ClassLoader, App ClassLoader, Custom ClassLoader

## 解释一下Serialization和Deserialization? serialVersionUID有什么用?
将对象转化为字节序列
serialVersionUID: 对序列化对象进行版本管理

## 被static或transient修饰的属性能被序列化吗?
这两种修饰的属性不能被序列化

## "a == b" 与 a.equals(b)的区别?
地址比较和逻辑比较

## 开发中用字节流好还是字符流好?
字符流 = 字节流 + 编码

## Comparable和Comparator的区别?
comparator: 重写compare
Comparable: 重写compareTo

## Java正则表达式匹配"成都市(武侯区)(高新区)"中的成都市?
```java
Pattern pattern = Pattern.compile(".*?(?=\\()");
Matcher matcher = pattern.matcher(str);
if (matcher.find()) {
	System.out.println(matcher.group(0));
}
```
## Java中socket连接过程?
服务器: bind, listen, accept, connect, write/read, close
客户端: connect, write/read, close

## Java中的引用有哪些类型? 目的是什么? 使用软引用能够带来什么好处?
- 强: 一般对象引用
- 软: 只有当内存不足时才会对失去引用的对象进行回收
- 弱: 一旦失去最后一个强引用, 立即回收
- 虚: 用来跟踪对象被垃圾回收的活动, 虚引用必须和引用队列(ReferenceQueue)联合使用.程序可以通过判断引用队列中是 否已经加入了虚引用, 来了解被引用的对象是否将要被垃圾回收.程序如果发现某个虚引用已经被加入到引用队列, 那么就可以在所引用的对象的内存被回收之前采取必要的行动.[参考](https://www.cnblogs.com/javaee6/p/4763190.html)
- 目的: 以代码的形式管理对象生命周期

软引用好处: 提升JVM内存使用性能

## throw和throws的区别?
前者抛出一个具体异常; 后者只是声明可能会抛出的异常不一定会抛出

## 处理完异常后, Exception会有什么变化?
会在下一个垃圾回收过程中被回收

## Java中用什么数据类型来代表价格?
BigDecimal, 需要使用字符串初始化, 用double初始化仍然不能精确表示

## 64位JVM中int的长度是多少?
无论什么平台都是32

## final, finally, finalize的区别?
- final修饰类, 类不可以被继承; 修饰方法, 方法不可以被重写; 修饰变量, 基本类型的值不可以改变, 引用类型不能改变其引用
- finally:try中使用, 而且一定会执行
- finalize: object方法, 重写后给变量一个自救机会, 让其与root链上的对象进行关联

## 编译器常量有什么风险?
即final static, 修改之后需要重新编译才能使用新值

## 构造方法能不能被继承? 有没有返回值?
构造方法不能被继承, 没有返回值

## this()写第一行的原因? super()写第一行的原因? 可以写在一起吗?
- this()写在第一行表示使用了委托构造, 不能和super()一起使用; 
- 防止父类重复构造
- super()写第一行是为保证父类方法的可用性

## 类初始化过程?
父类静态成员、父类静态代码块-子类静态成员、子类静态代码块-父类普通成员、父类代码块、父类构造函数-子类普通成员、子类代码块、子类构造函数

## Collection与Collections的区别?
前者属于集合接口; 后者是集合方法的集合

## '0', 'A', 'a', ' ' 的ASCII码是多少? 
48,65,97,32

## 在Java中unicode占多少字节? UTF-8下中文占多少字节, 英文占多少字节? GBK呢?
- 2字节
- 中3字节, 英1字节
- 中2字节, 英1字节

## instacneof有什么作用?
判断一个对象是否属于指定的类型

## System.arraycopy(), clone(), Arrays.copyOf(), for对数组的复制效率?
性能递减

---

## 什么是servlet?
接受用户请求, 生成动态内容

## servlet生命周期?
加载, 创建, 初始, 调用方法, 销毁

## servlet处理流程?
<71>
## 服务端包含?
## 什么是servlet链?
## servlet安全性? 
## Tomcat结构以及类加载流程?