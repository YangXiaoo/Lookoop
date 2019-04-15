### [1] “a==b”和 “a.equals(b)” 有什么区别？
如果a与b都是对象，则a==b比较的是对象的引用，只有两个对象都指向堆中同一对象才能返回true; 而a.eauqls(b)为逻辑比较，一般需要重写比如String类重写equals方法来比较两个不用对象但包含相同字母的比较。

------------

### [2] java中的引用
**目的**：一是可以通过代码的方式决定某些对象生命周期；二是有利于JVM进行垃圾回收
java中的引用包括**四种**引用
- **强引用**：是指创建一个对象并把这个对象赋给一个引用变量。在程序内存不足（OOM）的时候也不会被回收。
- **软引用**(SoftReference)： 软引用在程序内存不足时，会被回收，使用方式
```java
// 注意：wrf这个引用也是强引用，它是指向SoftReference这个对象的，
// 这里的软引用指的是指向new String("str")的引用，也就是SoftReference类中T
SoftReference<String> wrf = new SoftReference<String>(new String("str"));
```
- **弱引用**(WeakReference): 被弱引用关联的对象在JVM进行垃圾回收时总会被回收
```java
WeakReference<String> wrf = new WeakReference<String>(str);
```
- **虚引用**(PhantomReference): 在回收之前会被放入ReferenceQueue中，而其它引用是被JVM回收后才被传入ReferenceQueue中。大多被用于引用销毁前的处理工作。
```java
PhantomReference<String> prf = new PhantomReference<String>(new String("str"), new ReferenceQueue<>());
```

----
### [3] 你能保证GC执行吗
不能，虽然你可以调用 **System.gc()** 或者 **Runtime.gc()**，但是没有办法保证 GC 的执行。

------------
### [4] [throw和throws有什么区别](https://www.cnblogs.com/xiohao/p/3547443.html "throw和throws有什么区别")
- throw : 抛出一个异常
- throws: 抛出一个异常声明

throw出现在函数体；throws出现在方法函数头
执行throw则一定抛出了异常；throws表现出一种异常的可能性，但不一定会发生这些异常

----
### [5] 处理完异常后，Exception对象会发生什么变化?
会在下一个垃圾回收过程中被回收掉

----
### [6] 什么是可变对象和不可变对象？
不可变对象指对象一旦被创建，状态就不能再改变。任何修改都会创建一个新的对象，如String, Integer及其包装类。

---
### [7] 运算符
- 0xaa, 0x表示十六进制
- \>>>>: 无符号右移，与有符号右移(>>)的区别在于无符号右移不管为正还是为负都补0

---
### [8] java中用什么数据类型来代表价格？
如果不是特别关心内存和性能用**BigDecimal**， 否则使用预定义精度**double**类型

---
### [9] [哪个类包含 clone 方法？是 Cloneable 还是 Object？](https://blog.csdn.net/zhangyuan19880606/article/details/51240975 "哪个类包含 clone 方法？是 Cloneable 还是 Object？")
java.lang.Cloneable 是一个标示性接口，不包含任何方法，clone 方法在 object 类中定义。并且需要知道 clone() 方法是一个本地方法，这意味着它是由 c 或 c++ 或 其他本地语言实现的。

clone是**浅拷贝**-只克隆对象本身以及它所包含的所有对象引用地址
**深拷贝**-克隆自身以及它所包含的所有对象应用地址

---
### [10]  a = a + b 与 a += b 的区别?
+= 隐式的将加操作的结果类型强制转换为持有结果的类型。如果两这个整型相加，如 byte、short 或者 int，首先会将它们提升到 int 类型，然后在执行加法操作。如果加法操作的结果比 a 的最大值要大，则 a+b 会出现编译错误，但是 a += b 没问题，如下：
```java
byte a = 127;
byte b = 127;
b = a + b;  // error : cannot convert from int to byte
b += a;     // ok
```

---
### [11] 我能在不进行强制转换的情况下将一个 double 值赋值给 long 类型的变量吗？
不能，因为double类型范围比long类型更广，所以必须进行强制转换。

---
### [12] 3*0.1 == 0.3 将会返回什么？true 还是 false？
false, 因为有些浮点数不能完全精确的表示出来。与c++一样

---
### [13] int 和 Integer 哪个会占用更多的内存？
Integer 对象会占用更多的内存。Integer 是一个对象，需要存储对象的元数据。但是 int 是一个原始类型的数据，所以占用的空间更少。

---
### [14] 为什么 Java 中的 String 是不可变的（Immutable）？
Java 中的 String 不可变是因为 Java 的设计者认为字符串使用非常频繁，将字符串设置为不可变可以允许多个客户端之间共享相同的字符串。

---
### [15] Java集合类框架的基本接口有哪些？
Collection, Set, List, Map

---
### [16]  ArrayList和数组(Array)和有什么区别？什么时候应该使用Array而不是ArrayList？
- Array可以容纳基本类型和对象，而ArrayList只能容纳对象。
- Array是指定大小的，而ArrayList大小是固定的。
- Array没有提供ArrayList那么多功能，比如addAll、removeAll和iterator等
- 假如元素的大小是固定的，而且能事先知道，我们就应该用Array而不是ArrayLis

---
### [17] [Comparable与Comparator的区别？](https://www.cnblogs.com/sunflower627/p/3158042.html "Comparable与Comparator的区别？")
都是接口用来自定义class比较大小，Comparable定义在class内部，Comparator定义在外部。
```java
public class Person implements Comparable {
    String name;
    int age;
    public int compareTo(Person another) {
        int i = 0;
        i = name.compareTo(another.name);
        if (i == 0) {
            return age - another.age;
        } else {
            return 1;
        }
    }
    public static void main() {
        // 实现personList省略
        Collections.sort(personList);
    }
}
```
使用Comparator

```java
public class Person{
     String name;
     int age;
}
class PersonComparator implements Comparator { 
     public int compare(Person one, Person another) {
          int i = 0;
          i = one.name.compareTo(another.name); // 使用字符串的比较
          if(i == 0) { // 如果名字一样,比较年龄,返回比较年龄结果
               return one.age - another.age;
          } else {
               return i; // 名字不一样, 返回比较名字的结果.
          }
     }
}
//  Collections.sort( personList , new PersonComparator()) 可以对其排序
```

---
### [18] ArrayList 和 HashMap 的默认大小是多数？
在 Java 7 中，ArrayList 的默认大小是 10 个元素，HashMap 的默认大小是16个元素（必须是2的幂）

---
### [19]  什么时候使用字节流，什么时候使用字符流?
所有的输入都是转换成字节流之后，然后在内存中变成字符流。所以一般建议使用字符流。但是遇到中文汉字，出现乱码的情况下，可以使用字节流。

在所有的硬盘上保存文件或进行传输的时候都是以字节的方法进行的，包括图片也是按字节完成，而字符是只有在内存中才会形成的，所以使用字节的操作是最多的。我们建议尽量尝试使用字符流，一旦程序无法成功编译，就不得不使用面向字节的类库，即字节流。

---
### [20] 把包括基本类型在内的数据和字符串按顺序输出到数据源，或者按照顺序从数据源读入，一般用哪两个流?
DataInputStream DataOutputStream

---
### [21]  把一个对象写入数据源或者从一个数据源读出来,用哪两个流?
ObjectInputStream ObjectOutputStream