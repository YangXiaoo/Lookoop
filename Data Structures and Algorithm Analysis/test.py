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
print(N)