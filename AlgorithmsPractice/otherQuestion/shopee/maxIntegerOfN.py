# coding=utf-8
import copy
def getNumber(n):
    """通过n获得n的每位数字"""
    strN = str(n)
    ret = [x for x in strN]

    return ret 

def getAssemble(nums):
    ret = []
    ret.append(nums[:])
    length = len(nums)

    for i in range(length):
        j = i + 1
        tmp = []
        for k in range(j, length):
            for num in ret:
                curNum = copy.deepcopy(num)
                curNum[i], curNum[k] = curNum[k], curNum[i]
                if curNum not in tmp:
                    tmp.append(curNum)

        ret.extend(tmp)
    lastRet = []
    for num in ret:
        lastRet.append(int("".join(num)))
    return lastRet

def getMaxIntegerOfN(nums, n):
    lessThanN = []
    for num in nums:
        if num < n:
            lessThanN.append(num)
    if len(lessThanN) == 0:
        return 0
    lessThanN.sort(reverse=True)
    return lessThanN[0]

def solver(n):
    nums = getNumber(n)
    assemble = getAssemble(nums)
    ret = getMaxIntegerOfN(assemble, n)

    return ret
#######################################
def dfs(nums, ret, index):
    if index == len(nums):
        return
    if nums not in ret:
        ret.append(nums)
    for i in range(index, len(nums)):
        idx = nextMax(nums, i)
        if idx == -1:
            dfs(nums, ret, i + 1)
            continue
        cur = copy.deepcopy(nums)
        cur[i], cur[idx] = cur[idx], cur[i]
        dfs(cur, ret, i + 1)

def getIntFromStr(nums):
    ret = []
    for num in nums:
        ret.append(int("".join(num)))

    return ret

def nextMax(nums, index):
    maxNum = '0'
    nexNum = nums[index + 1:]
    for i,num in enumerate(nums[index:]):
        if num < nums[index]:
            if num > maxNum:
                maxNum = num
                return i

    return -1

def getRes(nums):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            return int("".join(nums))
        
def solver2(n):
    asm = []
    nums = getNumber(n)
    if max(nums) == min(nums):
        return 0
    cur = copy.deepcopy(nums)
    cur.sort(reverse=True)
    if cur == nums:
        return getRes(nums)
    dfs(nums, asm, 0)
    asm = getIntFromStr(asm)
    ret = getMaxIntegerOfN(asm, n)
    if len(str(ret)) != len(str(n)):
        return 0
    return ret  

def test():
    n = 63524235312311231232112
    ret = solver2(n)
    print(ret)

if __name__ == '__main__':
    test()