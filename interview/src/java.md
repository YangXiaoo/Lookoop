> ## Java基础知识问答

#### java关键字与保留字? goto,const?false,true,null,inner?
### String能被继承吗? 
### string,StringBuffer,StringBuilder区别?
### 数组定义: String a[10]; 正不正确? 数组等号左边能不能出现数字?
### System.out.println(25 + "" + 10 + 5);输出什么? 
### String.replaceAll(old, new); 其中old是什么形式?
### 引用类型为null, 能否找到其所属的静态类型?
### switch参数可以有哪些类型?
### Object有哪些方法?
### 构造方法可以有哪些访问修饰符?
### 分析count = count++;
### Math.ceil(),Math.floor(), Math.round()
### Java平台无关性与哪些有关?
### 运算符优先级?
### lambda表达式的作用?形参列表、代码块? 优点与缺点?
### 多态定义?抽象定义? 
### 多态实现的机制是什么?
### Java中null值是什么?
### 管理文件和目录的类是什么?
### Java如何将一个Date按照某种日期格式显示?
### a += b 与 a = a + b有什么区别?
### 能不能在不进行强制转换下将double赋给long?
### 基础数据类型自动转换规则
### 32位JVM和64位JVM最大堆内存分别是多少?
### | 和 ||, & 和 &&的区别?
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
### 一个文件里有多个接口, 编译后有几个class文件?
### Java中基本类型有哪些? 大小?
### Java中数组是基本类型吗?
### 类中方法可以与类同名吗?
### Stream与Reader, Writer
### 访问修饰符作用范围?
### Java编译过程?
### Number, ClassLoader可以被继承吗?

---
### JDBC使用什么设计模式?
### 类之间存在哪些关系? 
### 一般关系型和对象数据模型之间的对应关系?
### 一个类可以同时继承和实现其它类吗? 有没有先后顺序?
### JRE判断程序是否执行结束的标准是什么?
### JDK, JRE, JVM的区别和联系?
### 解释一下驱动在JDBC中的角色?
### equals与hashCode联系? equals默认比较什么?
### 为什么实现equals必须重新hashCode?
### Java中Arrays.sort()如何实现排序?
### JDK消费者生产者模型应用?
### final修饰符有什么好处?可以修饰哪些东西?
### 为什么需要克隆,直接new一个对象不行吗?浅克隆与深克隆如何实现?
### Java中的char可以存汉字吗?能存所有汉字吗?
### RTTI? 
### 注解有什么用?如何自定义注解?
### Java与C++比较?
### public static void main(String[] args); 需要注意哪些? 一个类里面可以有多个main方法吗? main方法可以用final修饰吗? 可以用synchronized修饰吗?
### 为什么Java中有些接口没有任何方法?
### 如何实现类似于C中的函数指针功能?
### 面向对象和面向过程的区别?
### 内部类有哪些?
### 为什么非静态内部类不能定义静态方法, 静态成员, 静态初始化块?
### 什么是反射, 反射优缺点?
### 反射破坏了面向对象的什么?
### 反射创建实例的三种方法?
### Class.forName()有什么作用?
### 反射中Class.forName()与ClassLoader()区别?
### 动态代理的几种实现方式? 优缺点? 可以通过类实现吗?
### 如何获取父类的类名?
### 什么是泛型? 限定通配符与非限定通配符? List< String > 能否传递给 List< Object >? Array可以使用泛型吗?
### 泛型会不会导致程序执行速度下降?
### 什么是泛型擦除?
### String底层如何实现? 不可变的好处? 采用什么设计模式?什么是String Pool?
### 基本类型中的缓冲池? 什么时候使用缓冲池的数据?
### try-catch-finally执行过程? finally是不是一定会执行?
### 拆箱与装箱?
### finalize什么时候使用? 为什么避免使用? 
### UML有哪些表示?
### 有哪些处理错误的方式?
### PHP与Java的区别?
### Java类什么时候加载?
### static原理?
### static方法能否被覆盖? private方法能不能被覆盖?
### 类方法内需要注意什么? 类方法能引用对象变量吗?
### 什么是类成员, 对象成员?
### 抽象类和接口区别? 如何选择?
### 面向对象的特性有哪些?
### 重载与重写定义? 构成重载条件? 函数返回值的不同可以作为重载吗? 构成重写条件?
### 被final修饰的方法能够被重载吗? 能够被重写吗?
### 数组和链表数据结构描述, 各自时间复杂度?
### 异常分为哪些? 异常基类?
### 类加载过程, 机制? 有什么优势? 类加载器有哪些?
### 解释一下Serialization和Deserialization? serialVersionUID有什么用?
### 被static或transient修饰的属性能被序列化吗?
### "a == b" 与 a.equals(b)的区别?
### 开发中用字节流好还是字符流好?
### Comparable和Comparator的区别?
### Java正则表达式匹配"成都市(武侯区)(高新区)"中的成都市?
### Java中socket连接过程?
### Java中的引用有哪些类型? 目的是什么?
### throw和throws的区别?
### 处理完异常后, Exception会有什么变化?
### Java中用什么数据类型来代表价格?
### 64位JVM中int的长度是多少?
### final, finally, finalize的区别?
### 编译器常量有什么风险?
### 构造方法能不能被继承? 有没有返回值?
### this()写第一行的原因? super()写第一行的原因? 可以写在一起吗?
### 类初始化过程?
### Collection与Collections的区别?
### '0', 'A', 'a', ' ' 的ASCII码是多少?
### 在Java中unicode占多少字节?UTF-8下中文占多少字节, 英文占多少字节? GBK呢?
### instacneof有什么作用?
### System.arraycopy(), clone(), Arrays.copyOf(), for对数组的复制效率?
---
### 什么是servlet?
### servlet生命周期?
### servlet处理流程?
### 服务端包含?
### 什么是servlet链?
### servlet安全性？
### Tomcat结构以及类加载流程?
