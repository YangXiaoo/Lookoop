def decodeString(s):
	tmp, digits = [""], []
	digit = 0
	pre = False
	for i, c in enumerate(s):
		if c.isdigit():
			digit = digit * 10 + int(c)
			continue
		if c == '(':
			tmp.append("")
		elif c == ')':
			if pre:	# 有括号的地方才放到一起
				last = tmp.pop()
				tmp.append(last * digit)
				digit = 0
			pre = True
		else:
			if digit != 0:	# 只针对有括号的地方才放到一起
				if pre:	
					last = tmp.pop()
					tmp.append(last * digit)
					pre = False
				else:
					tmp[-1] = tmp[-1][:-1] + tmp[-1][-1] * digit
				digit = 0
			tmp[-1] += c


	return "".join(tmp)

def test_decodeString():
	s = """
	A11B
	(AA)2A
	((A2B)2)2G
	(YUANFUDAO)2JIAYOU
	A2BC4D2
	"""
	ans = """
	AAAAAAAAAAAB
	AAAAA
	AABAABAABAABG
	YUANFUDAOYUANFUDAOJIAYOU
	AABCCCCDD
	"""

	inp = [x for x in s.split("\n")]
	ans = [x for x in ans.split("\n")]
	for i, s in enumerate(inp):
		ret = decodeString(s)
		if ret == ans[i]:
			print("True")

if __name__ == '__main__':
	test_decodeString()