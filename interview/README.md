> 关于Java基础知识, JVM, 多线程, 计算机网络, 数据库, 分布式, 算法, Java框架, 测试, Linux等知识, 详细答案见`/src/`目录下的细分内容, 里面附有面经

> ## Java基础

- java关键字与保留字? goto, const? false, true, null, inner?
- String能被继承吗?
- String底层如何实现? 不可变的好处? 采用什么设计模式? 什么是String Pool?
- 基本类型中的缓冲池? 什么时候使用缓冲池的数据?
- String, StringBuffer, StringBuilder区别?
- 数组定义: String a[10]; 正不正确? 数组等号左边能不能出现数字?
- `System.out.println(25 + "" + 10 + 5);` 输出什么? 
- `String.replaceAll(old, new);` 其中old是什么形式?
- String使用"+"拼接快还是使用StringBuilder.append()快? 
- 引用类型为null, 能否找到其所属的静态类型?
- switch参数可以有哪些类型?
- Object有哪些方法?
- 构造方法可以有哪些访问修饰符?
- 分析count = count++;
- Math.ceil(), Math.floor(), Math.round()
- Java平台无关性与哪些有关?
- 运算符优先级?
- lambda表达式的作用? 形参列表、代码块? 优点与缺点?
- 多态定义? 抽象定义? 
- 多态实现的机制是什么?
- Java中null值是什么?
- 管理文件和目录的类是什么?
- Java如何将一个Date按照某种日期格式显示?
- a += b 与 a = a + b有什么区别?
- 能不能在不进行强制转换下将double赋给long?
- 基础数据类型自动转换规则
- 32位JVM和64位JVM最大堆内存分别是多少?
- | 和 ||, & 和 && 的区别?
- 怎样将byte转换为string?
- B继承A, C继承B, 可以将B转换为C吗? 如 C = (C) B?
- 分析以下代码?
```java
byte a1 = 1, a2 = 2;
final byte b1 = 2, b2 = 3;
a1 = b1 + b2;  	// 会不会报错
a1 = a1 + a2;	// 会不会报错
```
- 分析以下代码
```java
String s1 = "abc";
String s2 = new String(s1);
s1 == s2;		// true or false
s1.equals(s2);	// true or false
```
- 分析以下代码
```java
String s1 = "abc";
String s2 = "a" + new String("bc");
s1 == s2;	// true or false
```
- Java标识符有哪些?
- 一个文件里有多个接口, 编译后有几个class文件?
- Java中基本类型有哪些? 大小?
- Java中数组是基本类型吗?
- 类中方法可以与类同名吗?
- Stream与Reader, Writer区别? 用代码实现一个txt文件的读写
- 用代码实现文件递归查询
- 访问修饰符作用范围?
- Java编译过程?
- Number, ClassLoader可以被继承吗?
---
- JDBC使用什么设计模式?
- 解释一下驱动在JDBC中的角色? JDBC执行大致流程?
- 类之间存在哪些关系? 
- 一般关系型和对象数据模型之间的对应关系?
- 一个类可以同时继承和实现其它类吗? 有没有先后顺序?
- JRE判断程序是否执行结束的标准是什么?
- JDK, JRE, JVM的区别和联系?
- equals与hashCode联系? equals默认比较什么?
- 为什么实现equals必须重新hashCode?
- Java中Arrays.sort()如何实现排序?
- JDK消费者生产者模型应用?
- final修饰符有什么好处? 可以修饰哪些东西?
- 为什么需要克隆, 直接new一个对象不行吗? 浅克隆与深克隆如何实现?
- Java中的char可以存汉字吗? 能存所有汉字吗?
- RTTI? 
- 注解有什么用? 如何自定义注解?
- Java与C++比较?
- public static void main(String[] args); 需要注意哪些? 一个类里面可以有多个main方法吗? main方法可以用final修饰吗? 可以用abstract修饰吗? 可以用synchronized修饰吗?
- 为什么Java中有些接口没有任何方法?
- 如何实现类似于C中的函数指针功能?
- 面向对象和面向过程的区别?
- 内部类有哪些?
- 为什么非静态内部类不能定义静态方法, 静态成员, 静态初始化块?
- 什么是反射, 反射优缺点?
- 反射破坏了面向对象的什么?
- 反射创建实例的三种方法?
- 反射中Class.forName()与ClassLoader()区别?
- 动态代理的几种实现方式? 优缺点? 可以通过类实现吗?
- 如何获取父类的类名?
- 什么是泛型? 限定通配符与非限定通配符? List< String > 能否传递给 List< Object >? Array可以使用泛型吗?
- 泛型会不会导致程序执行速度下降?
- 什么是泛型擦除?
- try-catch-finally执行过程? finally是不是一定会执行?
- 拆箱与装箱?
- UML有哪些表示?
- 有哪些处理错误的方式?
- PHP与Java的区别?
- Java类什么时候加载?
- static原理?
- static方法能否被覆盖? private方法能不能被覆盖?
- 类方法内需要注意什么? 类方法能引用对象变量吗?
- 什么是类成员, 对象成员?
- 抽象类和接口区别? 如何选择?
- 面向对象的特性有哪些?
- 重载与重写定义? 构成重载条件? 函数返回值的不同可以作为重载吗? 构成重写条件?
- 被final修饰的方法能够被重载吗? 能够被重写吗?
- 数组和链表数据结构描述, 各自时间复杂度?
- 异常分为哪些? 异常基类?
- 类加载过程, 机制? 有什么优势? 类加载器有哪些?
- 解释一下Serialization和Deserialization? serialVersionUID有什么用?
- 被static或transient修饰的属性能被序列化吗?
- "a == b" 与 a.equals(b)的区别?
- 开发中用字节流好还是字符流好?
- Comparable和Comparator的区别?
- Java正则表达式匹配"成都市(武侯区)(高新区)"中的成都市?
```java
Pattern pattern = Pattern.compile(".*?(?=\\()");
Matcher matcher = pattern.matcher(str);
if (matcher.find()) {
	System.out.println(matcher.group(0));
}
```
- Java中socket连接过程?
- Java中的引用有哪些类型? 目的是什么? 使用软引用能够带来什么好处?
- throw和throws的区别?
- 处理完异常后, Exception会有什么变化?
- Java中用什么数据类型来代表价格?
- 64位JVM中int的长度是多少?
- final, finally, finalize的区别?
- 编译器常量有什么风险?
- 构造方法能不能被继承? 有没有返回值?
- this()写第一行的原因? super()写第一行的原因? 可以写在一起吗?
- 类初始化过程?
- Collection与Collections的区别?
- '0', 'A', 'a', ' ' 的ASCII码是多少? 
- 在Java中unicode占多少字节? UTF-8下中文占多少字节, 英文占多少字节? GBK呢?
- instacneof有什么作用?
- System.arraycopy(), clone(), Arrays.copyOf(), for对数组的复制效率?
---
- 什么是servlet?
- servlet生命周期?
- servlet处理流程?
- 服务端包含?
- 什么是servlet链?
- servlet安全性? 
- Tomcat结构以及类加载流程?
---


