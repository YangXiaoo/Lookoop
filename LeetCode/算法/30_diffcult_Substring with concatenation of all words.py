'''
You are given a string, s, and a list of words, words, that are all of the same length.
 Find all starting indices of substring(s) in s that is a concatenation(一切事物的相关连接) of each word
  in words exactly once and without any intervening(中间) characters.

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
'''

# 2018-6-19
# Substring with concatenation of all words

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        wordsMap = {}
        for word in words:
            if word not in wordsMap:
                wordsMap[word] = 1
            else:
                wordsMap[word] += 1
        word_len = len(words[0])
        word_size = len(words)
        ans = []
        for i in range(len(s) - word_len * word_size + 1):
            j = 0
            cur_dict = {}
            while j < word_size:
                word = s[i + word_len * j:i + word_len * j + word_len]
                if word not in wordsMap:
                    break
                if word not in cur_dict:
                    cur_dict[word] = 1
                else:
                    cur_dict[word] += 1
                if cur_dict[word] > wordsMap[word]:
                    break
                j += 1
            if j == word_size:
                ans.append(i)
        return ans

s = "barfoothefoobarman"
words = ["foo","bar"]
test = Solution()
res = test.findSubstring(s,words)
print(res)