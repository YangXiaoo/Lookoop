/**
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
*/

// 2018-7-24
// 139. Word Break
// https://blog.csdn.net/mine_song/article/details/72081998
class 139_medium_Word_Break {
    public boolean wordBreak(String s, List<String> wordDict) {
        return dfs(0, 0, s, wordDict);
    }

    private boolean dfs(int start, int index, String s, List<String> dic) {
        if (index == s.length()) return true;

        for (int i = start; i < dic.length; i++) {
            String curStr = dic.get(i);
            int lens = curStr.length;
            String sub = s.subString(index, lens);
            if (sub != curStr) continue;
            dfs(0, index + lens, s, dic);
            index -= lens;
        }
    }
}