> ## 集合问题

- 线程同步的集合有哪些?
- 哪些类实现了Collection接口?
- 为什么集合没有实现Cloneable和Serializable?
- Iterator和ListIterator区别? 
- Enumeration接口和Iterator接口的区别?
- 快速失败(fail-fast)和安全失败(fail-safe)区别? 
- 数组和列表有什么区别? 如何选择
- ArrayList与LinkedList区别? 底层原理? ArrayList扩容、删除如何实现?
- LinkedList适合什么排序?
- 用过哪些Map类, 都有神马区别? HashMap实现过程(JDK1.8)? put、扩充等实现过程? 
- 为什么HashMap里数组使用transient修饰?
- HashMap的长度为什么是2的幂次方?
- HashMap链表插入是头插入还是尾插入? 头插入会造成什么问题? 
- HashMap为什么用红黑树而不用AVL树?
- concurrentHashMap实现原理? JDK1.7与JDK1.8区别?
- HashTable和HashMap的区别?
- HashTable和concurrentHashMap的区别?
- HashSet, TreeSet, LinkedHashSet之间的区别? HashSet内部原理?
- 阻塞队列, ArrayBlockingQueue, LinkedBlockingQueue, PriorityBlockingQueue, DelayQueue, SynchronousQueue各自特点? 非阻塞队列? 
- 阻塞队列的插入、移除方法?
- Set了解过吗? 知道add()会出现什么问题吗? 
---


