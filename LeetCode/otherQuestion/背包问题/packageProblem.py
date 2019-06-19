# coding=utf-8

"""
01背包
有N件物品和一个容量为V的背包。第i件物品的价格（即体积，下同）是w[i]，价值是p[i]. 
求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
"""

# https://blog.csdn.net/weixin_39059738/article/details/79924049
def pakage01(v, w, p):
	"""
	f[i][j] 第i个物品放入背包中背包大小为j时最佳值
	分两种情况
		1. 不放入背包 f[i-1][j]
		2. 放入背包 max(f[i-1][j], f[i-1][j-w[i]] + p[i])
	"""
	f = [[0 for _ in range(v+1)] for _ in w]
	for i in range(len(w)):
		for j in range(v+1)[1:]:
			if j < w[i]:
				f[i][j] = f[i-1][j]
			else:
				f[i][j] = max(f[i-1][j], f[i-1][j-w[i]] + p[i])
	print("f: {}".format(f))
	return f[-1][-1]

def testAns():
	w = [1 , 3 , 2 , 6 , 2]
	p = [2 , 5 , 3 , 10 , 4]
	v = 12
	ret = pakage01(v, w, p)
	print(ret)

if __name__ == '__main__':
	testAns()