# 2018-8-16
# greedy algorithm
# example

def change(money, values, count):
	lens = len(values)
	res = [0] * lens
	c = 0
	for i in range(lens):
		if money <= 0:
			break
		c = min(money // values[i], count[i])
		res[i] = c
		money -= c * values[i]
	return res



count = [ 3, 1, 2, 1, 1, 3, 5 ]
values = [1,2,5,10,20,50,100]
values = values[::-1]
count = count[::-1]
money = 442
r = change(money, values, count)
c = 0
for i in r:
	if i != 0:
		print("需要",i, "张",values[c],"块")
	c += 1