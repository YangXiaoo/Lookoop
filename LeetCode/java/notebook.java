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

