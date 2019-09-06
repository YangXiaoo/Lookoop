import java.io.*;
import java.util.*;

// 入口文件无法使用
// class String {
// 	private char[] charList = new char[20];
// 	String() {
// 		System.out.println("init");
// 	}
// } 
// class Integer {
// 	public static int IID = 0;
// 	private int num = 0;

// 	Integer(int num) {
// 		this.num = num;
// 	}

// 	public String toString() {
// 		return "[custome define] " + num;
// 	}
// }

class A {
	int a = 1;
}

class B {
	protected int b = 2;
}

class C extends A{
	private int c = 3;
}

public class Test {

	private List<File> fileList = new ArrayList<>();
	public static void testFalse() {
		// 测试保留字
		// int false = 1;
		// System.out.println(false);
	}

	public static void testGoto() {
		// 测试关键字
		// int goto = 1;
		// System.out.println(goto);
	}

	public void testShare() {
		// Integer a = 2;	// 错误: 不兼容的类型: int无法转换为Integer
		// int b = 2;
		// Integer c = 2;
		System.out.println();
	}

	public static void testDefaultDeclare() {
		A a = new A();
		B b = new B();
		C c = new C();
		System.out.println(a.a);	// default在同包下可以被访问
		System.out.println(b.b);
		System.out.println(c.a);	// 要使得default修饰的变量在子类方法中被继承必须在一个包下
		// System.out.println(c.c);	// 错误: c 在 C 中是 private 访问控制
	}

	public static void main(String[] args) {
		testDefaultDeclare();
	}

}
 