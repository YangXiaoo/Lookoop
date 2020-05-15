# coding:utf-8
# start: 2020-5-15
# 剑指offer内容

# 03 数组中重复的数字
def findDuplicate(nums):
	"""[2,3,1,0,2,5,3]"""
	for i in range(len(nums)):
		while i != nums[i]:
			if nums[nums[i]] == nums[i]: return nums[i]
			nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

	return -1

def testFindDuplicate():
	nums = [2,3,1,0,2,5,3]
	ret = findDuplicate(nums)
	print(ret)

testFindDuplicate()

