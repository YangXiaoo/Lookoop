import java.io.*;
import java.util.*;

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
	public static void fileWrite(File file, String str) {
		FileOutputStream fout = null;
		OutputStreamWriter fwriter = null;
		try {
			fout = new FileOutputStream(file);
			fwriter = new OutputStreamWriter (fout, "UTF-8");
			fwriter.write(str);
			fwriter.flush();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				fout.close();
				fwriter.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}


		System.out.println("[INFO] write successful, content: " + str);
	}

	public static void fileRead(File file) {
		FileInputStream fin = null;
		InputStreamReader freader = null;
		StringBuilder sb = new StringBuilder();
		try {
			fin = new FileInputStream(file);
			freader = new InputStreamReader(fin);
			while (freader.ready()) {
				sb.append((char)freader.read());
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				fin.close();
				freader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}


		System.out.println(sb.toString());
	}

	public static void testReadWrite() {
		File file = new File("C:\\Study\\github\\Lookoops\\java\\笔记\\tmp.txt");
		String str = "test\nthis is a test file!";

		// fileWrite(file, str);
		fileRead(file);
	}


}
 