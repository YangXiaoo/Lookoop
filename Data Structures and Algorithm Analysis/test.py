a,b,c,d,e,f,g,h = range(8)
N = [
	{b,c,d,e,f},
	{c,e},
	{d},
	{e},
	{f},
	{c,g,h},
	{f,h},
	{f,g}
]
N.pop(0)
m = [([0] * 3) for i in range(4)]
print(m )