> ## 线程

- 如果一个线程构造了一个不可变对象, 就可以保证这个对象被其它程序正确查看吗? 
- 线程调用过程?
- 守护线程和用户线程区别?
- 你对线程优先级的理解?
- 同步方法和同步块哪种方式好?
- 线程有哪些状态? 画一下线程状态转移图
- 数据库连接池与线程池?
- 为什么使用线程池, 为什么使用数据库连接池?
- 线程池ThreadPoolExecutor有哪些参数? 
- 线程池中线程任务数超过核心数会发生什么? 阻塞队列大小? 
- 线程池的组成?
- Java线程池工作原理(过程)?
- newSingleThreadExcutor, newFixedThreadPool, newCachedThreadPool, newScheduledThreadPool, newSingleThreadScheduledExcutor区别?
- 线程池的关闭有几种方式? 有哪些状态? 状态转移?
- 说一说ThreadLocal使用, 原理?
- ThreadLocal内存泄露? 如何解决?
- 为什么ThreadLocal要使用弱引用?
- synchronized锁的范围? 
- synchronized与Lock比较(锁与同步锁的比较)?
- synchronized与cas比较?
- 说说 synchronized 关键字和 volatile 关键字的区别
- 介绍一下AQS? 
- ReentrantLock如何实现可重入? 如何实现公平锁与非公平锁?
- 在监视器内部如何做到线程同步? 程序应该用哪种级别的同步? synchronized如何实现可重入(底层)? 
- 说说 JDK1.6 之后的synchronized 关键字底层做了哪些优化, 可以详细介绍一下这些优化吗
- 什么是自旋锁, 阻塞锁, 可重入锁, 乐观锁和悲观锁(使用场景, 各自实例), 轮询锁, 显示锁和内置锁, 读写锁, 对象锁和类锁, 锁粗化, 互斥锁, 消除锁, 轻量锁和偏向锁(这两个属于什么类型的锁)? 有几种锁状态?
- volatile实现原理? 保证了什么? 能否保证原子性?
- CAS机制? 包含哪些操作? 会产生哪些问题? 如何避免ABA问题?
- 有哪些原子类?
- 什么是原子操作? 什么是内存屏障?
- 线程池设置大小与CPU的关系? 
- Thread中join()方法的原理? 
- Thread.wait()可以设置超时吗?
- Java主线程如何捕获子线程抛出的异常? 
- 线程安全的实现方法?
- 如何判断线程是否终止? 如何正确终止处于运行状态的线程?
- isInterrupted和interrupted的区别?
- 并行和并发的区别?
- 什么是协程?
- 一个类可以同时继承Thread和实现Runnable接口吗?
- 如何让正在运行的线程暂停一段时间?
- sleep和yield的区别?
- sleep和wait的区别?
- 线程挂起怎么办?
- 导致死锁的原因? 怎么解除死锁?
- 死锁, 饥饿, 活锁之间的定义区别?
- 当一个线程进入一个对象的一个synchronized方法后, 其他线程是否可以进入该对象的其他方法?
- 线程实现接口 VS 继承Thread
- FutureTask是什么?
- 说一下CylicBarrier与CountDownLatch的区别?
- CylicBarrier与CountDownLatch内部实现原理?
- Random与ThreadLocalRandom? 
- ReentrantReadWriteLock原理
- 什么是Semaphore? Exchanger?
- NIO, BIO, AIO区别? 谈谈Reactor模型
- 阻塞与非阻塞, 异步与同步区别?
- 加入有一个第三方接口, 有很多线程去调用获取数据, 现在规定每秒钟最多有10个线程同时调用它, 如何做到?
- 线程之间相互协调完成某个工作, 如何设计?
- 如何实现一个并发安全的链表?
- 如何保证N个线程可以访问N个资源, 同时又不会导致死锁?
- 高并发下如何做到安全地修改一行数据?
- 多个线程达到同一个状态再执行, 如何实现?
- 如何指定多个线程顺序?
- 如何控制线程在某个时间内完成, 不完成就撤销?
- 为什么使用读写锁而不使用synchronized这类锁?
- 实现多线程的方法?
- 实现Runnable接口和Callable接口的区别?
- 执行execute()方法和submit()方法的区别是什么呢?
- 如何创建线程池?

