/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
*/

// 2019-4-27
// 461. Hamming Distance [easy]
// https://leetcode.com/problems/hamming-distance

import java.util.*;

// 异或结果中1的个数
class HammingDistance {
    public int hammingDistance(int x, int y) {
        int xor = x ^ y;	// 异或
        int count = 0;
        for (int i = 0; i < 32; ++i) {
        	count += (xor >> i) & 1;	// 统计异或结果中1的个数
        }

        return count;
    }

    public void test(String testName, int x, int y, int expect) {
        int ret = hammingDistance(x, y);
        System.out.println(testName + ", ret: " + ret + ", expect: " + expect);
    }

    public static void main(String[] args) {
    	HammingDistance test = new HammingDistance();
    	test.test("test-1", 1, 4, 2);
    }
}