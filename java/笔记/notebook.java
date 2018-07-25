// java笔记
// 2018-7-6
// 杨潇

1. 对象
	1）句柄
		String s; //创建句柄时需要初始化
		String s = "abc"
		String s = new String("abc")

2. 存储位置
	1）寄存器
		最快的保存区域，处理器内部，寄存器是根据需要由编译器分配，没有直接的控制权限，也不可能在程序中找到寄存器存在的痕迹。
	2）栈堆
		驻留于常规RAM(随机访问存储器)内，通过堆栈指针获得处理，堆栈指针向下移创建新的内存，向上移动，释放内存。
	3）堆
		一种常规用途的内存池也在RAM中，保存了java对象。在堆里分配存储空间会花掉更长时间。
	4）静态存储
		也在RAM中，位于固定位置。程序运行时，静态存储的数据随时等待调用。用 Static关键字指定一个对象的特定元素是静态的。JAVA对象本身永远也不会置于静态存储空间。
	5）常数存储
		通常直接置于程序代码内部，可将它置入只读存储器(ROM)
	6) 非RAM存储
		完全独立于程序之外，程序不允许时也存在，并在程序的控制范围之外。流式对象：对象会变成字节流，通常会发给另一台机器。固定对象：对象存在磁盘中，程序终止时可以保持对象类型不变。

3. 主要类型 Primitive
	程序设计时频繁使用，由于new对象存在堆中，并不是非常有效，所以用 Primitive 将其置于堆栈中，能够高效地存储。

	
4. 数据类型

	基本类型：boolean 二进制位数：1位
	包装类型：Boolean

	基本类型：byte 二进制位数：8
	包装类：java.lang.Byte
	最小值：Byte.MIN_VALUE=-128
	最大值：Byte.MAX_VALUE=127

	基本类型：short 二进制位数：16
	包装类：java.lang.Short
	最小值：Short.MIN_VALUE=-32768
	最大值：Short.MAX_VALUE=32767

	基本类型：int 二进制位数：32
	包装类：java.lang.Integer
	最小值：Integer.MIN_VALUE=-2147483648
	最大值：Integer.MAX_VALUE=2147483647

	基本类型：long 二进制位数：64
	包装类：java.lang.Long
	最小值：Long.MIN_VALUE=-9223372036854775808
	最大值：Long.MAX_VALUE=9223372036854775807

	基本类型：float 二进制位数：32
	包装类：java.lang.Float
	最小值：Float.MIN_VALUE=1.4E-45
	最大值：Float.MAX_VALUE=3.4028235E38

	基本类型：double 二进制位数：64
	包装类：java.lang.Double
	最小值：Double.MIN_VALUE=4.9E-324
	最大值：Double.MAX_VALUE=1.7976931348623157E308

	基本类型：char 二进制位数：16
	包装类：java.lang.Character
	最小值：Character.MIN_VALUE=0
	最大值：Character.MAX_VALUE=65535


	默认值：
	Boolean false
	Char '\u0000'(null)
	byte (byte)0
	short (short)0
	int 0
	long 0L
	float 0.0f
	double 0.0d

5. 返回

	int storage(String s)
	{
		return s.length()*2;
	}

6. 函数命名
	类大写开始，连续单词首字母大写
	函数名称首字母小写，连续单词各首字母大写

7. 注释
	javadoc只能为Public和protected成员处理注释文档。
	1）@see 引用其他类
		允许引用其他类里的文档
	2）@version 
		@version 版本信息
	3）@author 作者信息
	4）@param 参数名 说明
	5）@return 说明
	6）@exception 完整类名 说明
	7）deprecated
		表示一些功能已由改进过的新功能取代。建议用户不必再使用一种特定的功能，因为改进后可能会摒弃。

	例子：
	/** The first java program.
	  * Display string.
	  * @author Yauno
	  * @author http://www.xxx.com
	 */

	public class HelloWorld {
		/** Hello World
		  * @param String 
		  * @return No return Value
		  * @exception exceptions No exception thrown
		 */
	    public static void main(String []args) {
	        System.out.println("Hello world");
	        try {
	        	Thread.currentThread().sleep(5 * 1000);
	        }
	        catch(InterruptedException e) { }
	    }
	}