---


> ## JVM虚拟机与JMM内存模型

- JVM, JMM
- JVM内存模型(介绍下 Java 内存区域/运行时数据区)? 程序计数器, 栈, 堆, 方法区?
- JDK1.7之前常量池在哪里? 之后在哪里?
- JDK1.8永久代变为了什么?
- Java内存模式对final的实现? 什么是引用逃逸?
- 什么是元空间?
- Java基本类型、引用类型在内存中的存储原理?
- JVM如何判断两个类是否相同?
- 分析 `Object obj = new Object();` 对象创建过程?
- `String.intern()`?
- `String s = new String("abc");`创建了几个对象?
- 栈中对象引用有几种方法? 详细介绍一下区别? 
- JVM年轻代与老年代? 年轻代垃圾回收过程? 
- 永久代会发生垃圾回收吗?
- JVM年轻代中Eden与survivor的比例?
- 垃圾回收算法有哪些?
- 垃圾回收策略?
- 垃圾收集器有哪些? CMS特点?
- CMS中什么是浮动垃圾?
- 比较一下G1与CMS?
- 整个JVM大小?
- 年老代堆空间被占满如何解决? 持久代被占满如何解决? 堆栈溢出如何解决?
- 如何解决异常Fatal: Stack size too small?
- 如何解决异常java.lang.OutOfMemoryError: unable to create new native thread?
- JMM内存模型中的规定了哪八种操作? 什么是重排序?
- 内存模型三大特性? 原子性、可见性、有序性如何实现?
- 堆上的内存如何释放, 栈上的内容如何释放?
- Java内存泄露的最直接表现? 
- 什么是内存溢出, 什么是内存泄露? Java会不会发生内存泄露?
- 什么情况下会发生内存溢出?
- 老年代溢出原因? 永久代溢出原因?
- 如果对象的引用被置为null, 垃圾回收器是否会立即释放该对象占用的内存?
- Java中对象什么时候可以被垃圾回收?
- 你能保证GC吗?
- finalize什么时候使用? 为什么避免使用? 
- JVM如何确定一个对象是不是有引用?
- GC Roots包含哪些?
- GC Roots 对不可用对象的判断过程?
- 什么时候新生代会发生GC? 老年代发生GC条件? Full GC 触发条件? +
- 永久代回收条件?
- GC为什么要分代?
- JVM中大对象被分配到哪里? 长期存活对象进入哪里? 什么是空间分配担保?
- 进入老年代的几种情况?
- JRE判断程序是否结束的标准?
- 什么是安全点?
- 什么是happens-before(先发行为原则)?
- 对象创建的过程?
- 对象内存布局?
- 被动引用有哪些情况?
- 静态解析和动态解析?
- 静态分配和动态分配?
- 频繁FullGC如何排查?
- JVM中存在大量图片如何解决?
- 双重校验锁为什么要加锁后再次判断是否为空? 为什么外面还要判断? 

---


> ## 计算机网络

