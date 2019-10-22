# coding:utf-8
# 版本号比较，第二个版本号高于第一个时才输出true
# 6.6.6 6.6.7
# 1 1.0
# 输出
# true
# false
import sys

# AC 100%
def solver(nums):
    ret = []
    for line in nums:
        # 判断
        f, s = line[0], line[1]
        fNums = list(map(int, f.split(".")))
        sNums = list(map(int, s.split(".")))
        maxLens = max(len(fNums), len(sNums))
        flag = True
        # print(fNums, sNums)
        for i in range(maxLens):
            fDigit = 0
            if i < len(fNums):
                fDigit = fNums[i]
            sDigit = 0
            if i < len(sNums):
                sDigit = sNums[i]
            if fDigit > sDigit:
                ret.append("false")
                flag = False 
                break
            elif fDigit < sDigit:
                ret.append("true")
                flag = False
                break
        if flag:    # 平
            ret.append("false")

    return ret 

def test():
    nums = [["6.6.6", "6.6.7"],
            ["1", "1.0"]]

    ret = solver(nums)
    printRet(ret)

def printRet(ret):
    for n in ret:
        print(n)

def inputs():
    n = int(sys.stdin.readline().strip())
    nums = []
    for i in range(n):
        cur = list(sys.stdin.readline().strip().split(" "))
        nums.append(cur)

    ret = solver(nums)
    printRet(ret)
if __name__ == '__main__':
    inputs()
