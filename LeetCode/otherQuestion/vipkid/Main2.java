import java.util.*;

// 2019/9/3
// 求整数中bit位上1的个数
public class Main2 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			int number = Integer.parseInt(cin.nextLine());
			int ret = solver(number);
			System.out.println(ret);
		}
	}

	public static int solver(int n) {
		int ret = 0;
		while (n != 0) {
			n = (n - 1) & n;
			ret += 1;
		}

		return ret;
	}
}