8. 方法调用中的别名处理
	class Leter {
		char c;
	}

	public class PassObject {
		static void f(Leter y) {
			y.c = "z";
		}

		public static void main(String[] args) {
			Leter x = new Leter();
			x.c = 'a';
			System.out.println("x.c:" + x.c);
			f(x);
			System.out.println("x.c:" + x.c);
		}
	}

	// x.c : a
	// x.c : z

9.随机数
	Random rand = new Random()
	rand.nextInt(),rand.nextLong(),rand.nextFloat(),rand.nextDouble()

10. 三元运算
	t = i < 10 ? i * 10 : i * 2;

11. label 标签
	label标签在循环前面
	列：
	
	out:
	for (; true; ) {
		inner:
		for (int i = 0; i < 10; i++) {
			if (i == 2):
				continue inner;
			if (i == 6) {
				break out;
			}
		}
	}


12. 变量类型
	int a,b,c;
	byte z = 22;
	String s = 'ss';
	double pi = 3.1415;
	char x = 'x';


13. 局部变量
	局部变只在声明他的方法、构造方法或语句块中可见; 局部变量是在栈上分配的; 局部变量没有默认值，必须经过初始化才可以使用。

14. 装饰符
	1) private : 通过 this.xx 来使用
		public class Looger {
			private String format;
			public String getFormat() {
				return this.format;
			}

			public void setFormat() {
				this.format = format;
			}
		}

	2) public 共有访问
		被声明为 public 的类、方法、构造方法和接口能被任何其他类访问。

	3) protected 受保护的访问装饰符

15. Number & Math
	int x = 6;
	String s = 'ss';
	double a = 1.4;
	x.byteValue();
	x.ComparableTo(2); //相等返回0; 小于参数返回-1; 大于返回1

	// valueOf(int i)
	// valueOf(String s)
	// valueOf(String s, int radix) // radix 指定进制数
	Integer n = Integer.valueOf(9); // 9
	Double y = Double.valueOf(5); // 5.0
	Float z = Float.valueOf("80"); // 80.0


	x.toString();

	// parseInt()
	s.parseInt();

	Math.abs(a);

	// 返回大于等于指定参数的最小值
	Math.ceil(a);
	// 返回小于等于指定参数的最小值
	Math..floor(a);
	// 返回与参数最接近的整数，返回类型为double
	Math.rint(a);
	Math.round(a);
	Math.min(a,x);
	Math.pow(a,x);
	Math.sqrt(a,x);
	Math.toDegrees(x);
	Math.random();


16. Character

	// 原始字符串装箱到Character对象ch中
	Character ch = 'a';

	// 原始字符串用 test 方法装箱，返回拆箱的值到c
	char c = test('x');

	// 方法

	Character.isLetter('3'); // false
	Character.isDigit('c'); // false
	Character.isWhitespace(' '); // true
	Character.isUpperCase('E'); // true
	Character.isLowerCase('c'); // true
	Character.toUpperCase('c'); // 'C'
	Character.isLetterOrDigit(tail)
	Character.toLowerCase('E'); // 'e'

17. String
	
	String s = "Yauno";
	String c = "Yauno123";
	String n = "yAUNO";
	char res = s.charAt(1); // 'a'
	int res = s.compareTo(c); // 返回差值；小于则返回小于0；等于返回0
	int res = s.compareToIgnoreCase(n);
	String res = s.concat(c);
	int index = s.indexOf('0');
	int lastindex = s.lastindexOf('n'); // lastindexOf(int ch, int fromIndex) 第二个参数为从指定位置开始搜索，默认为最后一位
	int leng = s.length();
	String r = s.replace('o', 'Y'); // YaunY
	s.matches("Y(.*)");
	s.replaceAll("(.*)n(.*)", "YY"); // "YY"
	String replaceFirst(String regex, String replacement)

	String[] split(String regex, int limit) // limit默认为全分割

	String s = new String("Y-X-y-x");
	s.split("-", 2) // ["Y","X-y-x"]

	s.startWith('Y') // true

	s.subSequence(1,3); // "-X-"


	String substring(int beginIndex, int endIndex) // 包含起始位置，不包括结束索引位置

	char[] toArray()
	n.toArray(); // ["y","A","U","N","O"]

	n.toLowerCase(); // "yauno"
	n.toUpperCase(); // "YAUNO"

	String m = new String("   xbb   ");
	m.trim(); // "xbb"

