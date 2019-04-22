// java笔记

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

	Long.parseLong(String)
	String.valueOf(int)

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

	12.1 转换
		string 和int之间的转换
		string转换成int  :Integer.valueOf("12")
		int转换成string : String.valueOf(12)


		char和int之间的转换
		首先将char转换成string
		String str=String.valueOf('2')
		Integer.valueof(str) 或者Integer.PaseInt(str)
		Integer.valueof返回的是Integer对象，Integer.paseInt返回的是int

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

16.1. String
	
	String s = "Yauno";
	String c = "Yauno123";
	String n = "yAUNO";
	char res = s.charAt(1); // 'a'
	int res = s.compareTo(c); // 返回差值；小于则返回小于0；等于返回0
	int res = s.compareToIgnoreCase(n);
	String res = s.concat(c);
	void s.contains(keyword);
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

	String message = String.format("hello, %s. Next year, you'll be %d", name, age);


	String substring(int beginIndex, int endIndex) // 包含起始位置，不包括结束索引位置

	char[] toArray()
	n.toArray(); // ["y","A","U","N","O"]

	n.toLowerCase(); // "yauno"
	n.toUpperCase(); // "YAUNO"

	String m = new String("   xbb   ");
	m.trim(); // "xbb"


	char charAt(int index) 	// 返回指定索引处的 char 值。
	int compareTo(Object o) //把这个字符串和另一个对象比较。
	int compareTo(String anotherString) // 按字典顺序比较两个字符串。
	int compareToIgnoreCase(String str) // 按字典顺序比较两个字符串，不考虑大小写。
	String concat(String str) // 将指定字符串连接到此字符串的结尾。
	boolean contentEquals(StringBuffer sb) // 当且仅当字符串与指定的StringButter有相同顺序的字符时候返回真。
	static String copyValueOf(char[] data) // 返回指定数组中表示该字符序列的 String。
	static String copyValueOf(char[] data, int offset, int count) // 返回指定数组中表示该字符序列的 String。
	boolean endsWith(String suffix) // 测试此字符串是否以指定的后缀结束。
	boolean equals(Object anObject) // 将此字符串与指定的对象比较。
	boolean equalsIgnoreCase(String anotherString) // 将此 String 与另一个 String 比较，不考虑大小写。
	byte[] getBytes() // 使用平台的默认字符集将此 String 编码为 byte 序列，并将结果存储到一个新的 byte 数组中。
	byte[] getBytes(String charsetName) // 使用指定的字符集将此 String 编码为 byte 序列，并将结果存储到一个新的 byte 数组中。
	void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin) // 将字符从此字符串复制到目标字符数组。
	int hashCode() 	// 返回此字符串的哈希码。
	int indexOf(int ch) // 返回指定字符在此字符串中第一次出现处的索引。
	int indexOf(int ch, int fromIndex) //回在此字符串中第一次出现指定字符处的索引，从指定的索引开始搜索。
	int indexOf(String str) // 返回指定子字符串在此字符串中第一次出现处的索引。
	int indexOf(String str, int fromIndex) //返回指定子字符串在此字符串中第一次出现处的索引，从指定的索引开始。
	String intern() // 返回字符串对象的规范化表示形式。
	int lastIndexOf(int ch) // 返回指定字符在此字符串中最后一次出现处的索引。
	int lastIndexOf(int ch, int fromIndex) //返回指定字符在此字符串中最后一次出现处的索引，从指定的索引处开始进行反向搜索。
	int lastIndexOf(String str) // 返回指定子字符串在此字符串中最右边出现处的索引。
	int lastIndexOf(String str, int fromIndex) // 返回指定子字符串在此字符串中最后一次出现处的索引，从指定的索引开始反向搜索。
	int length() // 返回此字符串的长度。
	boolean matches(String regex)v // 告知此字符串是否匹配给定的正则表达式。
	boolean regionMatches(boolean ignoreCase, int toffset, String other, int ooffset, int len) // 测试两个字符串区域是否相等。
	boolean regionMatches(int toffset, String other, int ooffset, int len) // 测试两个字符串区域是否相等。
	String replace(char oldChar, char newChar) // 返回一个新的字符串，它是通过用 newChar 替换此字符串中出现的所有 oldChar 得到的。
	String replaceAll(String regex, String replacement) // 使用给定的 replacement 替换此字符串所有匹配给定的正则表达式的子字符串。
	String replaceFirst(String regex, String replacement) // 使用给定的 replacement 替换此字符串匹配给定的正则表达式的第一个子字符串。
	String[] split(String regex) // 根据给定正则表达式的匹配拆分此字符串。
	String[] split(String regex, int limit) // 根据匹配给定的正则表达式来拆分此字符串。
	boolean startsWith(String prefix) // 测试此字符串是否以指定的前缀开始。
	boolean startsWith(String prefix, int toffset) // 测试此字符串从指定索引开始的子字符串是否以指定前缀开始。
	CharSequence subSequence(int beginIndex, int endIndex) // 返回一个新的字符序列，它是此序列的一个子序列。
	String substring(int beginIndex) // 返回一个新的字符串，它是此字符串的一个子字符串。
	String substring(int beginIndex, int endIndex) // 返回一个新字符串，它是此字符串的一个子字符串。
	char[] toCharArray() // 将此字符串转换为一个新的字符数组。
	String toLowerCase() // 使用默认语言环境的规则将此 String 中的所有字符都转换为小写。
	String toLowerCase(Locale locale) // 使用给定 Locale 的规则将此 String 中的所有字符都转换为小写。
	String toString() // 返回此对象本身（它已经是一个字符串！）。
	String toUpperCase() // 使用默认语言环境的规则将此 String 中的所有字符都转换为大写。
	String toUpperCase(Locale locale) // 使用给定 Locale 的规则将此 String 中的所有字符都转换为大写。
	String trim() // 返回字符串的副本，忽略前导空白和尾部空白。
	static String valueOf(primitive data type x) // 返回给定data type类型x参数的字符串表示形式。



