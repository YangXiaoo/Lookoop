# coding:utf-8

def solver(nums):
	tmp = 0
	maxSum = -999999
	for i in range(len(nums)):
		if tmp < 0:
			tmp = nums[i]
		else:
			tmp += nums[i]

		if tmp > maxSum:
			maxSum = tmp 


	return maxSum

def test():
	nums = [2,4,-7,5,2,-1,2,-4,3]
	ret = solver(nums)

	print(ret)

if __name__ == '__main__':
	test()
		
