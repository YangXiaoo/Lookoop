"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/./b/../c/", => "/a/c"
path = "/a/./b/c/", => "/a/b/c"，
path = "/...", => "/..."
click to show corner cases.

Corner Cases:

Did you consider the case where path = "/../"?
first case is /a/./, we should skip /./
In this case, you should return "/".
Another corner case(极端情况; 边界情况;)is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
# 2018-6-24
# Simplify Path
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr = path.split("/")
        # print(arr)
        i = 0
        tmp = []
        while i < len(arr):
        	if arr[i] == '.':
        		i += 1
        		continue
        	elif arr[i] == '..':
        		try:
        			tmp.pop()
        		except:
        			pass
        		i += 1
        		continue
        	elif arr[i] == '':
        		i += 1
        		continue
        	else:
        		tmp.append(arr[i])
        		i += 1
        # print(tmp)
        res = ""
        if tmp == []:
        	return "/"
        # print(tmp)
        for j in range(len(tmp)):
        	res += "/" + tmp[j]
       	return res



# test
path = "/a/./b/../c/"
test = Solution()
res = test.simplifyPath(path)
print(res)        