18. StringBuffer & StringBuilder
	和 String 类不同的是，这两个类的对象能够被多次修改并且不产生新的未使用对象。
	StringBuffer 速度弱于 StringBuilder,但线程安全时喜不适用 StringBuffer 

	StringBuffer s = new StringBuffer("yauno");
	public StringBuffer append(String s)
	public StringBuffer reverse()
	public delete(int start, int end)
	public insert(int offset, int i)
	replace(int start, int end, String s)

19. 时间
	Date date = new Date();
	date.toString();

20. 可变参数
	typeName... parameterName

21. 文件流操作

	1) 写入读出文件
	import java.io.*;

	public class Files {
	    public static void main(String []args) throws IOException {
	        System.out.println("文件流操作");

	        // 创建test.txt文件
	        File f = new File("test.txt");

	        // 构建FileOutputStream对象，文件不存在会自动创建
	        FileOutputStream fout = new FileOutputStream(f);

	        // 构建OutputStreamWriter对象，参数可以指定编码，默认操作系统编码，windows上市gbk
	        OutputStreamWriter writer = new OutputStreamWriter(fout, "UTF-8");

	        // 写入到文件
	        writer.append("中文输入保存到文件test.txt中");
	        writer.append("\r\n");
	        writer.append("English");

	        // 关闭写入流
	        writer.close();

	        // 关闭输出流
	        fout.close();

	        FileInputStream fin = new FileInputStream(f);
	        InputStreamReader reader = new InputStreamReader(fin, "UTF-8");

	        StringBuffer sb = new StringBuffer();
	        while (reader.ready()) {
	        	// 转换成char加入到StringBuffer对象中
	        	sb.append((char) reader.read());
	        }

	        System.out.println(sb.toString());

	        reader.close();
	        fin.close();
	    }
	}

	2） 创建文件夹

	String dirname = "test1.txt";
	File dir = new File(dirname);
	d.mkdirs();

	// 检测是否为目录
	dir.isDirectory();
	String s[] = dir.list();


22. 构造器
	构造器不能被继承，不是函数。继承时，用 super 调用父类构造器。


	public class Human {
		String name;

		Human(String input) {
			name = input;
		}

		Human() {
			this("Yauno");
		}

		public static void main(String[] args) {
			Human h1 = new Human("YY");
			Human h2 = new Human();
		}
	}

23. 重写 与 重载
	参数列表必须与被重写方法相同; 父类成员方法只能被它的子类重写; 声明为 final 的方法不能被重写; 构造方法不能被重写; 
	方法名与参数一样为重写 Override, 方法名相同，参数不同为 Overloading；

24. 多态
	多态是一个行为具有多个不同表现形式或形态的能力，多态就是同一个接口使用不同的实例而执行的不同操作。同一件事情发生在不同的对象上会产生不同的结果 。
	优点：消除类型之间的耦合性，可替换性，可扩充性，接口性，灵活性，简化性
	多态存在的三个必要条件：继承，重写，父类引用指向子类对象。

25. 泛型

	泛型三种：
	          [1]ArrayList<T> al=new ArrayList<T>();指定集合元素只能是T类型
	          [2]ArrayList<?> al=new ArrayList<?>();集合元素可以是任意类型，这种没有意义，一般是方法中，只是为了说明用法
	          [3]ArrayList<? extends E> al=new ArrayList<? extends E>();
	            泛型的限定：
	               ? extends E:接收E类型或者E的子类型。
	               ？super E:接收E类型或者E的父类型。

