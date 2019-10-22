// 2019-4-21
// 数组中超过一半的数字

import java.util.*;

public class MoreThanHalfNumber {
	public int halfNumber(int[] nums) {
		int ret = nums[0], count = 1;
		for (int i = 1; i < nums.length; ++i) {
			if (ret == nums[i]) {
				count++;
			} else {
				if (count == 1) {
					ret = nums[i];
				} else {
					count--;
				}
			}
		}

		// if (!isValid(nums, ret)) {
		// 	ret = 0
		// }

		return ret;
	}

	public void test(String testName, int[] nums, int expect) {
		int ret = halfNumber(nums);
		System.out.println(testName + ", result: " + ret + ", expect: " + expect);
	}

	public static void main(String[] args) {
		MoreThanHalfNumber test = new MoreThanHalfNumber();
		int[] nums1 = {1, 2, 3, 2, 2,2,5,4,2};
		test.test("test1", nums1, 2);
	}
}