/*
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
*/

// 2019-4-28
// 581. Shortest Unsorted Continuous Subarray [medium]
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
import java.util.*;

public class ShortestUnsortedContinuousSubarray {
    public int findUnsortedSubarray(int[] nums) {
		int[] numsCopy = Arrays.copyOf(nums, nums.length);
		Arrays.sort(numsCopy);

		// 获得左边变动索引
		int left = 0;
		for (int i = 0; i < nums.length; ++i) {
			left = i;
			if (nums[i] != numsCopy[i]) {
				break;
			}
		}
		// 获得右边变动索引
		int right = nums.length;
		for (int j = nums.length - 1; j >= left; --j) {
			right = j;
			if (nums[j] != numsCopy[j]) {
				right += 1;
				break;
			}
		}

		return right - left;
    }

	public int findUnsortedSubarray2(int[] nums) {
		int n = nums.length;
		int max = nums[0] , min = nums[nums.length-1];
		int left = 0, right = 0;
		for (int i = 0; i < n; ++i) {
			max = Math.max(max, nums[i]);
			if (max != nums[i]) right = i;

			min = Math.min(min, nums[n - i - 1]);
			if (min != nums[n - i - 1]) left = n - i - 1;
		}

		return right == left ? 0 : right - left + 1;
	}

    public void test(String testName, int[] nums, int expect) {
    	int ret = findUnsortedSubarray2(nums);
    	System.out.println(testName + ", expect: " + expect + ", result: " + ret);
    }

    public static void main(String[] args) {
    	ShortestUnsortedContinuousSubarray test = new ShortestUnsortedContinuousSubarray();

    	int[] nums1 = {1,2,3,4};
    	test.test("test-1", nums1, 0);

		int[] nums2 = {2, 6, 4, 8, 10, 9, 15};
		test.test("test-2", nums2, 5);

		int[] nums3 = {2,1};
		test.test("test-3", nums3, 2);

		int[] nums4 = {1};
		test.test("test-4", nums4, 0);
    }
}