import java.util.*;
import java.io.*;

// 2019/9/7
// 判断整数的二进制是否为回文串
public class Main1 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			int t = cin.nextInt();
			String[] ret = new String[t];
			for (int i = 0; i < t; ++i) {
				String cur = solver(cin.nextInt());
				ret[i] = cur;
			}

			for (String r : ret) {
				System.out.println(r);
			}
		}
	}

	public static String solver(int n) {
		StringBuilder sb = new StringBuilder();
		while (n != 0) {
			int cur = 1 & n;
			n >>= 1;
			sb.append(cur);
		}
		String rs = sb.reverse().toString();
		// System.out.println(rs);
		for (int i = 0; i < rs.length(); ++i) {
			if (rs.charAt(i) != '0') {
				sb = new StringBuilder(rs.substring(i));
				break;
			}
		}

		if (sb.toString().equals(sb.reverse().toString())) {
			return "YES";
		} 

		return "NO";
	}
}