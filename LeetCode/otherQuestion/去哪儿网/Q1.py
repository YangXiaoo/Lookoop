# coding:utf-8

"""
设有n维数组，元素分别为a00  a01 ... a0(n-1) a10 a11 ... a1(n-1) ... ... a(n-1)0 a(n-1)1 ... a(n-1)(n-1)，求其相加和最大子数组的值max

输入
n

a00  a01 ... a0(n-1) a10 a11 ... a1(n-1) ... ... a(n-1)0 a(n-1)1 ... a(n-1)(n-1)

（数据范围：n在1到100之间，每个数在-128到127之间）

输出
max


样例输入
2
-1 2 -3 6
样例输出
8
"""
# ac 83%
def solver(n, nums):
    dp = [[0 for _ in range(len(nums[0]))] for _ in range(n)] # init dp
    maxRet = float("-inf")
    tmp = 0
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            dp[i][j] = nums[i][j]
            if tmp < 0:
                tmp = nums[i][j]
            else:
                tmp += nums[i][j]

            if tmp > dp[i][j]:
                dp[i][j] = tmp

            maxRet = max(maxRet, dp[i][j])

    tmp = 0
    for j in range(len(nums[0])):
        for i in range(len(nums)):
            dp[i][j] = nums[i][j]
            if tmp < 0:
                tmp = nums[i][j]
            else:
                tmp += nums[i][j]

            if tmp > dp[i][j]:
                dp[i][j] = tmp
            maxRet = max(maxRet, dp[i][j])
    # print(dp)

    for i in range(1,n):
        for j in range(1,n):
            up = dp[i-1][j]
            left = dp[i][j-1]
            maxP = max(up, left)
            dp[i][j] = max(dp[i][j], dp[i][j])
            maxRet = max(maxRet, dp[i][j])

    return maxRet

def test():
    n = 2
    s = "-1 2 -3 6"
    snums = list(map(int, s.split(" ")))
    nums = []
    for i in range(n):
        end = len(snums)//n
        nums.append(snums[i*end:(i*end+end)])
    # print(nums)
    ret = solver(n, nums)
    print(ret)

def inputs():
    n = int(input().strip())
    s = input().strip()
    snums = list(map(int, s.split(" ")))
    nums = []
    for i in range(n):
        end = len(snums)//n
        nums.append(snums[i*end:(i*end+end)])
    ret = solver(n, nums)
    print(ret)

if __name__ == '__main__':
    test()
