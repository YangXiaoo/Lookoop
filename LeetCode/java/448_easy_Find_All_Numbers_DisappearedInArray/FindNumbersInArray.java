/*
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
*/

// 2019-4-27
// 448. Find All Numbers Disappeared in an Array [easy]
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

import java.util.*;

public class FindNumbersInArray {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ret = new ArrayList<>();

        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == i + 1) {
                nums[i] = 0;
                continue;
            }
            if (nums[i] == 0) {
                continue;
            } 
            while (nums[nums[i]-1] != 0) {
                // System.out.println("[DEBUG] index: " + i +", curNumber: " + (nums[i]-1));
                int tmp = nums[i];
                nums[i] = nums[tmp-1];
                nums[tmp-1] = 0;   

                if (nums[i] == i + 1) {
                    nums[i] = 0;
                    break;
                }
   
            }
        }

        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != 0) {
                ret.add(i+1);
            }
        }

        return ret;
    }


    public List<Integer> findDisappearedNumbers2(int[] nums) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int cur = Math.abs(nums[i]);
            if (nums[cur - 1] > 0) nums[cur - 1] = 0 - nums[cur -  1];
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= 0) {
                res.add(i + 1);
            }
        }
        return res;
    }

    
    public void test(String testName, int[] nums, int[] expect) {
        List<Integer> ret = findDisappearedNumbers(nums);
        System.out.println(testName + ", ret: " + ret.toString() + ", expect: " + Arrays.toString(expect));
    }

    public static void main(String[] args) {
        FindNumbersInArray test = new FindNumbersInArray();
        int[] nums1 = {4,3,2,7,8,2,3,1};
        int[] expect1 = {5,6};
        test.test("test-1", nums1, expect1);

        int[] nums2 = {1,1};
        int[] expect2 = {2};
        test.test("test-2", nums2, expect2);

        int[] nums3 = {2,1};
        int[] expect3 = {};
        test.test("test-3", nums3, expect3);
    }
}