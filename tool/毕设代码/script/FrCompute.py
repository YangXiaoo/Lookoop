# coding:utf-8

G = 9.8

def getV(Fr, L):
	"""根据Fr和水线长度获得速度"""
	return Fr * ((L*G)**0.5)

def main():
	Fr = [0.05, 0.1, 0.2, 0.3, 0.4]
	L = 14.23
	for f in Fr:
		v = getV(f, L)
		print("Fr: {}, v: {}".format(f, v))

if __name__ == '__main__':
	main()