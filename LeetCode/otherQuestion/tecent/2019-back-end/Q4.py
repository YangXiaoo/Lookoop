def solver(nums):
	pass

def compute(nums):
	visit = [0 for _ in nums]
	visit[0] = 1
	for i in range(1, len(nums)):
		j = i 
		while j >= 0:
			if nums[i] < nums[j]:
				break
			visit[i] += 1
			j -= 1

	print(visit)

def test():
	nums = [5,3,8,3,2,5]
	ret = compute(nums)

if __name__ == '__main__':
	test()