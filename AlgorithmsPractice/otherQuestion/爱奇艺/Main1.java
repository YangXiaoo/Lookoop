import java.util.*;
import java.io.*;

public class Main1 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);

		while (cin.hasNext()) {
			int n = cin.nextInt();
			int[] aNums = new int[n-1];
			for (int i = 0; i < n-1; ++i) {
				aNums[i] = cin.nextInt();
			}

			int[] sum = new int[1];
			sum[0] = 0;
			List<Integer> tmp = new LinkedList<>();
			genNums(n, tmp, sum, aNums);
			System.out.println(sum[0]);
		}
	}

	public static void genNums(int n, List<Integer> tmp, int[] sum, int[] aNums) {
		if (tmp.size() == n) {
			sum[0] = sum[0] + 1;
		} else {
			for (int i = 1; i < n+1; ++i) {
				if (!tmp.contains(i)) {
					if (check(tmp, i-1, aNums)) {
						tmp.add(i);
						genNums(n, tmp, sum, aNums);
						tmp.remove(tmp.size()-1);
					}
				}
			}
		}
	}

	public static boolean check(List<Integer> tmp, int i, int[] aNums) {
		if (tmp.isEmpty()) return true;

		int pre = tmp.get(tmp.size()-1);
		int index = tmp.size() - 1;
		if (aNums[index] == 0) {
			if (pre < i + 1) {
				return true;
			}
		} else {
			if (pre > i + 1) {
				return true;
			}
		}

		return false;
	}
}