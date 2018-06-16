'''
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
'''

# 2018-6-16
# Regular Expression Matching


class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        # 匹配规则的第二个字符串不为*，当匹配字符串不为空的时候
        # 返回 两者的第一个元素是否相同，或匹配规则使用. and 递归新的字符串(去掉第一个字符的匹配字符串 和 去掉第一个字符的匹配规则)
        if p[1] != "*":
            if s == "":
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        # 当匹配字符串不为空 and (两者的第一个元素是否相同 or 匹配规则使用.)
        while s and (s[0] == p[0] or p[0] == '.'):
            # 到了while循环，说明p[1]为*，所以递归调用匹配s和p[2:](*号之后的匹配规则)
            # 用于跳出函数，当s循环到和*不匹配的时候，则开始去匹配p[2:]之后的规则
            if self.isMatch(s, p[2:]):
                return True
            # 当匹配字符串和匹配规则*都能匹配的时候，去掉第一个字符成为新的匹配字符串，循环
            s = s[1:]
        # 假如第一个字符和匹配规则不匹配，则去判断之后的是否匹配
        return self.isMatch(s, p[2:])


class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
        print(s,p)
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        else:
            return s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])

s = "aa"
p = "c*a*b"
test = Solution2()
res = test.isMatch(s,p)
if res:
    print("True")
else:
    print("False")