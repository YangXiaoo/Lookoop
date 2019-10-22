'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
回文串: 是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

输入: "ccc"
输出: "ccc"

输入: "c"
输出: "c"

输入: "ccd"
输出: "cc"
'''
# 2018-6-15
# Longest Palindromic Substring

# 暴力破解(效率极差)
class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        ma = []
        max_str = ''
        leng = len(s)
        i = 0
        while i < leng - 1:
            j = leng - 1
            while j > i:
                if s[i] == s[j]:
                    st = s[i:j+1]
                    res.append(st)
                j -= 1
            i += 1
        print(res)
        if not res:
            return s[0]
        length = len(res)
        max_len = 0
        for n in range(0,length):
            ma.append(res[n])
            i = 0
            while i < (len(res[n])//2):
                if res[n][i] != res[n][len(res[n])-1-i]:
                    ma.pop()
                    break
                i += 1
        if not ma:
            return s[0]
        for m in range(0,len(ma)):
            if len(ma[m]) > max_len:
                max_len = len(ma[m]) 
                max_str = ma[m]
        return max_str



# Manacher’s Algorithm
# 复杂度o(n) 
# https://www.cnblogs.com/grandyang/p/4475985.html
'''
将所有可能的奇数/偶数长度的回文子串都转换成了奇数长度：在每个字符的两边都插入一个特殊的符号。abba => #a#b#b#a#， aba => #a#b#a#
'''
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#' # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
        lens = len(s)
        p = []                      # 辅助列表：p[i]表示i作中心的最长回文子串的长度
        id = 0                      # 最大回文子串中心位置
        mx = 0                      # 最大回文子串边界(右边界) mx = id + p[id]
        
        for i in range(lens):       # 遍历字符串
            if mx > i:
                count = min(mx-i, int(p[2*id-i]/2)+1)  
                # count == p[i]
            else :
                count = 1 # 初始回文子串长度为1，就是自身

            # 匹配
            # i - count: 最大长度不得超过左边边界
            while i-count >= 0 and i+count < lens and s[i-count] == s[i+count]:
                count += 1
            if(i-1+count) > mx:    # 更新影响范围最大的字符的右边界
                mx = i-1+count     # 当前id影响
                id = i
            p.append(count*2-1)

            print(p,count,mx,id)   # 更新回文子串最长长度
        maxd = max(p)
        position = int((maxd+1)/2)-1
        return position            # 去除特殊字符


class Solution3(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        while k < lenS - 1 and s[k] == s[k + 1]: k += 1 is very efficient and can handle both odd-length (abbba) and even-length (abbbba).
        """
        lenS = len(s)
        if lenS <= 1:
            return s
        minStart = 0
        maxLen = 1
        i =  0
        while i < lenS:
            if lenS - i <= maxLen / 2:
                break
            j = i 
            k = i
            while k < lenS - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while k < lenS - 1 and j and s[k + 1] == s[j - 1]:
                k = k + 1
                j = j - 1
            if k - j + 1 > maxLen:
                minStart = j
                maxLen = k - j + 1
        return s[minStart: minStart + maxLen]


# 动态规划法
'''
基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。如果头和尾不同，那么它最的长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。 
P[i,j]表示第i到第j个字符的回文子串数 
dp[i,i]=1
dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j]
dp[i,j]=max(dp[i+1,j],dp[i,j−1])|s[i]!=s[j]
'''
class Solution4(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """        
        n = len(s)
        maxl = 0
        start = 0
        for i in range(0,n):
            # 右边加一个字符
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1   # 回文字符多了一个
            # 右边加一个字符左边加一个字符
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1 
                maxl += 2  # 这里回文字符多了两个
        return s[start: start + maxl]

# test
# s = "rxabaabahiherereretmjk"
s = "ccabcbaewdf"
test = Solution4()
re = test.longestPalindrome(s)
print (re)


# practice
start = 0
maxl = 0
lens = len(s)
for i in range(lens):
    if i - maxl >= 0 and s[i-maxl:i+1] == s[i-maxl:i+1][::-1]:
        start = i -maxl
        maxl += 1        
    if i - maxl -1 >= 0 and s[i-maxl-1:i+1] == s[i-maxl-1:i+1][::-1]:
        start = i - maxl -1
        maxl += 2
print (s[start:start+maxl])


# Manacher's Algorithm
s = "#" + "#".join(s) + "#"
id = 0
mx = 0
p = []
lens = len(s)

for i in range(lens):
    if mx > i:
        count = min(p[2*id -i],mx-i)
    else:
        count = 1
    while i - count >= 0 and i + count < lens and s[i+count] == s[i-count]:
        count += 1
    if i - count +1 > mx:
        mx = i - count + 1
        id = i
    p.append(2*count - 1)
print (p)