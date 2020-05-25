# coding:utf-8
# 计算排水量变化

def delta(originoriginall, newShape):
	return (newShape - originoriginall) / originoriginall

def main():
	original = 13953969295
	newShape = 14195394452
	maxSizeShape = 15815557598
	minSizeShape = 13368960489

	originalVolume = original*2/1e9
	print("[INFO] 游艇原始排水量： {}".format(originalVolume))

	newShapeVolume = newShape*2/1e9
	print("[INFO] 优化后游艇排水量： {}".format(newShapeVolume))

	ret = delta(original, newShape)
	print("[INFO] 最优造型排水量变化： {}".format(ret))

	maxShapeVolume = maxSizeShape*2/1e9
	print("[INFO] 游艇最大排水量： {}".format(maxShapeVolume))
	ret2 = delta(original, maxSizeShape)
	print("[INFO] 最大变形排水量变化： {}".format(ret2))
	

	minShapeVolume = minSizeShape*2/1e9
	print("[INFO] 游艇最小排水量： {}".format(minShapeVolume))
	ret3 = delta(original, minSizeShape)
	print("[INFO] 最小变形排水量变化： {}".format(ret3))

if __name__ == '__main__':
	main()