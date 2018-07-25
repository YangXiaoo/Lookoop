/**
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
*/

// 2018-7-24
// 140. Word Break II
// https://www.cnblogs.com/springfor/p/3877056.html
// https://blog.csdn.net/zdavb/article/details/47755365
// ????????????????????????????????????????????????????????????????????????????
// DFS
class 140_hard_Word_Break_II {
    public List<String> wordBreak(String s, List<String> wordDict) {
    	List<String> res = new ArrayList<String>();
    	List<String> tmp = new ArrayList<String>();
        dfs(0, s, wordDict, res, tmp);
        return res;
    }

    private void dfs(int index, String s, List<String> dic, List<String> res, List<String> tmp) {
        if (index == s.length()) {
        	StringBuilder subRes = new StringBuilder();
        	for (int j = 0; j < tmp.size(); j++) {
        		subRes.append(tmp.get(j));
        		if (j < tmp.size() - 1) subRes.append(" ");
        	} 
            String t = subRes.toString();
        	res.add(t); 
            System.out.println(subRes);
        	return;       	
        }

        for (int i = 0; i < dic.size(); i++) {
            String curStr = dic.get(i);
            int lens = curStr.length();
            if (index + lens > s.length()) continue;
            String sub = s.substring(index, lens);
            if (sub != curStr) continue;
            tmp.add(curStr);
            index += lens;
            dfs(index, s, dic, res, tmp);
            String last = tmp.get(tmp.size() - 1);
            tmp.remove(tmp.size() - 1);
            index -= last.length();
        }
    }
}