- 什么是URI
- URL格式?
- Http请求和响应结构?
- HTTP请求头与请求行之间是什么? 
- 什么是Cookie? Session和Cookie的区别? Cookie被禁用解决办法?
- 浏览器和Servlet通信协议?
- HTTP隧道?
- URL解码与编码?
- 常见HTTP状态码: 100, 200, 301, 302, 400, 401, 403, 404, 500, 502, 503, 504
- 301和302区别?
- HTTP状态码502与504区别?
- HTTP请求有哪些?
- post与get的区别?
- 为什么get效率高于post?
- HTTP协议? 特点?
- HTTP长连接与短连接? 非流水线与流水线?
- HTTP1.1与HTTP1.0比较? HTTP2.0与HTTP1.x比较?
- HTTP2.0 多路复用与HTTP1.X中的长连接比较?
- HTTP2.0中服务端推送?
- 一次完整的HTTP请求?
- HTTP是有状态还是无状态? 如何记住上次请求的用户?
- HTTPS交互过程? 与HTTP比较?
- SMTP, DNS, HTTPS端口号与通信协议?
- 什么是RESTful?
- 什么是token? 
- HTTP是基于TCP还是UDP? 
- TCP三次握手与四次挥手?
- TCP三次握手的必要性?
- 为什么不能进行两次握手连接?
- 为什么连接的时候是三次握手, 关闭的时候是四次挥手?
- 如果已经建立了连接, 但客户端忽然出故障了怎么办?
- TIME_WAIT与CLOSE_WAIT区别?
- TIME_WAIT为什么要等待2MSL, 可以等待1MSL吗?
- 什么是SYN攻击, 如何检测, 如何防御?
- TCP流量控制?
- 什么是流量控制? 流量控制和拥塞控制是一种东西吗?
- 滑动窗口机制?
- 拥塞避免机制?
- TCP, UDP的区别? 
- TCP, UDP的应用场景? 
- TCP可靠传输的实现? 
- TCP粘包现象? 如何解决? 
- 如何用UDP实现可靠性传输?
- UDP为什么不会发送粘包现象?
- UDP为什么采用链式传播?
- UDP有发送缓冲区吗?
- TCP, UDP, IP在传输过程中数据的最大值?
- 段, 数据包, 帧?
- TCP中keep alive与HTTP中的keep-alive区别?
- 稳定且有上限的带宽条件下, 超大文件从server传输到client端, 选择一个TCP连接快还是构建多个TCP连接快?
- TCP包结构? TCP, UDP, MAC, IP包头有多少字节?
- OSI七层模型, TCP/IP四层模型
- 如何查找域名对应IP? 
- 有网络层的存在为什么还需要传输层?
- ICMP协议? ping功能? 
- 路由功能? 分组和路由选择的区别? 什么是AS? 常用路由选择协议?
- IP地址分类
- ARP
- 数据链路层的作用?
- 浏览器从一个请求发送到返回经历过程中的优化有哪些?
- 浏览器访问一个网站的过程? 会用到哪些协议?
- CSRF和XSS区别? 各自解决方法?
- 什么是ajax?
- SOAP和REST有什么区别?
- 什么是XML?
- PV和UV区别?
- 什么是跨域, 如何解决? 
- 客户端缓存过期机制, 缓存验证?
- 数据包的流动?
- forward和redirect的区别?
- URL重写技术?
- IP寻址过程? 
- 客户端与服务端建立TCP连接三次握手前做了什么? 

---


> ## 数据库

