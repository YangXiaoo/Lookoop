def getAssemble(nums):
    ret = []
    lens = len(nums)
    for i in range(lens):
        tmp = [nums[i]]
        for j in range(i + 1,lens):
            if j != i:
                tmp = tmp + [nums[j]]
                for x in range(j+1, lens):
                    if x != i and x != j:
                        tmp.append(nums[x])
                        if len(tmp) == 3:
                            ret.append(tmp[:])
                        tmp.pop()

    return ret 

def computeVar(nums):
    s = 0
    mean = sum(nums) / 3
    s += (nums[0] - mean)**2
    s += (nums[1] - mean)**2
    s += (nums[2] - mean)**2
    return round(s / 3, 2)

def solver(nums):
    """给定N个整数, 找出其中3个数字, 满足这三个数的组合方差最小"""
    asm = getAssemble(nums)
    # print(asm)
    minVar = computeVar(asm[0])
    ret = asm[0]
    for num in asm:
        curVar = computeVar(num)
        if curVar < minVar:
            ret = num 
            minVar = curVar

    return minVar



def test():
    nums = [10, -1, 0, 1, 3, 0, 2, 3, 20]
    ret = solver(nums)
    print(ret)

if __name__ == '__main__':
    test()