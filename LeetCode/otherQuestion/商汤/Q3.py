def solver(nums):
    minNum = nums[0]
    maxProfit = 0
    for n in nums:
        maxProfit = max(maxProfit, n - minNum)
        if n < minNum:
            minNum = n 

    return maxProfit

def test():
    nums = [7,1,5,3,6,4]
    ret = solver(nums)
    print(ret)

if __name__ == '__main__':
    test()