# 2018-8-8
# update 2018-9-4
# Code chinese character
# from codeWord import CodeWord
class CodeChar(object):
	"""
	Have code problem!
	test = CodeChar()
	res = test.code(string)
	res2 = test.decode(res)
	"""
	def __init__(self):
		self.exp = ['，','。','？','！','：','《','》','【','】','（','）','、','@','#','$','%','^','&','*','.',',','.','<','>','-','+','=', ' ','\n', '“','”', '!', '[', ']', '(', ')']
		self.radix = 19
		self.a_int = 97
		self.A_int = 65
		self.func = CodeWord(33)

	def code(self, s):
		res = []
		flag = 0
		tmp = []
		for i in s:
			if i in self.exp:
				if flag == 1:
					tmp.append('`')
					t = self.func.code("".join(tmp[1:-1]))
					t = '`' + t + '`'
					res.append(t)
					tmp = []
					flag = 0
				res.append(i)
			else:
				i_to_int = ord(i)
				if i_to_int > 19000 and i_to_int < 40000:
					if flag == 1:
						tmp.append('`')
						t = self.func.code("".join(tmp[1:-1]))
						t = '`' + t + '`'
						res.append(t)
						tmp = []
						flag = 0 
					nums = []
					while i_to_int > 0:
						while i_to_int:
							num = i_to_int % 10
							nums.append(num)
							i_to_int = i_to_int // 10
						nums = nums[::-1]
						r = []
						fir = nums[0] * 10 + nums[1] - self.radix + self.A_int
						r.append(chr(fir))
						sec = nums[2] + self.a_int
						r.append((chr(sec)))
						thr = nums[3] + self.a_int + 8
						r.append(chr(thr))
						fur = nums[4] + self.a_int + 16
						r.append(chr(fur))
						res.append("".join(r))
						r = []
				else:
					if flag == 0:
						tmp.append('`')
						tmp.append(i)
						flag = 1
					else:
						tmp.append(i)
		return " ".join(res)

	def decode(self, s):
		record = []
		flag = 1
		mark = 0
		end = 0
		tmp = []
		re = ""
		for i in s:
			if i not in self.exp and i != " " and i != '`' and mark == 0:
				record.append(i)
			elif i == '`':
				if mark == 0:
					mark = 1
				if end:
					t = self.func.deCode(" ".join(tmp))
					re += t
					mark = 0
					end = 0
					tmp = []
			else:	
				if mark == 1:
					tmp.append(i)
					end = 1
				else:
					re += i
					flag = 0
			if flag == 0 and len(record) == 4:
				r = 0
				r += (ord(record[0]) - self.A_int + self.radix) * 1000
				r += (ord(record[1]) - self.a_int) * 100
				r += (ord(record[2]) - self.a_int - 8) * 10
				r += ord(record[3]) - self.a_int - 16
				re += chr(r)
				record = []
				flag = 1

		res = ""
		pre = 0
		for i in re:
			if i == ' ' and pre == 1:
				res += i
			elif i != ' ':
				res += i
				pre = 0

			if i == ' ':
				pre = 1
		return res
		
class CodeWord(object):
	def __init__(self,x):
		self.x = x
	def code(self, s):
		d = {}
		for i in (65,97):
			for j in range(26):
				d[chr(i+j)] = chr( (j+self.x) % 26 + i)
		res = "".join([d.get(c,c) for c in s])
		return res

	def deCode(self, s):
		d = {}
		for i in (65, 97):
			for j in range(26):
				d[chr(i+j)] = chr((j+26-self.x) % 26 + i)
		res = "".join([d.get(c,c) for c in s])
		return res

s = """
![](dijkstra.jpg)
>## 个人博客

- [链接](http://www.lxxx.site)

>## tool 

- 图片，文件批量操作
- 数据处理
- 字符编码

>## LeetCode

- LeetCode算法题解析 Python, Java, C

>## C Python Linux java MySQL PHP MatLab PyQt5 神经网络
- 笔记


>## Data Structures and Algorithm Analysis

- 大部分用python实现


"""
test = CodeChar()
r1 = test.code(s)
r2 = test.decode(r1)
print()
print(r1)
print(r2)

"""
! [ ] ( `kpqrzayh` . `qwn` ) 
 > # #   Bajq Bbnu Cdly Eeny 
 
 -   [ Tbms Gfiz ] ( `oaaw://ddd` . `seee` . `zpal` ) 
 
 > # #   `avvs`   
 
 -   Dcpq Kcnv ， Gjrr Bcju Gciz Sdkx Giiv Bdjw 
 -   Gjoy Genu Dhqy Khis 
 -   Edqt Mfkw Nflu Lhkr 
 
 > # #   `SllaJvkl` 
 
 -   `SllaJvkl` Mglz Iior Uaou Qcrz Hfjs   `Wfaovu` ,   `Qhch` ,   `J` 
 
 > # #   `J`   `Wfaovu`   `Spube`   `qhch`   `TfZXS`   `WOW`   `ThaShi`   `WfXa5`   Mapq Neot Nfrt Nepw 
 -   Mfiy Qhoq 
 
 
 > # #   `Khah`   `Zaybjabylz`   `huk`   `Hsnvypaot`   `Huhsfzpz` 
 
 -   Dikt Sarw Bjry Kjrs `wfaovu` Eenu Kgjw 
 
 


![](dijkstra.jpg)
>##  个人博客

-  [链接](http://www.lxxx.site)

>##  tool  

-  图片，文件批量操作
-  数据处理
-  字符编码

>##  LeetCode

-  LeetCode算法题解析  Python,  Java,  C

>##  C  Python  Linux  java  MySQL  PHP  MatLab  PyQt5  神经网络
-  笔记


>##  Data  Structures  and  Algorithm  Analysis

-  大部分用python实现

"""