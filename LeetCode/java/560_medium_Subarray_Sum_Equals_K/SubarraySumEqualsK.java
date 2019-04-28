/*
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
*/

// 2019-4-28
// 560. Subarray Sum Equals K [medium]
// https://leetcode.com/problems/subarray-sum-equals-k/
import java.util.*;

public class SubarraySumEqualsK {

	// Time Limit Exceeded 58/80
    public int subarraySum(int[] nums, int k) {
    	if (nums.length == 0) return 0;

        List<Long> list = new LinkedList<>();
        int ret = 0, pre = 0;

        for (int i = 0; i < nums.length; ++i) {
        	int listSize = list.size();
        	list.add((long)nums[i]);	// 先将当前数字添加到列表中
        	int curSize = 1;
        	for (int j = listSize - pre; j < listSize; ++j) {
        		list.add(list.get(j) + (long)nums[i]);
        		curSize += 1;
        	}
        	pre = curSize;
        }

        for (int i = 0; i < list.size(); ++i) {
        	if (list.get(i) == (long)k) {
        		ret += 1;
        	}
        }

        return ret;
    }

    // TLE
	public int subarraySum2(int[] nums, int k) {
    	if (nums.length == 0) return 0;

        List<Long> list = new ArrayList<>();
        int ret = 0, pre = 0;

        for (int i = 0; i < nums.length; ++i) {
        	int listSize = list.size();
        	list.add((long)nums[i]);	// 先将当前数字添加到列表中

        	if (nums[i] == k)
        		ret += 1;

        	int curSize = 1;	// 记录当前添加的数组序列
        	for (int j = listSize - pre; j < listSize; ++j) {
        		list.add(list.get(j) + (long)nums[i]);
        		if ((list.get(j) + (long)nums[i]) == (long)k) {
        			ret += 1;
        		}
        		curSize += 1;
        	}
        	pre = curSize;	// pre 作为上一个数字添加的序列数
        }

        return ret;

	}

	// 使用map
	// sum(i, j) == (sum(0, j) - sum(0, i))
	public int subarraySum3(int[] nums, int k) {
		HashMap<Integer, Integer> map = new HashMap<>();
		map.put(0, 1);
		int sum = 0, ret = 0;

		for (int n : nums) {
			sum += n;
			int sub = sum - k;	// 从当前点往前的范围是否存在sum(i,j) == k, 
								// 即 sum(0, i) = sum(0, j) - sum(i, j)

			if (map.containsKey(sub)) {
				ret += map.get(sub);
			}

			if (!map.containsKey(sum)) {
				map.put(sum, 1);	// 当前sum添加到map作为sum(0, i)
			} else {
				map.put(sum, map.get(sum) + 1);
			}
		}

		return ret;
	}

    public void test(String testName, int[] nums, int k, int expect) {
    	int ret = subarraySum3(nums, k);
    	System.out.println(testName + ", expect: " + expect + ", result: " + ret);
    }

    public static void main(String[] args) {
    	SubarraySumEqualsK test = new SubarraySumEqualsK();
    	
    	int[] nums1 = {1,1,1};
    	test.test("test-1", nums1, 2, 2);

    }
}