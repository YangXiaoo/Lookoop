# 2018-8-22
# Rabin-Karp算法
# 算法导论 P580
# https://blog.csdn.net/seacowtech/article/details/79256299
# https://blog.csdn.net/chenhanzhun/article/details/39895077

def RabinKarpMatcher(T, P, d, q):

	n = len(T) # 被搜索字符串
	m = len(P) # 匹配字符串
	h = 1 # d**(m-1) % q
	p = 0 # 匹配字符的哈希值
	t = 0 # 被搜索字符串的哈希值


	# 可以用蒙哥马利法求解模幂乘运算
	for i in range(m - 1):
		h = (h * d) % q

	# 第一个匹配窗口的值
	for i in range(m):
		p = (d * p + ord(P[i])) % q
		t = (d * t + ord(T[i])) % q

	print(m,n,h,p,d,q)

	for s in range(n-m+1):
		# print(T[s:s+m], p, t)
		if p == t:
			i = 0
			for i in range(m):
				if T[s + i] != P[i]:
					break
				if i == m-1:
					print("Index: ", s)
					return 
		if s < (n - m):
			t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q

			if t < 0:
				t = t + q

T = "Rarbin-KarpstringsearchalgorithmRabinKarp"
P = "Rab"
d = 256 # 字符串转义范围 
q = 101 # 素数
RabinKarpMatcher(T, P,d,q);