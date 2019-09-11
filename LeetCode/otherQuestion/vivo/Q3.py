#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Welcome to vivo !
'''

def solution(boxes):
    #TODO Write your code here
    score = 0
    while len(boxes) != 0:
    	left, right = [], []
    	index, lens, num = getMaxSameNumLength(boxes)
    	score += lens * lens
    	left += boxes[:index]
    	right += boxes[index+lens:]
    	boxes = left + right

    return score


def getMaxSameNumLength(boxes):
	start = 1
	ret = []
	preMax, preIndex, preNum = 1, 0, boxes[0]
	while start < len(boxes):
		if boxes[start] == boxes[start-1]:
			preMax += 1
		else:
			ret.append([preMax, preIndex, preNum])
			preMax = 1
			preIndex = start 
			preNum = boxes[start]
		if start == len(boxes) - 1:
			ret.append([preMax, preIndex, preNum])
		start += 1
	ret = sorted(ret, key = lambda x :x[0])
	print(ret, boxes)
	return ret[-1]


def inputs():
    x = input()
    boxes = list(map(int,x.split()))
    print(solution(boxes))

def test():
	s = "1 4 2 2 3 3 2 4 1"
	boxes = list(map(int, s.split()))

	ret = solution(boxes)
	print(ret)

if __name__ == '__main__':
	test()