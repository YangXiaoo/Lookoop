// 2019-4-22
// leetcode-03
// 最长不包含重复字符的子字符串
// 如, “arabcacfr”,最长不包含重复字符的子字符串是"acfr", 长度为4

import java.util.*;

public class LongestSubstringWithoutDup {
	public int longestSubstring(String str) {
		int[] index = new int[26];	// 每个字符的索引
		Arrays.fill(index, -1);

		int start = 0, maxLength = 0;
		for (int i = 0; i < str.length(); ++i) {
			int tmpStr = str.charAt(i) - 'a';
			int preIndex = index[tmpStr];
			if (preIndex > start) {
				start = preIndex + 1;
			}
			if ((i - start) > maxLength) {
				maxLength = i - start;
			}
			index[tmpStr] = i;
		}

		return maxLength;
	}

	public void test(String testName, String string, int expect) {
		int ret = longestSubstring(string);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		LongestSubstringWithoutDup test = new LongestSubstringWithoutDup();

		test.test("test1", "arabcacfr", 4);
		test.test("test2", "abcabcbb", 3);
		test.test("test3", "bbbbb", 1);
		test.test("test4", "pwwkew", 3);
	}
}