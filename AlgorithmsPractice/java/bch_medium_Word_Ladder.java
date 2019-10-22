/**
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
*/

// 2018-7-20
// 127. Word Ladder
// LTE
class bch_medium_Word_Ladder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<String> queue = new LinkedList<>();
        HashMap<String, Integer> map = new HashMap<>();
        
        if (beginWord.length() != endWord.length() || !wordList.contains(endWord)) return 0;

        // 入栈
        queue.offer(beginWord);
        // 加入字典中
        map.put(beginWord, 1);

        if (wordList.contains(beginWord)) wordList.remove(beginWord);

        while (!queue.isEmpty()) {
            String top = queue.poll();
            int lens = map.get(top);
            int wordLens = top.length();
            StringBuilder builer;

            for (int i = 0; i < wordLens; i++) {
                builer = new StringBuilder(top);
                for (char c = 'a'; c <= 'z'; c++) {
                    // 新的字符串
                    builer.setCharAt(i, c);
                    String tmp = builer.toString();

                    if (tmp.equals(top)) continue;
                    if (tmp.equals(endWord)) return lens + 1;

                    if (wordList.contains(tmp)) {
                        // 入栈
                        queue.offer(tmp);
                        // 删除遍历过的字符串
                        wordList.remove(tmp);
                        map.put(tmp, lens + 1);
                    } // ~~~ end id
                } // ~~~ end for loop
            } // ~~~ end for loop
        } // ~~~ end while loop
        return 0;
    }
}