16.2 Scanner
	Scanner in = new Scanner(System.in);
	String s = in.nextLine(); // 读取输入下一行内容
	String sNext = in.next(); // 读取下一个单词，以空格作为分隔符
	int nextint = in.nextInt();
	double nextdouble = in.nextDouble();
	boolean hasnxt = in.hasNext();
	boolean hasnextint = in.hasNextInt();
	boolean hasdouble = in.hasNextDouble();

17 Arrays 
  17.1. Arrays.asList(T… data) 
	// 注意：该方法返回的是Arrays内部静态类ArrayList，而不是我们平常使用的ArrayList,，该静态类ArrayList没有覆盖父类的add, remove等方法，所以如果直接调用，会报UnsupportedOperationException异常

	// 将数组转换为集合，接收一个可变参
	17.1.1 List<Integer> list = Arrays.asList(1, 2, 3);
	list.forEach(System.out::println); // 1 2 3

	Integer[] data = {1, 2, 3};
	List<Integer> list = Arrays.asList(data);

	// 如果将基本数据类型的数组作为参数传入， 
	// 该方法会把整个数组当作返回的List中的第一个元素
	int[] data = {1, 2, 3};
	17.1.2 List<int[]> list = Arrays.asList(data);
	System.out.println(list.size()); // 1
	System.out.println(Arrays.toString(list.get(0))); // [1, 2, 3]

  17.2、Arrays.fill()

	17.2.1 Arrays.fill(Object[] array, Object obj)
	// 用指定元素填充整个数组（会替换掉数组中原来的元素）
	Integer[] data = {1, 2, 3, 4};
	Arrays.fill(data, 9);
	System.out.println(Arrays.toString(data)); // [9, 9, 9, 9]

	17.2.2 Arrays.fill(Object[] array, int fromIndex, int toIndex, Object obj)
	// 用指定元素填充数组，从起始位置到结束位置，取头不取尾（会替换掉数组中原来的元素）
	Integer[] data = {1, 2, 3, 4};
	Arrays.fill(data, 0, 2, 9);

  17.3、Arrays.sort()
	17.3.1 Arrays.sort(Object[] array)
	// 对数组元素进行排序（串行排序）
	String[] data = {"1", "4", "3", "2"};
	System.out.println(Arrays.toString(data)); // [1, 4, 3, 2]
	Arrays.sort(data);
	System.out.println(Arrays.toString(data)); // [1, 2, 3, 4]

	17.3.2 Arrays.sort(T[] array, Comparator<? super T> comparator)
	// 使用自定义比较器，对数组元素进行排序（串行排序）
	String[] data = {"1", "4", "3", "2"};
	System.out.println(Arrays.toString(data)); // [1, 4, 3, 2]
	// 实现降序排序，返回-1放左边，1放右边，0保持不变
	Arrays.sort(data, (str1, str2) -> {
	    if (str1.compareTo(str2) > 0) {
	        return -1;
	    } else {
	        return 1;
	    }
	});

	// other
	17.3.3 Arrays.sort(Object[] array, int fromIndex, int toIndex)


	17.3.4 Arrays.sort(T[] array, int fromIndex, int toIndex, Comparator<? super T> c)
	使用自定义比较器，对数组元素的指定范围进行排序（串行排序）
	String[] data = {"1", "4", "3", "2"};
	System.out.println(Arrays.toString(data)); // [1, 4, 3, 2]
	// 对下标[0, 3)的元素进行降序排序，即对1，4，3进行降序排序，2保持不变
	Arrays.sort(data, 0, 3, (str1, str2) -> {
	    if (str1.compareTo(str2) > 0) {
	        return -1;
	    } else {
	        return 1;
	    }
	});
	System.out.println(Arrays.toString(data)); // [4, 3, 1, 2]

  17.4、Arrays.parallelSort() 
	// 注意：其余重载方法与 sort() 相同

	17.4.1 Arrays.parallelSort(T[] array)
		// 对数组元素进行排序（并行排序），当数据规模较大时，会有更好的性能
		String[] data = {"1", "4", "3", "2"};
		Arrays.parallelSort(data);
		System.out.println(Arrays.toString(data)); // [1, 2, 3, 4]

  17.5、Arrays.binarySearch() 
	// 注意：在调用该方法之前，必须先调用sort()方法进行排序，如果数组没有排序， 
	// 那么结果是不确定的，此外如果数组中包含多个指定元素，则无法保证将找到哪个元素

	17.5.1 Arrays.binarySearch(Object[] array, Object key)
	// 使用 二分法 查找数组内指定元素的索引值

	// 这里需要先看下binarySearch()方法的源码，对了解该方法有很大的帮助 


	// 搜索元素是数组元素，则返回该元素的索引值
	// 如果不是数组元素，则返回 - (索引值 + 1)，具体的用法可以看下面的例子
	// 搜索元素是数组元素，返回该元素索引值

	Integer[] data = {1, 3, 5, 7};
	Arrays.sort(data);
	System.out.println(Arrays.binarySearch(data, 1)); // 0

	// 搜索元素不是数组元素，且小于数组中的最小值
	Integer[] data = {1, 3, 5, 7};
	Arrays.sort(data);
	// 此时程序会把数组看作 {0, 1, 3, 5, 7}，此时0的索引值为0，则搜索0时返回 -(0 + 1) = -1
	System.out.println(Arrays.binarySearch(data, 0)); // -1

	// 搜索元素不是数组元素，且大于数组中的最大值
	Integer[] data = {1, 3, 5, 7};
	Arrays.sort(data);
	// 此时程序会把数组看作 {1, 3, 5, 7， 9}，此时9的索引值为4，则搜索8时返回 -(4 + 1) = -5
	System.out.println(Arrays.binarySearch(data, 8)); // -5

	// 搜索元素不是数组元素，但在数组范围内
	Integer[] data = {1, 3, 5, 7};
	Arrays.sort(data);
	// 此时程序会把数组看作 {1, 2, 3, 5, 7}，此时2的索引值为1，则搜索2时返回 -(1 + 1) = -2
	System.out.println(Arrays.binarySearch(data, 2)); // -2

	17.5.2 Arrays.binarySearch(Object[] array, int fromIndex, int toIndex, Object obj)
	// 使用 二分法 查找数组内指定范围内的指定元素的索引值
	Integer[] data = {1, 3, 5, 7};
	Arrays.sort(data);
	// {1, 3}，3的索引值为1
	System.out.println(Arrays.binarySearch(data, 0, 2, 3)); // 1

  17.6、Arrays.copyOf()
	17.6.1 Arrays.copyOf(T[] original, int newLength)
	// 拷贝数组，其内部调用了 System.arraycopy() 方法，从下标0开始，如果超过原数组长度，会用null进行填充
	Integer[] data1 = {1, 2, 3, 4};
	Integer[] data2 = Arrays.copyOf(data1, 2);
	System.out.println(Arrays.toString(data2)); // [1, 2]
	Integer[] data2 = Arrays.copyOf(data1, 5);
	System.out.println(Arrays.toString(data2)); // [1, 2, 3, 4, null]

  17.7、Arrays.copyOfRange(T[] original, int from, int to)
	// 拷贝数组，指定起始位置和结束位置，如果超过原数组长度，会用null进行填充
	Integer[] data1 = {1, 2, 3, 4};
	Integer[] data2 = Arrays.copyOfRange(data1, 0, 2);
	System.out.println(Arrays.toString(data2)); // [1, 2]
	Integer[] data2 = Arrays.copyOfRange(data1, 0, 5);
	System.out.println(Arrays.toString(data2)); // [1, 2, 3, 4, null]

  17.8、Arrays.equals(Object[] array1, Object[] array2)
	// 判断两个数组是否相等，实际上比较的是两个数组的哈希值，即 Arrays.hashCode(data1) == Arrays.hashCode(data2)
	Integer[] data1 = {1, 2, 3};
	Integer[] data2 = {1, 2, 3};
	System.out.println(Arrays.equals(data1, data2)); // true

  17.9、Arrays.deepEquals(Object[] array1, Object[] array2)
	// 判断两个多维数组是否相等，实际上比较的是两个数组的哈希值，即 Arrays.hashCode(data1) == Arrays.hashCode(data2)
	Integer[][] data1 = {{1,2,3}, {1,2,3}};
	Integer[][] data2 = {{1,2,3}, {1,2,3}};
	System.out.println(Arrays.deepEquals(data1, data2)); // true

  17.10、Arrays.hashCode(Object[] array)
	// 返回数组的哈希值
	Integer[] data = {1, 2, 3};
	System.out.println(Arrays.hashCode(data)); // 30817

  17.11、Arrays.deepHashCode(Object[] array)
	// 返回多维数组的哈希值
	Integer[][] data = {{1, 2, 3}, {1, 2, 3}};
	System.out.println(Arrays.deepHashCode(data)); // 987105

  17.12、Arrays.toString(Object[] array)
	// 返回数组元素的字符串形式
	Integer[] data = {1, 2, 3};
	System.out.println(Arrays.toString(data)); // [1, 2, 3]

  17.13、Arrays.deepToString(Object[] array)
	// 返回多维数组元素的字符串形式
	Integer[][] data = {{1, 2, 3}, {1, 2, 3}};
	System.out.println(Arrays.deepToString(data)); // [[1, 2, 3], [1, 2, 3]]

  17.14、Arrays.setAll(T[] array, IntFunction
	Integer[] data = {1, 2, 3, 4};
	// i为索引值
	Arrays.setAll(data, i -> data[i] * 2);
	System.out.println(Arrays.toString(data)); // [2, 4, 6, 8]

  17.15、Arrays.parallelSetAll(T[] array, IntFunction
	Integer[] data = {2, 3, 4, 5};
	// 第一个元素2不变，将其与第二个元素3一起作为参数x, y传入，得到乘积6，作为数组新的第二个元素
	// 再将6和第三个元素4一起作为参数x, y传入，得到乘积24，作为数组新的第三个元素，以此类推
	Arrays.parallelPrefix(data, (x, y) -> x * y);
	System.out.println(Arrays.toString(data)); // [2, 6, 24, 120]


  17.16、Arrays.spliterator(T[] array)
	// 返回数组的分片迭代器，用于并行遍历数组
	public class Students {

	    private String name;

	    private Integer age;

	    public Students(String name, Integer age) {
	        this.name = name;
	        this.age = age;
	    }
	    // 省略get、set方法
	}

	public static void main(String[] args) {
	    Students[] data = new Students[5];
	    IntStream.range(0,5).forEach(i -> data[i] = new Students("小明"+i+"号", i));
	    // 返回分片迭代器
	    Spliterator<Students> spliterator = Arrays.spliterator(data);
	    spliterator.forEachRemaining(stu -> {
	        System.out.println("学生姓名: " + stu.getName() + "  " + "学生年龄: " + stu.getAge());
	        // 学生姓名: 小明0号  学生年龄: 0
	        // 学生姓名: 小明1号  学生年龄: 1
	        // 学生姓名: 小明2号  学生年龄: 2
	        // 学生姓名: 小明3号  学生年龄: 3
	        // 学生姓名: 小明4号  学生年龄: 4
	    });
	}

  17.17、Arrays.stream(T[] array)
	// 返回数组的流Stream，然后我们就可以使用Stream相关的许多方法了
	Integer[] data = {1, 2, 3, 4};
	List<Integer> list = Arrays.stream(data).collect(toList());
	System.out.println(list); // [1, 2, 3, 4]


18. StringBuffer & StringBuilder
	和 String 类不同的是，这两个类的对象能够被多次修改并且不产生新的未使用对象。
	StringBuffer 速度弱于 StringBuilder,但线程安全时喜不适用 StringBuffer 

	StringBuffer s = new StringBuffer("yauno");
	String ss = s.toString();
	public StringBuffer append(String s)
	public StringBuffer reverse()
	public delete(int start, int end)
	public insert(int offset, int i)
	replace(int start, int end, String s)


19. 时间
	Date date = new Date();
	date.toString();

	LocalDate date = new LocalDate.now();
	int month = date.getMonthValue();
	int day = date.getDayOfMonth();
	...

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
	        FileOutputStream fout = new FileOutputStream(f);	// 可以将字符流转为字节流

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

	        StringBuffer sb = new StringBuffer();	// 属于处理流中的缓冲流， 可以将读取的内容存在内存里面
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

	26.1 ArrayList：底层的数据结构使用的是数组结构（数组长度是可变的百分之五十延长）（特点是查询很快，但增删较慢）线程不同步

	26.2 LinkedList：底层的数据结构是链表结构（特点是查询较慢，增删较快）
	26.3 Vector：底层是数组数据结构 线程同步（数组长度是可变的百分之百延长）（无论查询还是增删都很慢，被ArrayList替代了）
	List接口的常用实现类有ArrayList和LinkedList，在使用List集合时，通常情况下声明为List类型，实例化时根据实际情况的需要，实例化为ArrayList或LinkedList，例如：
	List<String> l = new ArrayList<String>();// 利用ArrayList类实例化List集合
	List<String> l2 = new LinkedList<String>();// 利用LinkedList类实例化List集合
	String a = "A", b = "B", c = "C";
	List<String> list = new LinkedList<String>();

	list.add(a);
	list.remove(0); 
	list.remove("A");
	list.size(); // int[] s  --->  s.length;
	list.contains("a,b,c");
	list.clear();
	list.set(1, b);// 将索引位置为1的对象e修改为对象b
	list.add(2, c);// 将对象c添加到索引位置为2的位置
	list.subList(from, to).clear(); // 截断不影响原列表
	list.subList(from, to); 	// 影响原列表
	list.isEmpty();
	list.toArray();
	list.addAll(anotherList);
	
	for (int i = 0; i < list.size(); i++) {
		System.out.println(list.get(i));// 利用get(int index)方法获得指定索引位置的对象
	}
	// for的形式
	for (int i=0;i<arr.size();i++) {...}
	// foreach的形式： 
	for (int　i：arr) {...}
	// iterator的形式：
	Iterator it = arr.iterator();
	while (it.hasNext()){ object o =it.next(); ...}


27. Queue
	// Queue: FIFO 数据结构，与 Set, List 同一级别，都是继承 Collection, 用 LinkedList 实现 Queue 接口
	// https://www.cnblogs.com/lemon-flm/p/7877898.html
	// 非阻塞
	  
	ConcurrentLinkedQueue
	// 双端列队
	Deque
	// 阻塞列队
	BlockingQueue为接口
	ArrayBlockingQueue // 一个由数组支持的有界队列。在构造时需要指定容量， 并可以选择是否需要公平性，如果公平参数被设置true，等待时间最长的线程会优先得到处理（其实就是通过将ReentrantLock设置为true来 达到这种公平性的：即等待时间最长的线程会先操作）。通常，公平性会使你在性能上付出代价，只有在的确非常需要的时候再使用它。它是基于数组的阻塞循环队 列，此队列按 FIFO（先进先出）原则对元素进行排序。
　　LinkedBlockingQueue //一个由链接节点支持的可选有界队列。容量是没有上限的（说的不准确，在不指定时容量为Integer.MAX_VALUE，不要然的话在put时怎么会受阻呢），但是也可以选择指定其最大容量，它是基于链表的队列，此队列按 FIFO（先进先出）排序元素。
　　PriorityBlockingQueue //一个由优先级堆支持的无界优先级队列。是一个带优先级的 队列，而不是先进先出队列。元素按优先级顺序被移除，该队列也没有上限（看了一下源码，PriorityBlockingQueue是对 PriorityQueue的再次包装，是基于堆数据结构的，而PriorityQueue是没有容量限制的，与ArrayList一样，所以在优先阻塞 队列上put时是不会受阻的。虽然此队列逻辑上是无界的，但是由于资源被耗尽，所以试图执行添加操作可能会导致 OutOfMemoryError），但是如果队列为空，那么取元素的操作take就会阻塞，所以它的检索操作take是受阻的。另外，往入该队列中的元 素要具有比较能力。
　　DelayQueue //一个由优先级堆支持的、基于时间的调度队列。是一个存放Delayed 元素的无界阻塞队列，只有在延迟期满时才能从中提取元素。该队列的头部是延迟期满后保存时间最长的 Delayed 元素。如果延迟都还没有期满，则队列没有头部，并且poll将返回null。当一个元素的 getDelay(TimeUnit.NANOSECONDS) 方法返回一个小于或等于零的值时，则出现期满，poll就以移除这个元素了。此队列不允许使用 null 元素。
　　SynchronousQueue //一个利用 BlockingQueue 接口的简单聚集（rendezvous）机制。
	BlockingQueue<String> queue = new ArrayBlockingQueue<String>();
	阻塞列队的方法
　　add      增加一个元索                     如果队列已满，则抛出一个IIIegaISlabEepeplian异常
　　remove   移除并返回队列头部的元素    如果队列为空，则抛出一个NoSuchElementException异常
　　element  返回队列头部的元素             如果队列为空，则抛出一个NoSuchElementException异常
　　offer    添加一个元素并返回true       如果队列已满，则返回false
　　poll     移除并返回队列头部的元素    如果队列为空，则返回null
　　peek     返回队列头部的元素             如果队列为空，则返回null
　　put      添加一个元素                      如果队列满，则阻塞
　　take     移除并返回队列头部的元素     如果队列为空，则阻塞

	remove、element、offer、poll、peek,isEmpty() 是属于Queue接口。 

	// 遍历
	Queue<String> waitingQueue = new LinkedList<>();
	// 遍历using Java 8 forEach()
    waitingQueue.forEach(name -> {
        System.out.println(name);
    });

    // 遍历 iterator()
    Iterator<String> waitingQueueIterator = waitingQueue.iterator();
    while (waitingQueueIterator.hasNext()) {
        String name = waitingQueueIterator.next();
        System.out.println(name);
    }

    // 遍历 iterator() and Java 8 forEachRemaining()
    waitingQueueIterator = waitingQueue.iterator();
    waitingQueueIterator.forEachRemaining(name -> {
        System.out.println(name);
    });

    // 遍历using simple for-each loop ===");
    for(String name: waitingQueue) {
        System.out.println(name);
    }


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
	LinkedBlockingDeque是Deque的并发实现,在队列为空的时候,它的takeFirst,takeLast会阻塞等待队列处于可用状态

29. Map
	HashMap // 线程非安全, 允许使用null键和null值, 会使用equals比较key对象
	TreeMap	// 线程不安全，不允许null
	HashTable // 线程安全，比较慢
	LinkedHashMap // 
	EnumMap // https://blog.csdn.net/ljh_learn_from_base/article/details/77991970 
	// 实例
		class EnumMapTest {
			public enum Color{//默认继承  extends Enum类，所以枚举也是个类，既然是类就有构造函数，变量，方法等
				RED, BLUE, BLACK, YELLOW, GREEN;//下标为0,1,2,3,4
				@Override
				public String toString() {
					return super.toString()+"..."+super.ordinal();//ordinal()方法获取下标
				}
			}
		 
			public static void main(String[] args) {
				EnumMap<Color, String> map = new EnumMap<>(Color.class);
		         //System.out.println(Color.GREEN);
				map.put(Color.YELLOW, "黄色");
				map.put(Color.BLUE, null);
				// map.put(null, "无"); //会报NullPonitException的错误
				map.put(Color.RED, "红色");
				map.put(Color.GREEN, "绿色");
		        map.get(Color.BLACK);
				for (Map.Entry<Color, String> entry : map.entrySet()) {
					System.out.println(entry.getKey() + ":" + entry.getValue());
				}
				System.out.println(map);
			}
		}

	WeakHashMap // 键和值都可以是null
	IdentityHashMap // 使用 == 比较key对象, 要想key内容能够重复 (指的
					// 是两个对象的地址不一样，key1!=key2）。则要使用IdentityHashMap类
	HashMap<String, Integer> map = new HashMap<>();
	map.put("sss", 1);
	map.get("sss"); // 不存在返回null
	map.pullAll(Map<? extends K,? extends V> m);
	boolean iscontain =  map.containsKey(xx);
	boolean iscontain =  map.constainsValue(xx);
	boolean isempty = map.isEmpty(); 
	map.remove(xx);
	map.clear();
	int size = map.size();
	// 遍历法1
	Iterator it = map.keySet().iterator();
	    //获取迭代器
	    while(it.hasNext()){
	        Object key = it.next();
	        System.out.println(map.get(key));
	    }
	// 遍历法2
    Collection<String> vs = map.values();
    Iterator<String> it = vs.iterator();
    while (it.hasNext()) {
        String value = it.next();
        System.out.println(" value=" + value);
    }
    // 法3, 效率最高
    // 返回的Map.Entry对象的Set集合 Map.Entry包含了key和value对象
    Set<Map.Entry<Integer, String>> es = map.entrySet();
    Iterator<Map.Entry<Integer, String>> it = es.iterator();
    while (it.hasNext()) {
        // 返回的是封装了key和value对象的Map.Entry对象
        Map.Entry<Integer, String> en = it.next();
        // 获取Map.Entry对象中封装的key和value对象
        Integer key = en.getKey();
        String value = en.getValue();
        System.out.println("key=" + key + " value=" + value);
    }

    // 根据key排序
    Map< Integer, String> map=new TreeMap<>();
    map.put(5, "a");
    map.put(3, "c");
    map.put(4, "b");
    map.put(2, "d");
    map.put(1, "e");
    List<Entry<Integer,String>> list =new ArrayList<Entry<Integer,String>>(map.entrySet());
    Collections.sort(list, new Comparator<Entry<Integer, String>>() {

        @Override
        public int compare(Entry<Integer, String> o1, Entry<Integer, String> o2) {
            // TODO Auto-generated method stub
            return o1.getValue().compareTo(o2.getValue());
        }
    });
    for(Entry<Integer, String> aEntry:list) {
        System.out.println(aEntry.getKey()+":"+aEntry.getValue());
    }


30. Set
	30.1 HashSet // HashSet不允许重复（HashMap的key不允许重复，如果出现重复就覆盖）,
	 			 // 允许null值，非线程安全

	30.2 TreeSet // 使用元素的自然顺序对元素进行排序。
				 // 或者根据创建 set 时提供的 Comparator进行排序，具体取决于使用的构造方法
	30.3 SortSet // 
	Set<ListNode> set = new HashSet<>();
	set.contains(xx);
	set.remove(xx);
	set.add(xx)
	set.clear();
	set.clone(); // 浅复制
	set.isEmpty();
	// 遍历1
	Set<String> set = new HashSet<String>();  
	Iterator<String> it = set.iterator();  
	while (it.hasNext()) {  
	  String str = it.next();  
	  System.out.println(str);  
	}  
	// 遍历2
	// for(foreach)循环遍历
	for (String str : set) {  
	      System.out.println(str);  
	} 

31. Stack
	Stack<Integer> stack = new Stack<>();
	boolean empty() // 测试堆栈是否为空。
	Object peek( ) // 查看堆栈顶部的对象，但不从堆栈中移除它。
	Object pop( ) // 移除堆栈顶部的对象，并作为此函数的值返回该对象。
	Integer size = stack.size();
	Object push(Object element) // 把项压入堆栈顶部。
	int search(Object element) // 返回对象在堆栈中的位置，以 1 为基数。
	             boolean       empty()
	synchronized E             peek()
	synchronized E             pop()
	             E             push(E object)
	synchronized int           search(Object o)

32. 集合方法 
	// https://www.cnblogs.com/yoyohong/p/7644650.html
	// 排序
	Collections.sort(list, new Comparator<Student>() {
	    @Override
	    public int compare(Student o1, Student o2) {
	        return o1.getId() - o2.getId();
	    }
	});
	// 获取最大最小值
	int max = Collections.max(list);
	int min = Collections.min(list);
	
	Collections.shuffle(list)
	
	int index1 = Collections.binarySearch(list2, "Thursday");
	// 替换集合中指定元素
	boolean flag = Collections.replaceAll(list2, "Sunday", "tttttt");

	//反转集合中的元素的顺序
        Collections.reverse(list2);

    // 交换集合中指定元素
    Collections.swap(list2, 0, 3);

    //替换集合中的所有元素，用对象object
    Collections.fill(list2, "替换");

 	//生成一个指定大小与内容的集合
    List<String> list4 = Collections.nCopies(5, "哈哈");

	//为集合生成一个Enumeration
    List<String> list5 = Arrays.asList("I love my country!".split(" "));
    System.out.println(list5);
    Enumeration<String> e = Collections.enumeration(list5);
    while (e.hasMoreElements()) {
        System.out.println(e.nextElement());
    }