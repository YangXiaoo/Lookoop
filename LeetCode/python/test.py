# test
t = [None] * 9
t[2] = 3
t = [[] for _ in range(len(t))]
t[1].append(6)
print(t)