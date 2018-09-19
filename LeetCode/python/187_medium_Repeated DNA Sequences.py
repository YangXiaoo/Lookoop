'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

'''

# 2018-9-19
# 187. Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/description/

# 其他方法： https://www.cnblogs.com/grandyang/p/4284205.html

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        dic = {}
        for i in range(len(s)-9):
            sub = s[i : i + 10]
            if sub not in dic:
                dic[sub] = 1
            else:
                if sub not in res:
                    res.append(sub)

        return res

        
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAA"
test = Solution()
r = test.findRepeatedDnaSequences(s)
print(r)