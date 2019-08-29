# codig:utf-8
"""
求最长的特殊子序列
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
现有一个长度为n的序列，需要你求出最长的子序列，使得其长度最长，并且这个子序列是满足性质C的

子序列的定义：现有,则为一个子序列

性质C的定义：现有子序列，若,则称子序列满足性质C 

输入
第一行一个数n，代表序列的长度 接下来一行n个数ai，代表序列中的每个数

1≤n≤100000,1≤ai≤n

输出
一行一个数，代表最长的满足性质C的子序列的长度 


样例输入
5
1 2 1 3 4
样例输出
4
"""
def solver1(n, nums):
    dp = [0 for _ in range(n)]  # 定义长度
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])


    return max(dp)

from bisect import bisect_left
def solver(n, nums):
    ret = []
    for i in range(n):
        index = bisect_left(ret, nums[i])
        # print(index)
        if len(ret) == index:
            ret.append(nums[i])
        else:
            ret[index] = nums[i]
    return len(ret)

def inputs():
    n = int(input())
    nums = list(map(int, input().split(" ")))
        
    ret = solver(n, nums)
    print(ret)

def test():
    n, nums = 5, [1,2,1,3,4]
    ret = solver(n, nums)
    print(ret)

if __name__ == '__main__':
    test()