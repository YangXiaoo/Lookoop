// 2019-4-22
// 把数组排成最小的数
// 如, 输入数组{3,32,321}, 则打印出这三个数字能排成的最小数字321323

import java.util.*;

public class SortArrayForMinNumber {
	public long sortArray(int[] nums) {
		String[] strNum = new String[nums.length];
		for (int i = 0; i < nums.length; ++i)
			strNum[i] = String.valueOf(nums[i]);

		Arrays.sort(strNum);
		System.out.println(Arrays.toString(strNum));

		for (int j = 1; j < strNum.length; ++j) {
			String rightValue = strNum[j - 1] + strNum[j];	// 前后组合
			String leftValue = strNum[j] + strNum[j - 1];	// 后前组合
			if (Long.parseLong(rightValue) < Long.parseLong(leftValue)) {
				strNum[j] = rightValue;
			} else {
				strNum[j] = leftValue;
			}
		}

		return Long.parseLong(strNum[strNum.length-1]);
	}

	public void test(String testName, int[] array, long expect) {
		long ret = sortArray(array);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		SortArrayForMinNumber test = new SortArrayForMinNumber();
		int[] array = {3,32,321};
		test.test("test1", array, 321323);
	}

}