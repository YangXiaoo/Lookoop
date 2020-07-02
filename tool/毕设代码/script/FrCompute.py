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

def getFr(v, L):
		return v / ((L*G)**0.5)

if __name__ == '__main__':
	L = 14.23
	v = 5
	fr = getFr(v, L)
	print(fr)

# Fr: 0.05, v: 0.5904532157588779
# Fr: 0.1, v: 1.1809064315177558
# Fr: 0.2, v: 2.3618128630355115
# Fr: 0.3, v: 3.5427192945532675
# Fr: 0.4, v: 4.723625726071023
# [Finished in 1.2s]