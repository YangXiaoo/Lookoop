# coding=utf-8
# 2019-1-28
# quick_sort

def quick_sort(array):
	less, greater = [], []
	if len(array) <=1 :
		return array

	# choose a pivot 
	pivot = array.pop()
	for x in array:
		if x <= pivot: 
			less.append(x)
		else: 
			greater.append(x)

	return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
	array = [5,2,8,4,3,7,6,9,1]
	ret = quick_sort(array)
	print(ret)
