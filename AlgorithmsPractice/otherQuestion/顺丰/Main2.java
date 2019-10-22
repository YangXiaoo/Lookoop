import java.util.*;
// ac 64%
public class Main2 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			String ns = cin.nextLine();
			int n = Integer.parseInt(ns);
			String line = cin.nextLine();
			String[] str = line.split(" ");
			int[] nums = new int[n];
			for (int i = 0; i < n; ++i) {
				nums[i] = Integer.parseInt(str[i]);
			}

			int ret = solver(nums);
			System.out.println(ret);
		}
	}

	public static int solver(int[] nums) {
		int[] dp = new int[nums.length];
		int ret = 0;
		for (int i = 0; i < nums.length; ++i) {
			dp[i] = 1;
			for (int j = 0; j < i; ++j) {
				if (nums[i] >= nums[j]) {
					dp[i] = Math.max(dp[i], dp[j] + 1);
				}
			}
		}
		for (int k = 0; k < dp.length; ++k) {
			if (dp[i] > ret) {
				ret = dp[i];
			}
		}
		return ret;
	}
}