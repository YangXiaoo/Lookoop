# 2018-7-30
# 桶排序

# 简单桶排序
def buck(nums):
	bucks = [];
	mins = nums[0];
	maxs = nums[0];

	for n in nums:
		mins = mins < n ? mins : n;
		maxs = maxs > n ? maxs : n;

	for i in maxs:
		bucks.append(32767);

	for i in range(len(nums)):
		bucks[nums[i]] = 1;

	res = [];

	for i in bucks:
		if i != 32767:
			res.append(i);

	return res
