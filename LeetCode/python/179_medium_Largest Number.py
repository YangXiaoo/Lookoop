'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

# 2018-9-18
# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        tmp = []
        for i in nums:
            tmp.append(str(i))
        # tmp = sorted(tmp)
        def swap(i, j):
            t = tmp[i]
            tmp[i] = tmp[j]
            tmp[j] = t
        lens = len(nums) - 1
        i = 0
        while i < lens :
            j = 0
            while j < lens - i:
                c = 0
                iscontinue = True
                while c < min(len(tmp[j+1]), len(tmp[j])):
                    if tmp[j+1][c] < tmp[j][c]:
                        swap(j+1, j)
                        c += 1
                        iscontinue = False
                        break
                    elif tmp[j+1][c] == tmp[j][c]:
                        c += 1
                        continue
                    else:
                        iscontinue = False
                        c += 1
                        break
                if iscontinue:
                    p = c - 1
                    if c == len(tmp[j+1]):
                        while c < len(tmp[j]):
                            if tmp[j+1][p] < tmp[j][c]:
                                swap(j+1, j)
                                c += 1
                                iscontinue = False
                                break
                            elif tmp[j+1][p] == tmp[j][c]:
                                c += 1
                                continue
                            else:
                                iscontinue = False
                                break
                    if iscontinue:
                        if c == len(tmp[j]):
                            while c < len(tmp[j+1]):
                                if tmp[j+1][c] < tmp[j][p]:
                                    swap(j+1, j)
                                    c += 1
                                    break
                                elif tmp[j+1][c] == tmp[j][p]:
                                    c += 1
                                    continue
                                else:
                                    break
                j += 1
            i += 1

        print(tmp)
        tmp = tmp[::-1]
        return str(int("".join(tmp)))


class Solution2(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        tmp = []
        for i in nums:
            tmp.append(str(i))
        # tmp = sorted(tmp)
        def swap(i, j):
            t = tmp[i]
            tmp[i] = tmp[j]
            tmp[j] = t
        lens = len(nums) - 1
        i = 0
        while i < lens :
            j = 0
            while j < lens - i:
                if int(tmp[j] + tmp[j + 1]) > int(tmp[j + 1] + tmp[j]):
                    swap(j, j + 1)
                j += 1
            i += 1

        print(tmp)
        tmp = tmp[::-1]
        return str(int("".join(tmp)))


class Solution3(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return ""
        

        
        def sort_cmp(a, b):
            if a+b > b + a:
                return -1
            return 1
        
        nums_lists = map(str, nums)
        nums_lists.sort(cmp=sort_cmp)
        # nums_lists.reverse()
        
        a = reduce(lambda a,b: a + b, nums_lists)
        s = "".join(map(lambda n: str(n), a)).lstrip("0")
        return s if len(s) > 0 else "0"



nums = [3,30,34,5,9,314]
test = Solution2()
r  = test.largestNumber(nums)
print(r)

        