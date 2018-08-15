# RSA
# 2018-8-15
# https://blog.csdn.net/bian_h_f612701198412/article/details/79358771
# https://blog.csdn.net/rentenglong2012/article/details/68944518

def gcd(a, b):
	"""
	a = kb + r --> r = a % b
	we have:
	c = gcd(a, b)
	r = a - kb
	c|r --> c = gcd(b, r)
	gcd(a, b) = gcd(b, a % b )
	"""
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def extendGcd(a, b):
	"""
	ax + by = gcd(a, b) = d (Introduction to Algorithms P544)
	we have two case:
	a. if b == 0
		ax + 0 = gcd(a, 0) = a
		--> x = 1
			y = 0,1,... --> y = 0
	b. if a*b != 0
		then, ax + by = ax' + (a%b)y'.And a % b = a - (a/b)*b
		so, ax + by= ay' + b[x' - (a/b)y']
		-->	x = x'
			y = x' - (a/b)y'
	"""
	if b == 0:
		return a,1,0
	else:
		_b, _x, _y = extendGcd(b, a % b)
		d, x, y = _d, _y, _x - (a / b) * _y
		return d, x, y

