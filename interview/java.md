## Java基础知识问答
#### java关键字与保留字？goto,const?false,true,null,inner?
### String能被继承吗？
### string,StringBuffer,StringBuilder区别?
### 数组定义：String a[10]; 正不正确？数组等号左边能不能出现数字?
### System.out.println(25 + "" + 10 + 5);输出什么？
### String.replaceAll(old, new);其中old是什么形式?
### 引用类型为null，能否找到其所属的静态类型?
### switch参数可以有哪些类型?
### Object有哪些方法?
### 构造方法可以有哪些访问修饰符?
### 分析count = count++;
### Math.ceil(),Math.floor();
### Java平台无关性与哪些有关?
### 运算符优先级?
### lambda表达式的作用?形参列表、代码块？优点与缺点?
### 解释一下Serialization和Deserialization？
### 多态定义?抽象定义？
---
## Java高级应用
### JDBC使用什么设计模式?
### 类之间存在哪些关系？
### 一般关系型和对象数据模型之间的对应关系?
### 一个类可以同时继承和实现其它类吗?有没有先后顺序?
### JRE判断程序是否执行结束的标准是什么?
### 解释一下驱动在JDBC中的角色?
### class.forName()有什么作用?
### PreparedStatement与Statement区别?
### 什么是RMI？
### 什么是servlet?
### servlet生命周期?
### 服务端包含?
### 什么是servlet链?
### servlet安全性？
### 为什么实现equals必须重新hashcode?
---
## 集合问题
### 为什么集合没有实现Cloneable和Serializable?
### Iterator和ListIterator区别？
### 快速失败(fail-fast)和安全失败(fail-safe)区别？
### 数组和列表有什么区别？如何选择
### ArrayList与LinkedList区别？底层原理?ArrayList扩容、删除如何实现?
### 用过哪些Map类，都有神马区别？HashMap实现过程（JDK1.8）？put,resize等实现过程？
### HashMap链表插入是头插入还是尾插入？头插入会造成什么问题？
### Enumeration接口和Iterator接口的区别?
### HashSet,TreeSet,LinkedHashSet之间的区别?
### 阻塞队列，ArrayBlockingQueue, LinkedBlockingQueue, PriorityBlockingQueue, DelayQueue, SynchronousQueue各自特点？非阻塞队列？

---
## 线程
### 如果一个线程构造了一个不可变对象，就可以保证这个对象被其它程序正确查看吗？
### 线程调用过程?
### 数据库连接池与线程池?
### 线程池ThreadPoolRxecutor有哪些参数？
### 线程池中线程任务书数超过核心数会发生什么？阻塞队列大小？
### Synchronized与Lock比较（锁与同步锁的比较）？
### ReentrantLock如何实现可重入？如何实现公平锁与非公平锁？
### 在监视器内部如何做到线程同步？程序应该用哪种级别的同步？synchronized如何实现可重入（底层）？
### 线程池设置大小与CPU的关系？
### 介绍一下AQS？
### Thread中join()方法的原理？
### synchronized锁的范围？
### ThreadLocal内存泄露？如何解决？
---
## JVM虚拟机与JMM内存模型
### JMM内存模型中的规定了哪八种操作？什么是重排序？
### 类加载顺序，机制？有什么优势？
### 堆上的内存如何释放，栈上的内容如何释放？
### Java内存泄露的最直接表现?
### 如果对象的引用被置为null，垃圾回收器是否会立即释放该对象占用的内存?
### Java中对象什么时候可以被垃圾回收?
### JVM如何确定一个对象是不是有引用？
### 永久代会发生垃圾回收吗？
### GC Roots包含哪些？
### 什么时候新生代会发生GC？老年代发生GC条件？
### JRE判断程序是否结束的标准?
### String s = new String("abc");创建了几个对象？
### CAS机制？包含哪些操作？会产生哪些问题？如何避免ABA问题？
### 什么是原子操作？什么是内存屏障？
### volatile实现原理？
### JVM中大对象被分配到哪里？长期存活对象进入哪里？什么是空间分配担保？
### 什么是happens-before(先发行为原则)?

---
## 框架
### Maven特点？
---
## JSP
---
## MyBatis
### MyBatis中#{}和${}的区别？
---
## spring
### sprig有哪些特点？
### 什么是IOC/DI,什么是AOP？
### spring事物的传播级别?
### spring中Scope作用域？
### springMVC路由怎么写？
### springMVC如何接受ajax?
### springMVC用到了那个核心servlet？
### SpringBoot优点?
### 关于加@Transactional注解的方法之间调用，事物是否生效？
### Bean的生命周期？
---
## 其他
### 对软件测试的理解?
### Pyton垃圾回收策略？
### 虚拟化技术？
### 对称加密和非对称加密？
---
## 计算机网络
### Http请求和响应结构?
### HTTP请求头与请求行之间是什么？
### 什么是Cookie?Session和Cookie的区别?Cookie被禁用解决办法?
### 浏览器和Servlet通信协议?
### HTTP隧道?
### URL解码与编码?
### 什么是RESTful?
### 什么是token？
### HTTP是基于TCP还是UDP？
### TCP,UDP的应用场景？
### HTTP是有状态还是无状态？如何记住上次请求的用户？
### 如何查找域名对应IP？
### 路由功能？分组和路由选择的区别？什么是AS？常用路由选择协议？
### 浏览器从一个请求发送到返回经历过程中的优化有哪些？
---
## 计算机基础
### 栈有哪些用途？
### 进程间的通信方式？
---
## 数据库
### Mysql约束类型?
### Mysql有哪些语言？
### Mysql有哪些搜索引擎？
### 事物的两个特性？
### 数据库分表？分片规则？分表带来的事物问题、join查询、全局主键重复问题如何解决？
### 数据库索引原理？
### 数据库优化？
### 索引优化？索引优缺点？
### Mysql索引有哪些？
### Mysql在哪些情况下索引会失效?
### 性别适合使用索引嘛？
### Mysql有哪些锁？InnoDb行锁有几种？什么是死锁？数据库死锁如何解决？
### Mysql事物隔离级别？各自会带来什么问题？
### 如何解决RC,RP带来的问题？什么是MVCC?
### 如何解决幻读？
### Mysql中exist和in的区别？
---
### Redis是数据库吗？
### 为什么Redis是单线程还这么快？
### Redis数据持久化如何实现？
###  Redis主从复制模式下，主挂了怎么办？
### Redis缓存更新策略?
### redis底层数据结构？跳跃表如何实现？压缩列表是什么？
---
## 分布式
### 什么是zookeeper?
### 什么是Dubbo?
---
## 算法
### 你了解大O吗？你能给出不同数据结构的例子吗?
### 如何权衡使用有序数组还是无序数组?
### 五大基础算法？
---
## 设计模式
### 四种单例模式的实现？
