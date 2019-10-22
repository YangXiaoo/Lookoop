/**
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
*/

// 2018-7-19
// 126. Word Ladder II

class Pair {
    String str;
    ArrayList<String> path;
    HashSet<String> hash;
    Pair(String str, ArrayList<String> path, HashSet<String> hash) {
        this.str  = str;
        this.path = path;
        this.hash = hash;
    }
}
 
 
public class bcg_hard_Word_Ladder_II {
    
    public ArrayList<ArrayList<String>> findLadders(String start, String end, HashSet<String> dict) {
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        ArrayList<String> path = new ArrayList<String>();
        HashSet<String>   hash = new HashSet<String>();

        // 特殊情况
        if(start==null||end==null||start.length()!=end.length()) {
            return result;
        }

        Queue queue = new LinkedList<Pair>(); // 每一层
        path.add(start);  // 遍历路径队列，从start开始寻找
        hash.add(start);  // hash表查看是否重复
        Pair   node = new Pair(start, path, hash);  // 创建图
        int min_length = -1;
        queue.add(node);

        while(!queue.isEmpty()) {
            node = (Pair)queue.poll(); // 弹出节点
            String str = node.str;  // 验证的字符串

            for(int i=0;i<str.length();i++) {
                char[] strCharArr = str.toCharArray(); // 转换为数组
                for(char ch='a';ch<='z';ch++) {
                    if(strCharArr[i]==ch) { // 找一个相差一位的字符组成新的字符串
                        continue;
                    }
                    strCharArr[i] = ch; // 组成新的字符串
                    String newWord = new String(strCharArr);

                    if(newWord.equals(end)==true) { // 如果和endword相同则
                        path = node.path;
                        path.add(newWord);
                        if(min_length==-1) {
                            min_length = path.size();
                        }
                        if(path.size()>min_length) { // 
                            return result;
                        } else {
                            result.add(path);
                            //dict.remove(newWord);
                            continue;
                        }
                    } else {
                        // 可以添加形成新路
                        if(dict.contains(newWord)&&!node.hash.contains(newWord)){
                            path = new ArrayList<String>(node.path); // 将node.path赋予path，下面相同 
                            hash = new HashSet<String>(node.hash);
                            path.add(newWord);
                            hash.add(newWord);
                            Pair newnode = new Pair(newWord, path, hash);
                            queue.add(newnode);
                            //dict.remove(newWord);
                        }
                    } // ~~~if else结束
                } // ~~~ 内层for结束
            } // ~~~ 外层for结束
        } // ~~~ end while
        return result;
    }
}