- ER图?
- SQL与NoSQL区别?
- 数据库分表? 分片规则? 分表带来的事物问题、join查询、全局主键重复问题如何解决?
- 事物的两个特性? 
- 什么是存储过程? 与函数有什么区别和联系?
- 什么是游标?
- 什么是触发器?
- 什么是视图? 如何进行操作?
- 什么是ACID? 具体?
- 说一下一范式, 二范式, 三范式? 举例说明
- InnoDB乐观锁如何实现?
- InnoDB有多少种日志?
- MySQL中redo log与undo log区别?
- MySQL约束类型?
- MySQL有哪些语言? 
- MySQL有哪些数据类型? ip用什么类型存储? 电话号码用什么类型存储?
- MySQL连接有哪些方式? 内连接与外连接有什么区别? 默认使用什么连接?
- MySQL中exist和in的区别?
- union和union all区别?
- group by, having, where区别?
- count(\*), count(column), count(1)的区别?
- drop, truncate, delete区别?
- MySQL有哪些搜索引擎? MySQL索引有哪些? 什么是倒排索引?
- MySQL如何删除外键? 
- MySQL数据库索引原理? 
- MySQL数据库优化? 
- 聚集索引与非聚集索引区别?
- MySQL索引优化? 
- 为什么要使用索引? 索引那么多有点为什么不对表中的每一列都创建索引?
- 什么是覆盖索引?
- 索引是如何提高查询速度的?
- MySQL在哪些情况下索引会失效?
- MySQL索引使用条件? 性别适合使用索引嘛? 
- MySQL如何优化数据访问?
- 什么是最左匹配原则? 什么是联合索引?
- MySQL封锁粒度? 封锁类型? 封锁协议? 
- 什么是当前读与快照读?
- MySQL有哪些锁? InnoDb行锁有几种? 什么是死锁? 数据库死锁如何解决?
- InnoDB的行锁加什么完成?
- MySQL事物隔离级别? 各自会带来什么问题? 
- MySQL如何解决RC, RP带来的问题? 什么是MVCC?
- MySQL如何解决幻读? 
- MySQL主从复制过程? 读写分离好处? 
- InnoDB与MyISAM的区别?
- 如果数据库日志满了, 会出现什么情况?
- 如何查看慢查询?
- B+ Tree 与B Tree区别?
- B+ Tree操作过程?
- B+ Tree 与红黑树比较?
- JDBC处理事务采用什么方法?
- JDBC中getString()和getObject()区别?
- 数据库如何查询大数据
---
- Redis是数据库吗? 
- 为什么Redis是单线程还这么快? 
- Redis数据持久化如何实现?
- AOF文件过大如何解决?
- Redis如何保证原子性?
- Redis主从复制模式下, 主挂了怎么办? 
- Redis缓存更新策略?
- Redis底层数据结构(有哪些数据类型)? 跳跃表如何实现? 压缩列表是什么?
- Redis使用场景?
- 与Memcached比较?
- Redis数据淘汰策略?
- Redis如何实现事务?
- Redis复制如何实现? 什么是主从链?
- Redis切片?
- 常见的缓存策略?
- 如何防止缓存雪崩?
- 如何防止穿透?
- 什么是缓存预热?
- 什么是缓存无底洞现象?
- 如何保证缓存与数据库的双写一致性?
- MySQL数据备份与恢复

---


> ## 计算机基础

- 栈有哪些用途? 
- 原码, 反码, 补码
- 进程间的通信方式? 
- CPU占用率100%怎么查?
- 操作系统有哪些部分组成?
- 什么是大端, 小端?
- 上下文?
- 上下文切换步骤?
- 进程切换步骤?
- 进程切换一定比线程切换开销大吗?
- 引起线程上下文切换的原因?
- 程序计数器?
- PCB-切换帧?	-
- 线程调度算法?
- JVM如何实现线程调度?
- 进程调度算法?
- 死锁处理方法?
- 分页与分段的比较?
- 虚拟内存? 
- 页面置换算法?
- I/O复用
- 线程和进程的区别? 多线程和单线程的区别?
- 计算机判断是否有中断应该是什么时候? 降低进程优先级的时机?
- 实时操作系统与分时操作系统的区别?
- 中断, 异常
- 内存碎片如何解决?

---


> ## 分布式

