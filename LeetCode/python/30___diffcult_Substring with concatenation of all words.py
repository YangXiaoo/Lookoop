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
# words里的字符串长度可能不一致，有问题
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
        for i in range(len(s) - word_len * word_size + 1): # words中的字符串必须在s中
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
                if cur_dict[word] > wordsMap[word]: # 字符串重复了
                    break
                j += 1
            if j == word_size: # 全部都在s中
                ans.append(i)
        return ans

# test
s = "barfoothefoobarman"
words = ["foo","bar"]
# test = Solution()
# res = test.findSubstring(s,words)
# print(res)

if len(words) == 0:
	print("[]")
words_map = {}
words_lens = len(words[0])
words_size = len(words)
for i in words:
	if i in words_map:
		words_map[i] += 1
	else:
		words_map[i] = 1
print(words_map)
res = []
n = 0
while n < (len(s)-words_lens*words_size +1):
	j = 0
	cur = {}
	while  j < words_size:
		word = s[n+j*words_lens:n + words_lens + j*words_lens]
		print(word)
		if word not in words_map:
			break
		if word not in cur:
			cur[word] = 1
		else:
			cur[word] += 1
		if cur[word] > words_map[word]:
			break
		j += 1
		if j ==  words_size:
			res.append(n)
	n += 1
print(res)

