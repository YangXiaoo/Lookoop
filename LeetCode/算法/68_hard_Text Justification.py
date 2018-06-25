"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

# 2018-6-23
# Text Justification
# So messy logical, i should find a new solution
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i = 0
        count = 0
        tmp = []
        res = []
        while i < len(words):
            # print(res)
            count += len(words[i]) + 1
            tmp.append(words[i])
            if count > maxWidth + 1:
                tmp.pop()
                res.append(tmp)
                tmp = []
                count = 0
                continue
            else:
                i += 1
        res.append(tmp)
        
        # print(res)
        # handle each line words
        line_tmp = []
        handle_line = []
        cc = 0
        for l in res:
            cc += 1
            s = ""
            dic = {}
            l_t = l.copy()
            l.pop()
            j = 0
            if cc==len(res):
                for kk in l_t:
                    s += kk + " "
                if len(s) > maxWidth:
                    s.rstrip(" ")
                else:
                    s += " "*(maxWidth-len(s)) 
                handle_line.append(s)
                continue
            if len(l_t) == 1:
                s = l_t[0] + " "*(maxWidth - len(l_t[0]))
                handle_line.append(s)
                continue
            while j < len(l):
                dic[j] = ""
                j += 1
            lens = 0
            for k in l_t:
                lens += len(k)
            spaces = maxWidth - lens
            n = 0
            m = 0
            while n < spaces:
                m = n%(len(l))
                dic[m] += " "
                n += 1
            # print(dic,handle_line,l,l_t,spaces,lens)
            k = 0
            while k < len(l_t):
                if k < len(dic):
                    s += l_t[k] + dic[k]
                else:
                    s += l_t[k]
                k += 1
            handle_line.append(s)
        return handle_line  



# test
words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
maxWidth = 16
test = Solution()
res = test.fullJustify(words,maxWidth)
print(res)

