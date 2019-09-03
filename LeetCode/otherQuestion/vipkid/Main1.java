import java.util.*;

// 2019/9/3
public class Main1 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			String[] ns = cin.nextLine().split(",");

			// 获取数组
			int[] nums = new int[ns.length];
			for (int i = 0; i < ns.length; ++i) {
				nums[i] = Integer.parseInt(ns[i].trim());
			}

			int ret = solver(nums);
			System.out.println(ret);
		}
	}

	public static int solver(int[] nums) {
		int ret = 0;
		Set<Integer> set = new HashSet<>();
		Set<Integer> tmp = new HashSet<>();
		for (int n : nums) {
			if (set.contains(n)) {	// 如果存在相反数
				if ((!tmp.contains(n)) && (!tmp.contains(-n))) {	// 结果不重复
					tmp.add(n);
					ret += 1;
				}
			}

			set.add(-n);
		}

		return ret;
	}
}