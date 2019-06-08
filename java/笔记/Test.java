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
	public static void main(String[] args){
		Integer it = new Integer(10);
		System.out.println(it.toString());
	}
}
 