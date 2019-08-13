> ## Java基础知识问答

### java关键字与保留字? goto, const? false, true, null, inner?
goto没有定义, 但自己也不能使用这样的变量名, 使用编译后会报错
关键字与保留字作为变量使用会报错

### String能被继承吗?
不能继承, 使用final修饰

### String底层如何实现? 不可变的好处? 采用什么设计模式? 什么是String Pool?
JDK1.8，String内部使用`private final char value[];`
JDK1.9, String定义时使用`private final byte value[]`有些字母不需要两个字节，节省空间
不可变的好处：线程安全，哈希值存储，字符串常量池
采用享元设计模式
字符串常量池在JDK1.7时被转移到堆中，之前在方法区的运行时常量池中。
使用字符串常量池，每当我们使用字面量（`String s=”1”;`）创建字符串常量时，JVM会首先检查字符串常量池，如果该字符串已经存在常量池中，那么就将此字符串对象的地址赋值给引用s（引用s在Java栈中）。如果字符串不存在常量池中，就会实例化该字符串并且将其放到常量池中，并将此字符串对象的地址赋值给引用s（引用s在Java栈中）。
使用字符串常量池，每当我们使用关键字new（`String s=new String(”1”);`）创建字符串常量时，JVM会首先检查字符串常量池，如果该字符串已经存在常量池中，那么不再在字符串常量池创建该字符串对象，而直接堆中复制该对象的副本，然后将堆中对象的地址赋值给引用s，如果字符串不存在常量池中，就会实例化该字符串并且将其放到常量池中，然后在堆中复制该对象的副本，然后将堆中对象的地址赋值给引用s。
[原文链接](https://blog.csdn.net/qq_34490018/article/details/82110578)

### 基本类型中的缓冲池? 什么时候使用缓冲池的数据?
### String, StringBuffer, StringBuilder区别?
分别是字符串常量，字符串变量(线程安全但与StringBuilder相比效率不高)，字符串变量
StringBuilder[底层原理](https://blog.csdn.net/AlbenXie/article/details/89739172)

### 数组定义: String a[10]; 正不正确? 数组等号左边能不能出现数字?
### `System.out.println(25 + "" + 10 + 5);` 输出什么? 
### `String.replaceAll(old, new);` 其中old是什么形式?
### 引用类型为null, 能否找到其所属的静态类型?
### switch参数可以有哪些类型?
7之前只能是int类型以及能够自动转换为int类型的变量, 之后开始支持String

### Object有哪些方法?
getClass(), equals(), hashCode(), clone(), wait(), notify(), notifyAll(), finalize(), toString()

### 构造方法可以有哪些访问修饰符?
四种修饰符之一, 能为abstract, static, final等，不能有返回值

### 分析count = count++;
### Math.ceil(), Math.floor(), Math.round()
Math.round(): 将原来的数字加0.5然后向下取整

### Java平台无关性与哪些有关?
### 运算符优先级?
单运移比按逻三赋

### lambda表达式的作用? 形参列表、代码块? 优点与缺点?
### 多态定义? 抽象定义? 
### 多态实现的机制是什么?
重载与重写

### Java中null值是什么?
### 管理文件和目录的类是什么?
File, 方法有: createFile(), delete(), isFile(), exists(), listFiles(), isDirectory(), mkdir(), getName(), getPath();

### Java如何将一个Date按照某种日期格式显示?
`java.text.SimpleDateFormat`

### a += b 与 a = a + b有什么区别?
后者会强制转换

### 能不能在不进行强制转换下将double赋给long?
### 基础数据类型自动转换规则
### 32位JVM和64位JVM最大堆内存分别是多少?
### | 和 ||, & 和 && 的区别?
### 怎样将byte转换为string?
### B继承A, C继承B, 可以将B转换为C吗? 如 C = (C)B?
### 分析以下代码?
```java
byte a1 = 1, a2 = 2;
final byte b1 = 2, b2 = 3;
a1 = b1 + b2;  	// 会不会报错
a1 = a1 + a2;	// 会不会报错
```
### 分析以下代码
```java
String s1 = "abc";
String s2 = new String(s1);
s1 == s2;		// true or false
s1.equals(s2);	// true or false
```
### 分析以下代码
```java
String s1 = "abc";
String s2 = "a" + new String("bc");
s1 == s2;	// true or false
```
### Java标识符有哪些?
数字，字母，下划线，$；变量方法不能以数字开头

### 一个文件里有多个接口, 编译后有几个class文件?
### Java中基本类型有哪些? 大小?
### Java中数组是基本类型吗?
### 类中方法可以与类同名吗?
### Stream与Reader, Writer区别? 用代码实现一个txt文件的读写
### 用代码实现文件递归查询
### 访问修饰符作用范围?
类内部，包，子类，任何地方

### Java编译过程?
### Number, ClassLoader可以被继承吗?

---
### JDBC使用什么设计模式?
桥接模式

### 解释一下驱动在JDBC中的角色? JDBC执行大致流程?
初始化，提供调用方法

### 类之间存在哪些关系? 
is-a, has-a, use-a

### 一般关系型和对象数据模型之间的对应关系?
### 一个类可以同时继承和实现其它类吗? 有没有先后顺序?
先继承后实现

### JRE判断程序是否执行结束的标准是什么?
前台线程执行完毕

### JDK, JRE, JVM的区别和联系?
- JDK: java开发工具, 是java开发核心, 包括javac.exe, java.exe等工具
- JRE: 包含JVM的标准实现与Java基本类
- JVM: 虚拟机

### equals与hashCode联系? equals默认比较什么?
### 为什么实现equals必须重新hashCode?
### Java中Arrays.sort()如何实现排序?
TIM sort

### JDK消费者生产者模型应用?
线程池

### final修饰符有什么好处? 可以修饰哪些东西?
线程安全，共享

### 为什么需要克隆, 直接new一个对象不行吗? 浅克隆与深克隆如何实现?
### Java中的char可以存汉字吗? 能存所有汉字吗?
### RTTI? 
### 注解有什么用? 如何自定义注解?
### Java与C++比较?
### public static void main(String[] args); 需要注意哪些? 一个类里面可以有多个main方法吗? main方法可以用final修饰吗? 可以用abstract修饰吗? 可以用synchronized修饰吗?
### 为什么Java中有些接口没有任何方法?
标识接口, 用来表明实现它的类属于一个特定的类型

### 如何实现类似于C中的函数指针功能?
### 面向对象和面向过程的区别?
### 内部类有哪些?
### 为什么非静态内部类不能定义静态方法, 静态成员, 静态初始化块?
### 什么是反射, 反射优缺点?
有点: 可扩展, 类浏览器
缺点: 性能开销, 破坏面向对象的封装性

### 反射破坏了面向对象的什么?
### 反射创建实例的三种方法?
### 反射中Class.forName()与ClassLoader()区别?
### 动态代理的几种实现方式? 优缺点? 可以通过类实现吗?
JDK: 通过接口, invocationHandler
cglib: 通过继承(子类可以继承父类私有方法与属性，只是子类无法直接访问私有方法；不能继承final修饰的方法), 速度较快。

### 如何获取父类的类名?
`this.getClass().getSuperClass().getName();`

### 什么是泛型? 限定通配符与非限定通配符? List< String > 能否传递给 List< Object >? Array可以使用泛型吗?
### 泛型会不会导致程序执行速度下降?
### 什么是泛型擦除?
### try-catch-finally执行过程? finally是不是一定会执行?
### 拆箱与装箱?
装箱: Integer.valueOf(), 拆箱: Integer.intValue()

### UML有哪些表示?
依赖, 关联, 聚合, 泛化-继承、实现
### 有哪些处理错误的方式?
### PHP与Java的区别?
### Java类什么时候加载?
php是脚本语言, java是解释性语言; java最小单位为类, PHP最小单位为可执行语句; 
Java内存自动回收, PHP一次创建一次销毁; Java可常驻内存, 可以实现多线程, 而PHP无法常驻内存, 无法实现多线程
### static原理?
### static方法能否被覆盖? private方法能不能被覆盖?
private被隐式声明为final
### 类方法内需要注意什么? 类方法能引用对象变量吗?
### 什么是类成员, 对象成员?
### 抽象类和接口区别? 如何选择?
### 面向对象的特性有哪些?
### 重载与重写定义? 构成重载条件? 函数返回值的不同可以作为重载吗? 构成重写条件?
### 被final修饰的方法能够被重载吗? 能够被重写吗?
### 数组和链表数据结构描述, 各自时间复杂度?
### 异常分为哪些? 异常基类?
- Error:非检查异常，程序无法处理的错误
- Exception: 
checked: 编译时异常属于检查异常，如文件资源打开关闭必须捕获
Runtime: 运行时异常，不必处理

### 类加载过程, 机制? 有什么优势? 类加载器有哪些?
过程：加载-链接-初始化
机制：父亲委托
优势：保证核心API，避免重复加载
类加载器：BootStrap ClassLoader, Extention ClassLoader, App ClassLoader, Custom ClassLoader

### 解释一下Serialization和Deserialization? serialVersionUID有什么用?
将对象转化为字节序列
serialVersionUID: 对序列化对象进行版本管理

### 被static或transient修饰的属性能被序列化吗?
不能

### "a == b" 与 a.equals(b)的区别?
地址比较和逻辑比较

### 开发中用字节流好还是字符流好?
### Comparable和Comparator的区别?
comparator: 重写compare
Comparable: 重写compareTo

### Java正则表达式匹配"成都市(武侯区)(高新区)"中的成都市?
```java
Pattern pattern = Pattern.compile(".*?(?=\\()");
Matcher matcher = pattern.matcher(str);
if (matcher.find()) {
	System.out.println(matcher.group(0));
}
```
### Java中socket连接过程?
服务器：bind, listen, accept, connect, write/read, close
客户端: connect, write/read, close

### Java中的引用有哪些类型? 目的是什么? 使用软引用能够带来什么好处?
强：一般对象引用
软：只有当内存不足时才会对失去引用的对象进行回收
弱：一旦失去最后一个强引用，立即回收
虚：用来跟踪对象被垃圾回收的活动，虚引用必须和引用队列（ReferenceQueue）联合使用。程序可以通过判断引用队列中是 否已经加入了虚引用，来了解被引用的对象是否将要被垃圾回收。程序如果发现某个虚引用已经被加入到引用队列，那么就可以在所引用的对象的内存被回收之前采取必要的行动。[参考](https://www.cnblogs.com/javaee6/p/4763190.html)
目的：以代码的形式管理对象生命周期

软引用好处：提升JVM内存使用性能

### throw和throws的区别?
前者抛出一个具体异常；后者只是声明可能会抛出的异常不一定会抛出

### 处理完异常后, Exception会有什么变化?
### Java中用什么数据类型来代表价格?
BigDecimal, 需要使用字符串初始化, 用double初始化仍然不能精确表示

### 64位JVM中int的长度是多少?
无论什么平台都是32

### final, finally, finalize的区别?
final修饰类，类不可以被继承；修饰方法，方法不可以被重写；修饰变量，基本类型的值不可以改变，引用类型不能改变其引用

### 编译器常量有什么风险?
修改之后没有重新编译

### 构造方法能不能被继承? 有没有返回值?
构造方法不能被继承，没有返回值

### this()写第一行的原因? super()写第一行的原因? 可以写在一起吗?
this()写在第一行表示使用了委托构造，不能和super()一起使用；防止父类重复构造
super()写第一行是为保证父类方法的可用性

### 类初始化过程?
父类静态成员、父类静态代码块-子类静态成员、子类静态代码块-父类普通成员、父类代码块、父类构造函数-子类普通成员、子类代码块、子类构造函数

### Collection与Collections的区别?
前者属于集合接口；后者是集合方法的集合

### '0', 'A', 'a', ' ' 的ASCII码是多少? 
48,65,97,32
### 在Java中unicode占多少字节? UTF-8下中文占多少字节, 英文占多少字节? GBK呢?
2字节；2字节，1字节；中3字节，英1字节

### instacneof有什么作用?
### System.arraycopy(), clone(), Arrays.copyOf(), for对数组的复制效率?
性能递减
---
### 什么是servlet?
接受用户请求，生成动态内容

### servlet生命周期?
加载，创建，初始，调用方法，销毁
### servlet处理流程?
<71>
### 服务端包含?
### 什么是servlet链?
### servlet安全性? 
### Tomcat结构以及类加载流程?