- 集群、分布式、微服务区别?
- 微服务的优点与缺点?
- 分布式锁的实现?
- CAP理论? BASE理论?
- 2PC, 3PC? 
- 什么是RMI? 什么是RPC?
- RPC与REST区别?
- 什么是一致性哈希?
- 反向代理与CDN加速的区别?
- 大型网站核心架构要素?
- 网站性能测试的主要指标?
- 性能测试包括哪些? 
- Web前端性能优化?
- 应用服务器性能优化?
- 典型的网站分层架构?
- 如何实现应用层高可用?
- 应用服务的Session如何管理?
- 如何实现高可用服务器?
- 如何实现高可用数据?
- 如何实现网站的可伸缩性?
- 什么是负载均衡? 有哪些实现方式? 
- 四层负载均衡与七层负载均衡? 二层负载均衡? 三层负载均衡?
- LVS? LVS-NAT? LVS-DR? LVS-Tun? Lvs-FULLNAT?
- Nginx与LVS比较?
- 正向代理和反向代理?
- Nginx负载均衡策略?
- 网站攻击方式?
- 如何实现服务限流(有哪些限流策略)?
- 分布式事务解决方案?
- 如何实现单点登录?
---
- 什么是zookeeper? 原理? session, ZNode, 版本, 顺序访问
- 什么是Dubbo? 框架图? 有哪些节点角色? 
- kafka?
- Hbase?
- springCloud与Dubbo区别?
- springCloud基本功能?
- Eureka? 可以被什么替代? 与zookeeper比较? 还有哪些注册服务? zookeeper可以实现负载均衡嘛?
- Ribbon负载策略?
- Hystrix容错实现方式? 熔断、资源隔离、降级. 限流?
- Alibaba Sentinel 熔断降级方式?
- Feign?
- 网关服务? 什么是网关?
- 配置中心? SpringCloud Bus?
- zipkin? +
- 微服务设计准则?
- 如何保证幂等性?
- RabbitMQ?
- 为什么使用RabbitMQ? 如何保证消息正确发送? 如何保证消息接收方消费了消息? 如何避免消费重复投递或重复消费? 基于什么传输? 消息如何分发? 如何保证消息可靠传输? 如何保证消息顺序性?
- 使用消息队列的好处? 使用消息队列会带来什么问题?

---


> ## 算法

- 算法定义?
- 你了解大O吗? 你能给出不同数据结构的例子吗?
- 如何权衡使用有序数组还是无序数组?
- 五大基础算法? 
- 红黑树? 
- BitMap如何实现? 有哪些应用? 什么是布隆过滤?
- RSA算法?
- 动态规划的三个概念?
- 什么是前缀树? 应用?
- 对称加密和非对称加密? 
- 各种排序算法时间复杂度与空间复杂度比较? 冒泡、交换、选择、插入、基数、希尔、快排、归并、堆
- 二叉树中两个节点的公共祖先?
- 从100亿条记录中找出重复数最多的前10条?
- 一个文本行, 大约有一万行, 每行一个单词, 要统计最频繁的前10个?
- 100万个数中找出最大的100个数?
- 动态规划与贪心算法的区别

---


> ## 设计模式

- 设计模式分为几大类?
- 说一说有哪些设计原则?
---
- 懒汉与饿汉区别? 实现单例模式的方法?
- 单例模式有什么特点? 应用场景?
- 工厂模式有哪些? 之间的区别(三种工厂模式的比较)?
- 生成器/建造者(Builder)
- 原型模式
---
- 责任链模式
- 命令模式
- 解释器
- 迭代器
- 中介者
- 备忘录
- 观察者
- 状态
- 策略
- 模板
- 访问者
- 空对象
---
- 适配器
- 桥接模式
- 装饰器
- 外观模式/门面模式(Facede)
- 享元模式(Flyweight)
- 代理模式
---


> ## 框架

- Maven特点? 
- Solr是什么?
- Thymeleaf是什么?
- 什么是webService? +
---

> ## JSP

- JSP有哪些动作?
- 会话跟踪技术?
- JSP内置九大类型?
---

> ## MyBatis

- MyBatis中#{}和${}的区别? 
- PreparedStatement与Statement区别?
- Mybatis缓存?
- 什么是MyBatis? 
- 当实体类的属性名和表中的字段名不一样, 怎么办? 
- 通常一个Xml映射文件, 都会写一个Dao接口与之对应, 请问, 这个Dao接口的工作原理是什么? Dao接口里的方法, 参数不同时, 方法能重载吗? 
- MyBatis如何实现分页? 分页插件的原理?
- 如何获取插入数据id? 
---

