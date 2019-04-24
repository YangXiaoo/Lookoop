// 2019-4-23
// 数组中数字出现的次数
// 求数组中只出现一次的两个数字，除这两个数字之外其余都出现了两次。

import java.util.*;

public class NumberAppearOnce {
	public int[] getNumbers(int[] nums) {
		if (nums.length < 3) return nums;
		// 两个数字不相同那么肯定在某个位上两个数字求^不等于0， 
		// 找到这个位在哪里，将数组分为两部分
		int bitSum = getBitSum(nums);

		int index = getIndex(bitSum);
		System.out.println("index: " + index);


		int left = 0, right = 0;
		for (int i = 0; i < nums.length; ++i) {
			// System.out.println( (nums[i] >> index) & 1 );
			if (((nums[i] >> index) & 1) == 1) {
				left ^= nums[i];
			} else {
				right ^= nums[i];
			}
		}

		int[] ret = {left, right};

		return ret;
	}

	// 位运算和
	public int getBitSum(int[] nums) {
		int ret = nums[0];

		for (int i = 1; i < nums.length; ++i) {
			ret ^= nums[i];
		}

		return ret;
	}

	// 右边第一位为1的索引
	public int getIndex(int num) {
		int index = 0;
		while (index < 32) {
			if ((num & 1) == 1) {
				break;
			}
			index += 1;
			num >>= 1;
		}

		return index;
	}

	public void test(String testName, int[] nums, int[] expect) {
		int[] ret = getNumbers(nums);
		System.out.println(testName + ", expect: " + Arrays.toString(expect) + ", result: " + Arrays.toString(ret));
	}

	public static void main(String[] args) {
		NumberAppearOnce test = new NumberAppearOnce();
		int[] nums1 = {1,1,2,3,4,4,5,5};
		int[] expect1 = {2,3};
		test.test("test-1", nums1, expect1);

		int[] nums2 = {1,1,2,3,4,4,5,5,2,7,8,8};
		int[] expect2 = {3,7};
		test.test("test-2", nums2, expect2);
	}
}

// index: 0
// test-1, expect: [2, 3], result: [3, 2]
// index: 2
// test-2, expect: [3, 7], result: [7, 3]