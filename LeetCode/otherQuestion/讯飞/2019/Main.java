import java.util.*;
// Q1
// 输入字符串将数字取出并排序后输出
public class Main {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			String line = cin.nextLine();
			ArrayList<Integer> list = new ArrayList<>();
			for (int i = 0; i < line.length(); ++i) {
				char curChar = line.charAt(i);
				int curInt = curChar - '0';
				if (curInt >= 0 && curInt <= 9) {
					list.add(curInt);
				}
			}
            if (list.size() == 0) {
                System.out.println("-1");
            }

			Collections.sort(list);
            StringBuilder sb = new StringBuilder();
			for (Integer n : list) {
				sb.append(n);
			}
            System.out.printf(sb.toString());
		}
	}
}