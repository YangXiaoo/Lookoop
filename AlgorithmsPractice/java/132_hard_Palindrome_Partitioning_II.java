/**
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
*/

// 2018-7-23
// 132. Palindrome Partitioning II
// LTE
class 132_hard_Palindrome_Partitioning_II {
    public int minCut(String s) {
        List<Integer> res = new ArrayList<>();
        res.add(s.length() - 1);
        List<String> tmp = new ArrayList<String>();

        dfs(res, s, tmp, 0);

        return res.get(res.size() - 1);
    }

    public void dfs(List<Integer> res, String s, List<String> tmp, int index) {
        if (s.length() == index) {
            if (tmp.size() - 1 < res.get(res.size() - 1)) {
                res.add(tmp.size() - 1);
                //System.out.println(res);
            }
        }

        for (int i = index + 1; i <= s.length(); i++) {
            String tmpStr = s.substring(index, i);
            if (!isPalindrome(tmpStr)) continue;
            tmp.add(tmpStr);
            dfs(res, s, tmp, i);
            tmp.remove(tmp.size() - 1);
        }
        
    }

    private boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }
}