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

// dfs
class 139_medium_Word_Break {
    public boolean wordBreak(String s, List<String> wordDict) {
        return dfs(0, 0, s, wordDict, 0);
    }

    private boolean dfs(int start, int index, String s, List<String> dic, int flag) {
        if (index == s.length()) flag = 1;

        for (int i = start; i < dic.size(); i++) {
            String curStr = dic.get(i);
            int lens = curStr.length();
            if (index + lens > s.length()) continue;
            String sub = s.substring(index, lens);
            if (sub != curStr) continue;
            index += lens;
            dfs(0, index, s, dic, flag);
            index -= lens;
        }
        System.out.println(index);
        return flag == 1;
    }
}

class Solution2 {
    public boolean wordBreak(String s, List<String> wordDict) {
        if (wordDict.contains(s)) return true;
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(0);
        Set<Integer> visit = new HashSet<Integer>();
        visit.add(0);

        while (!queue.isEmpty()) {
            int curIndex = queue.poll();

            for (int i = curIndex + 1; i <= s.length(); i++) {
                if (visit.contains(i)) continue;

                if (wordDict.contains(s.substring(curIndex, i ))) {
                    if (i == s.length()) return true;
                    queue.offer(i);
                    visit.add(i);
                }
            }
        }

        return false;
    }
}

class Solution3 {
    Set<String> map = new HashSet();
    public boolean wordBreak(String s, List<String> wordDict) {
        if(wordDict.contains(s)) return true;
        if(map.contains(s)) return false;
        for(String word : wordDict){
            if(s.startsWith(word)){
                if(wordBreak(s.substring(word.length()), wordDict)) return true;
            }
        }
        map.add(s);
        return false;
    }
}