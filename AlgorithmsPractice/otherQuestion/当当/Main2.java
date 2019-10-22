import java.util.*;

public class Main2 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			String s = cin.nextLine();
			int ret = solver(s);
			System.out.println(ret);
		}
	}

	public static int solver(String s) {
		int[] maps = new int[128];
		Arrays.fill(maps, 0);
		for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) != ' ')
			    maps[s.charAt(i) - ' '] += 1;
		}

		int ret = 0;
		for (int n : maps) {
			if (n > ret) {
				ret = n;
			}
		}

		return ret;
	}
}