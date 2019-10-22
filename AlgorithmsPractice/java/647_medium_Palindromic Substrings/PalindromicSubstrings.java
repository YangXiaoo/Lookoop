/*
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
*/

// 2019-4-29
// 647. Palindromic Substrings [medium]
// https://leetcode.com/problems/palindromic-substrings/
// https://leetcode.com/problems/palindromic-substrings/discuss/277507/topic

import java.util.*;

public class PalindromicSubstrings {
class Solution {
    public int countSubstrings(String s) {
        List<String> list = new LinkedList<>();
        int pre = 0;
        int ret = 0;
        for (int i = 0; i < s.length(); ++i) {
        	int curListSize = list.size();
        	String curString = s.substring(i, i+1);
        	list.add(curString);
        	ret += 1;
        	int curSize = 1;
        	for (int j = curListSize - pre; j < curListSize; ++j) {
        		list.add(list.get(j) + curString);
        		curSize += 1;
                // System.out.println(list.toString() + ", pre: " + pre);
        		if (isPalindom(list.get(j) + curString)) {
        			ret += 1;
        		}
        	}

        	pre = curSize;
        }

        return ret;
    }

    public boolean isPalindom(String str) {
    	int left = 0, right = str.length() - 1;
    	while (left < right) {
    		if (str.charAt(left) != str.charAt(right)) {
    			return false;
    		}

    		left += 1;
    		right -= 1;
    	}

    	return true;
    }

 /**
     * 如果一个串是回文串，那么向左右两边各拓展一位，如果首尾字符相等，则新的串也是回文串；
     * 故选取中心点，往两边进行拓展，直到不是回文串为止；
     * 从中心拓展时分别考虑子串长度为奇、偶两种情况，如a->xax,aa->xaax；
     * 往两边拓展的时候需要考虑是否越界；
     */
    public int countSubstrings(String s) {
        int result = 0;

        // 一个字符串的每一个字符都可能成为中心点
        for (int i = 0; i < s.length(); i++) {
            // 以当前字符为中心点，子串长度为奇数的情况
            int start = i, end = i;

            // 条件为不越界并且首尾字符相等  满足条件则往两边拓展
            while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
                result++;
                start--;
                end++;
            }
            // 以当前字符为中心点，子串长度为偶数情况 重置首尾
            start = i;
            end = i + 1;
            //拓展条件和长度为奇数时一致
            while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
                result++;
                start--;
                end++;
            }
        }
        return result;
    }
}