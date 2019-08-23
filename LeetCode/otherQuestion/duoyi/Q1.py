# coding:utf-8
# 数组循环右移 将一个长度为n的数组A的元素循环右移k位, 
# 比如 数组 1, 2, 3, 4, 5 循环右移3位之后变成 3, 4, 5, 1, 2

def solver(nums, k):
	lenNums = len(nums)
	if k > lenNums:
		k = k % lenNums
	left = lenNums - k
	numsL = nums[:left][::-1]
	# print(numsL)
	numsR = nums[left:][::-1]
	numsL.extend(numsR)


	return numsL[::-1]

def test():
	nums = [1,2,3,4,5]
	for k in range(1, 10):
		ret = solver(nums, k)
		print("k:{}, ret:{}".format(k, ret))

if __name__ == '__main__':
	test()

# k:1, ret:[5, 1, 2, 3, 4]
# k:2, ret:[4, 5, 1, 2, 3]
# k:3, ret:[3, 4, 5, 1, 2]
# k:4, ret:[2, 3, 4, 5, 1]
# k:5, ret:[1, 2, 3, 4, 5]
# k:6, ret:[5, 1, 2, 3, 4]
# k:7, ret:[4, 5, 1, 2, 3]
# k:8, ret:[3, 4, 5, 1, 2]
# k:9, ret:[2, 3, 4, 5, 1]