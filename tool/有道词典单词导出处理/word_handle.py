# 2018-9-13
import time
file = open("test.txt", encoding="utf-8")
data = file.readlines()
file.close()
with open("word.txt", "w",encoding="utf-8") as f:
	pre = ""
	for i in data:
		s = i.split(",")
		if len(s) == 2:
			s[0] += '.'
			w = s[1].split('[')
			if len(w) == 2:
				w[0] += '\t'
				w[1] = '[' + w[1]
			s[1] = "".join(w)
			f.write("".join(s))
			continue
	f.close()
with open("translate.txt", "w", encoding="utf-8") as f:
	pre = "********** 导出时间 %s **********" % str(time.asctime( time.localtime(time.time()) ))
	first = False
	for i in data:
		s = i.split(",")
		if len(s) == 2:
			pre += '\n'
			f.write(pre)
			pre = ""
			# print(s)
			pre += s[0] + '.' + " "
			continue
		# print(s)
		pre += s[0][:-1]

print()