> ## spring

- Spring有哪些特点? 
- Spring核心?
- Spring中的IOC有几种注入方式?
- Spring提供哪些配置方式?
- 什么是IOC/DI,什么是AOP? AOP的实现方式? 
- Spring IOC 容器初始化过程?
- 为什么用Spring IOC 而不用工厂模式?
- Spring事物的传播级别?
- Spring中的事物隔离级别?
- Spring中Bean的Scope作用域? 
-  什么是Spring Bean? 
- SpringMVC路由怎么写? 
- SpringMVC如何接受ajax?
- SpringMVC用到了那个核心servlet? 
- SpringMVC核心控制器是什么? 请求流程?
- SpringBoot优点?
- 关于加@Transactional注解的方法之间调用, 事物是否生效?
- Bean的生命周期?
- Spring用了哪些设计模式?
- Spring三大核心组件?
- Spring框架中的单例Beans是线程安全的么? 
- Spring如何处理线程并发问题? 
- SpringMVC如何区分post和get?
- Spring中@Autowrited与@Resource的区别? 
- Spring中的@RestController, @RequestBody, @Controller, @ResponseBody有什么用
- 过滤器与拦截器的区别?
---


> ## Linux

- Linux文件和目录操作
- 创建文件, 查看文件
- 创建目录
- 监测程序
- ps和top的区别
- 压缩数据
- 结束进程
- 压力测试衡量CPU的三个指标? 
- Linux下查看80端口是否被占用
- 查看内存 
- 查看磁盘
- 创建一个新用户
- 文件权限
- 备份
- 你知道库函数和内核调用吗?  

---


> ## Python

- Pyton垃圾回收策略? 
- MVC与MVT模式? 
- 什么是wsgi?uwsgi?
- Django请求生命周期?
- 什么是FBV, CBV?
- Django模板中自定义filter与simple_tag区别?
- Flask与Django区别?
---


> ## 测试

- 对软件测试的理解?
- 一个完整的测试应有哪些阶段组成?
- 单元测试怎么实现?
- 测试用例元素
- 好的测试用例应该从哪些方面考虑
- 软件测试有什么策略和阶段
- 回归测试和冒烟测试
- 软件测试类型
- 用例策略
- 测试用例是什么? 有什么作用?
- 软件缺陷定义
- 缺陷中应该包含什么? 严重等级一般有哪些?
- 给你一个杯子你会怎样测试?
- 测试报告应该包含哪些?
- 测试中出现BUG开发不承认, 你会怎么办? 
- 模拟铁路局卖火车, 假设有一条高铁线路, 途径多个城市, 火车上共5000个座位. 请设计一个数据结构, 以检查在某乘车区间内购票是否有座位的方法
- "3-5-8" 原则

> ## 其他

- 虚拟化技术? 
- 赛马, 有25匹马, 每次只能5匹马比赛, 比赛只能得到5匹马之间的快慢, 而不是速度.请问, 最少比赛多少次, 才能获得最快的前3匹马?
- SSH协议? 什么是跳板机?
- thinkPHP处理流程?
- 敏捷开发与瀑布开发的区别?
---


> ## 项目

- 项目需求
- 项目实现
- 项目问题, 项目如何解决
- 项目中的优化

> ## 综合面

- 为我介绍?
- 优缺点?
- 投简历的时候选择什么样的公司?
- 薪资
- 工作地点
- 对加班看法
- 职业规划?
- 你的人生规划怎样的? 
- 平时如何学习, 如何做项目?
- 遇到什么困难? 困难如何解决?
- 你觉得你做项目时最大的收获是什么? 
- 如何评价公司的?

> ## 提问

- 公司的研发团队目前是什么规模? 开发、测试分别有多少人? 
- 现在部门业务方向? 
- 如果我有幸能够进入你们部门,  请问到时候是先进行培训还是直接上手项目呢?
- 进入部门之后做的项目是针对某一方向还是看实际接手的项目不固定的那种?
- 晋升制度
---