26. List 列表
	https://www.cnblogs.com/111testing/p/6602603.html
	List:元素是有序的(怎么存的就怎么取出来，顺序不会乱)，元素可以重复（角标1上有个3，角标2上也可以有个3）因为该集合体系有索引，

	ArrayList：底层的数据结构使用的是数组结构（数组长度是可变的百分之五十延长）（特点是查询很快，但增删较慢）线程不同步

	LinkedList：底层的数据结构是链表结构（特点是查询较慢，增删较快）
	Vector：底层是数组数据结构 线程同步（数组长度是可变的百分之百延长）（无论查询还是增删都很慢，被ArrayList替代了）
	List接口的常用实现类有ArrayList和LinkedList，在使用List集合时，通常情况下声明为List类型，实例化时根据实际情况的需要，实例化为ArrayList或LinkedList，例如：
	List<String> l = new ArrayList<String>();// 利用ArrayList类实例化List集合
	List<String> l2 = new LinkedList<String>();// 利用LinkedList类实例化List集合

	// 实例
	String a = "A", b = "B", c = "C";
	List<String> list = new LinkedList<String>();
	list.add(a);
	list.size(); // int[] s  --->  s.length;
	list.contains("a,b,c");
	list.clear();
	list.set(1, b);// 将索引位置为1的对象e修改为对象b
	list.add(2, c);// 将对象c添加到索引位置为2的位置
	for (int i = 0; i < list.size(); i++) {
	System.out.println(list.get(i));// 利用get(int index)方法获得指定索引位置的对象
	}

27. Queue
	https://www.cnblogs.com/lemon-flm/p/7877898.html
	Queue: FIFO 数据结构，与 Set, List 同一级别，都是继承 Collection, 用 LinkedList 实现 Queue 接口

	列队的方法，不全都是 Queue 的
　　add      增加一个元索                     如果队列已满，则抛出一个IIIegaISlabEepeplian异常
　　remove   移除并返回队列头部的元素    如果队列为空，则抛出一个NoSuchElementException异常
　　element  返回队列头部的元素             如果队列为空，则抛出一个NoSuchElementException异常
　　offer    添加一个元素并返回true       如果队列已满，则返回false
　　poll     移除并返回队列头部的元素    如果队列为空，则返回null
　　peek     返回队列头部的元素             如果队列为空，则返回null
　　put      添加一个元素                      如果队列满，则阻塞
　　take     移除并返回队列头部的元素     如果队列为空，则阻塞

	remove、element、offer 、poll、peek,isEmpty() 其实是属于Queue接口。 
28. Deque
	https://www.cnblogs.com/bushi/p/6681543.html
	修饰符和返回值	方法名	描述
	添加功能
	void	push(E)	向队列头部插入一个元素,失败时抛出异常 
	void	addFirst(E)	向队列头部插入一个元素,失败时抛出异常
	void 	addLast(E)	向队列尾部插入一个元素,失败时抛出异常
	boolean 	offerFirst(E)	向队列头部加入一个元素,失败时返回false
	boolean 	offerLast(E)	向队列尾部加入一个元素,失败时返回false
	获取功能
	E	getFirst()	获取队列头部元素,队列为空时抛出异常
	E 	getLast()	获取队列尾部元素,队列为空时抛出异常
	E 	peekFirst()	获取队列头部元素,队列为空时返回null
	E 	peekLast()	获取队列尾部元素,队列为空时返回null
	删除功能
	boolean	removeFirstOccurrence(Object)	删除第一次出现的指定元素,不存在时返回false
	boolean 	removeLastOccurrence(Object)	删除最后一次出现的指定元素,不存在时返回false
	弹出功能
	E	pop()	弹出队列头部元素,队列为空时抛出异常
	E	removeFirst()	弹出队列头部元素,队列为空时抛出异常
	E 	removeLast()	弹出队列尾部元素,队列为空时抛出异常
	E 	pollFirst()	弹出队列头部元素,队列为空时返回null 
	E 	pollLast()	弹出队列尾部元素,队列为空时返回null 

	同Queue一样Deque的实现也可以划分成通用实现和并发实现.通用实现主要有两个实现类ArrayDeque和LinkedList.
29. HashMap
	HashMap<String, Integer> map = new HashMap<>();
	map.put("sss", 1);
	map.containsKey(xx);
	map.constains(xx);
	map.remove(xx);

30. Set
	Set<ListNode> set = new HashSet<>();
	set.contains(xx);
	set.remove(xx);
	set.add(xx)

31. Stack
	Stack<Integer> stack = new Stack<>();
	stack.push(xx);
	stack.pop(xx);