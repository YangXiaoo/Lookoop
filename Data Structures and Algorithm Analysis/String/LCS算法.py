# 2018-8-22
# LCS最长回文串

def Lcs(X, Y):
	m = len(X)
	n = len(Y)

	c = [([None] * n) for i in range(m)]

	for i in range(m):
		c[i][0] = 0

	for j in range(n):
		c[0][j] = 0

	for i in range(m):
		for j in range(n):
			if X[i] == Y[j]:
				c[i][j] = c[i-1][j-1] + 1
			else:
				c[i][j] = max(c[i-1][j],c[i][j-1])
	return c[-1][-1]