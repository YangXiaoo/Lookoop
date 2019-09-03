# coding:utf-8
# 2019/9/3

"""
题目名称：最大数
时间限制：3000ms
题目描述：



输入描述：第一行数据是一个整数，表示数组长度。
第二行数据是n个整数，表示数组元素。

输出描述：暂无
示例1
输入
5
1 201 20 9 8


输出
98202011
"""
import sys
def solver(nums):
	nums.sort()
	nums = nums[::-1]
	for i in range(len(nums)-1):
		f, s = nums[i] + nums[i+1], nums[i+1]+nums[i]
		if int(f) < int(s):
			nums[i], nums[i+1] = nums[i+1], nums[i]

	return "".join(nums)


def test():
	nums = "1 201 20 9 8"
	nums = nums.split()
	ret = solver(nums)
	print(ret)

def inputs():
	n = int(sys.stdin.readline().strip())
	nums = sys.stdin.readine().strip().split()
	ret = solver(nums)
	print(ret)

if __name__ == '__main__':
	test()