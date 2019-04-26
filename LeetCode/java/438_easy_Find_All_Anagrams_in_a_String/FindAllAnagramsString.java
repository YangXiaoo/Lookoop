/*
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
*/

// 2019-4-26
// 438. Find All Anagrams in a String [easy]
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

import java.util.*;

public class FindAllAnagramsString {
    public List<Integer> findAnagrams(String s, String p) {
    	List<Integer> ret = new ArrayList<>();
    	int pLength = p.length(), sLength = s.length();

    	if (pLength > sLength) {
    		return ret;
    	}

    	int targetSum = 0;
        HashMap<Character,Integer> map = new HashMap<>();
        for (int i = 0; i < pLength; ++i) {
        	if (map.containsKey(p.charAt(i))) {
        		targetSum += map.get(p.charAt(i));
        	} else {
        		map.put(p.charAt(i), i+1);
        		targetSum += i + 1;
        	}
        }

        int[] index = new int[sLength];
        for (int i = 0; i < sLength; ++i) {
        	if (map.containsKey(s.charAt(i))) {
        		index[i] = map.get(s.charAt(i));
        	} else {
        		index[i] = 0;
        	}
        }

        List<Integer> tmp = new LinkedList<>();
        int curSum = 0;
        for (int i = 0; i < sLength; ++i) {
        	tmp.add(i);
        	curSum += index[i];
        	if (tmp.size() == pLength) {
        		if (curSum == targetSum) {
        			ret.add(tmp.get(0));
        		}
        		curSum -= index[tmp.get(0)];
        		tmp.remove(0);
        	}
        }

        return ret;
    }

	public List<Integer> findAnagrams2(String s, String p) {
    	List<Integer> ret = new ArrayList<>();
    	int pLength = p.length(), sLength = s.length();

    	if (pLength > sLength) {
    		return ret;
    	}

		// 用数组替代字典
		int[] index = new int[26];
		Arrays.fill(index, 0);
		int traget = 0;
		for (int i = 0; i < pLength; ++i) {
			if (index[p.charAt(i) - 'a'] == 0){
				index[p.charAt(i) - 'a'] = i+1;
				traget += i + 1;
			} else {
				traget += index[p.charAt(i) - 'a'];
			}
			
		}
		System.out.println(Arrays.toString(index));

		List<Integer> tmp = new LinkedList<>();
		int curSum = 0;
		for (int j = 0; j < sLength; ++j) {
			tmp.add(j);
			curSum += index[s.charAt(j) - 'a'];
			System.out.println(tmp.toString() + ", curSum: " + curSum);
			if (tmp.size() == pLength) {
				if (curSum == traget) {
					ret.add(tmp.get(0));
				}
				curSum -= index[s.charAt(tmp.get(0)) - 'a'];
				tmp.remove(0);
			}
		}

		return ret;
	}



    public void test(String testName, String s, String p, List<Integer> expect) {
    	List<Integer> ret = findAnagrams2(s, p);
    	System.out.println(testName + ", ret: " + ret.toString() + ", expect: " + expect.toString());
    }

    public static void main(String[] args) {
    	FindAllAnagramsString test = new FindAllAnagramsString();
    	List<Integer> expect1 = new ArrayList<>(Arrays.asList(0,6));
    	test.test("test-1", "cbaebabacd", "abc", expect1);

    	List<Integer> expect2 = new ArrayList<>(Arrays.asList(1));
    	test.test("test-2", "baa", "aa", expect2);
    }
}