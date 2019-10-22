/**

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
*/

// 2018-7-22
// 131. Palindrome Partitioning
class 131_medium_Palindrome_Partitioning {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<List<String>>();
        List<String> tmp = new ArrayList<String>();
        dfs(s, 0, res, tmp);

        return res;
    }

    public void dfs(String s, int index, List<List<String>> res, List<String> tmp) {
    	if (index == s.length()) {
    		res.add(new ArrayList<String>(tmp));
    		return;
    	}
        
    	for (int i = index + 1; i <= s.length(); i++) {
    		String sub = s.substring(index, i);
    		if (!isPalidrome(sub)) continue;
    		tmp.add(sub);
    		dfs(s, i, res, tmp);
    		tmp.remove(tmp.size() - 1);
    	}
    }

    public boolean isPalidrome(String s) {
    	int left = 0, right = s.length() - 1;

    	while ( left < right) {
    		if (s.charAt(left) != s.charAt(right)) return false;
    		left++;
    		right--;
    	}

    	return true;
    }
}