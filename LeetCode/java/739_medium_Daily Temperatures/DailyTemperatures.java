/*
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
*/

// 2019-4-29
// 739. Daily Temperatures [medium]
// https://leetcode.com/problems/daily-temperatures/

import java.util.*;

public class DailyTemperatures {
    public int[] dailyTemperatures(int[] T) {
        int[] diffValue = new int[T.length + 1];
        int pre = T[0];
        for (int i = 0; i < T.length; ++i) {
        	diffValue[i] = T[i] - pre;
        	pre = T[i];
        }
        // System.out.println(Arrays.toString(diffValue));
        int[] ret = new int[T.length];
        for (int j = 1; j < diffValue.length; ++j) {
        	int cur = diffValue[j];
        	int right = j + 1;
        	while ((cur <= 0) && (right < diffValue.length)) {
        		cur += diffValue[right];
        		right += 1;
        	}
        	if (right == diffValue.length) {
        		ret[j-1] = 0;
        	} else {
        		ret[j-1] = right - j;
        	}
        	// System.out.println("right: " + right + ", j: " + j);
        }

        return ret;
    }
	
	public int[] dailyTemperatures2(int[] T) {
		int tLength = T.length;
		Stack<Integer> stack = new Stack<>();
		int[] ret = new int[tLength];

		for (int i = tLength - 1; i >= 0; --i) {
			while ((!stack.isEmpty()) && (T[stack.peek()] <= T[i])) {
				stack.pop();
			}

			if (stack.isEmpty()) {
				ret[i] = 0;
			} else {
				ret[i] = stack.peek() - i;
			}

			stack.push(i);
		}

		return ret;
	}

    public void test(String testName, int[] nums, int[] expect) {
    	int[] ret = dailyTemperatures2(nums);
    	System.out.println(testName + ", expect: " + Arrays.toString(expect) + ", result: " + Arrays.toString(ret));
    }

    public static void main(String[] args) {
    	DailyTemperatures test = new DailyTemperatures();

    	int[] nums1 = {73, 74, 75, 71, 69, 72, 76, 73};
    	int[] expect1 = {1, 1, 4, 2, 1, 1, 0, 0};

    	test.test("test-1", nums1, expect1);

    	int[] nums2 = {73,74,75,71,69,72,76,73,79,30,32};
    	int[] expect2 = {1,1,4,2,1,1,2,1,0,1,0};
    	test.test("test-2", nums2, expect2);

    }
}