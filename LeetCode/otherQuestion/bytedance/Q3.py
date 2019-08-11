def solver(N, nums):
    if N < 1:
        return 0
    if N < len(nums):
        nums = nums[:N]
    # 找到第一个最小的数
    idx = findMin(nums, 0)
    # print(idx)
    salary = [0 for _ in range(N)]
    salary[idx] = 100
    # 左边
    giveSalary(salary, 0, idx)

    # print(salary)

    # 右边
    i = idx + 1
    while i < N:
        if nums[i] > nums[i - 1]:
            salary[i] = salary[i-1] + 100
            i += 1
        elif nums[i] == nums[i-1]:
            salary[i] = salary[i-1]
            i += 1
        else:
            nextMinIdx = findMin(nums, i)
            gap = nextMinIdx - i + 1
            giveSalary(salary, i, nextMinIdx)
            i += gap
        # print(i, salary)

    return sum(salary)


def findMin(nums, start):
    firstMin = nums[start]
    idx = start
    for i in range(start+1, len(nums)):
        if nums[i] >= firstMin:
            break
        else:
            firstMin = nums[i]
            idx = i 

    return idx

def giveSalary(salary, start, end):
    salary[end] = 100
    for i in range(end-1, start-1, -1):
        # print(i)
        salary[i] = salary[i + 1] + 100

def test():
    N = 5
    nums = [1, 9, 5, 6, 10]
    ret = solver(N, nums)
    print(ret)

if __name__ == '__main__':
    test()