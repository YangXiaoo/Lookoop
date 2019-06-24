class Integer {
	public static int IID = 0;
	private int num = 0;

	Integer(int num) {
		this.num = num;
	}

	public String toString() {
		return "[custome define] " + num;
	}
}

class A {
	public static String c = "c";
	static {
		System.out.println("A");
	}
}

class B extends A {
	static {
		System.out.println("B");
	}
}
public class Test {

	public static void main(String[] args) {
		System.out.println(B.c);
	}
}
 