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


public class Test {
	int i = getJ();
	int j = 0;
	public int getJ() {
		System.out.println("j: " + j);
		j = 10;
		System.out.println("i: " + i);
		return j;
	}

	public static void main(String[] args) {
		Test test = new Test();
		System.out.println("j: " + test.j);
	}
}
 