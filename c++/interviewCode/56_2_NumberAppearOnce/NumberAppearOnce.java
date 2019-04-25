// 2019-4-24
// 在一个数组中除了一个数字出现了一次之外其余数字都出现了三次

import java.util.*;

public class NumberAppearOnce {
	public int getNumber(int[] nums) {
		int[] bitSum = new int[32];
		Arrays.fill(bitSum, 0);

		for (int i = 0; i < nums.length; ++i) {
			int bitMask = 1;
			for (int j = 31; j >= 0; --j) {
				int bit = nums[i] & bitMask;
				if (bit != 0) {
					bitSum[j] += 1;
				}

				bitMask <<= 1;
			}
		}

		System.out.println(Arrays.toString(bitSum));

		int ret = 0;
		for (int m = 0; m < 32; ++m) {
			ret <<= 1;
			ret += bitSum[m] % 3;
		}

		return ret;
	}

	public void test(String testName, int[] nums, int expect) {
		int ret = getNumber(nums);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		NumberAppearOnce test = new NumberAppearOnce();
		int[] nums1 = {1,1,2,3,3,2,2,1,5,3};
		test.test("test-1", nums1, 5);

		int[] nums2 = {1,1,2,3,3,2,2,1,5,3,6,5,5};
		test.test("test-2", nums2, 6);
	}
}

// [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 7]
// test-1, expect: 5, result: 5
// [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 7, 9]
// test-2, expect: 6, result: 6