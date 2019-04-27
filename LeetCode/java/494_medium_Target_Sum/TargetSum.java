/*
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
*/

// 2019-4-27
// 494. Target Sum [medium]
// https://leetcode.com/problems/target-sum/

import java.util.*;

public class TargetSum {
	private int sum = 0;
	private int ret = 0;

	// Status: Time Limit Exceeded
 public int findTargetSumWays(int[] nums, int S) {
    	this.sum = S;
    	int ret = 0;
    	Deque<Integer> queue = new LinkedList<>();
    	if (nums.length < 1) {
    		return ret;
    	}
        queue.offerFirst(nums[0]);
        queue.offerFirst(0-nums[0]);

        for (int i = 1; i < nums.length; ++i) {
        	int curSize = queue.size();
        	for (int j = 0; j < curSize; ++j) {
        		int tmpSum = queue.pollLast();
        		queue.offerFirst(tmpSum+nums[i]);
        		queue.offerFirst(tmpSum-nums[i]);
        	}
        }
        // System.out.println("deque: " + queue.toString() + ", deque.size(): " + queue.size());
        int queueSize = queue.size();
        for (int k = 0; k < queueSize; ++k) {
        	int curSum = queue.pop();
        	if (curSum == sum) {
        		ret += 1;
        	}
        	// System.out.println("deque: " + queue.toString() + ", deque.size(): " + queue.size() + ", k: " + k);
        }

        return ret;
    }

    // AC
	public int findTargetSumWays2(int[] nums, int S) {
		this.sum = S;
		this.ret = 0;
		helper(nums, 0, 0);

		return ret;
	}

	public void helper(int[] nums, int tmpSum, int index) {
		if (index > nums.length) return;

		if (index == nums.length) {
			if (tmpSum == sum) {
				ret += 1;
			}
		} else {
			int nextIndex = index + 1;
			helper(nums, tmpSum+nums[index], nextIndex);
			helper(nums, tmpSum-nums[index], nextIndex);
		}
	}

    public void test(String testName, int[] nums, int s, int expect) {
    	int ret = findTargetSumWays2(nums, s);
    	System.out.println(testName + ", ret: " + ret + ", expect: " + expect);
    }

    public static void main(String[] args) {
    	TargetSum test = new TargetSum();

    	int[] nums1 = {1, 1, 1, 1, 1};
    	test.test("test-1", nums1, 3, 5);

    	int[] nums2 = {1};
    	test.test("test-2", nums2, 1, 1);
    }
}