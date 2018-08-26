# 2018-8-24
# Knuth-Morris-Pratt算法
# 算法导论 P588
# 参考博客： https://blog.csdn.net/v_JULY_v/article/details/7041827?spm=a2c4e.11153940.blogcont366088.6.59964c70l6MLk9#t3

"""
假设字符串：S“BBC ABCDAB ABCDABCDABDE”，和模式串P“ABCDABD”
int ViolentMatch(char* s, char* p)
{
	int sLen = strlen(s);
	int pLen = strlen(p);
 
	int i = 0;
	int j = 0;
	while (i < sLen && j < pLen)
	{
		if (s[i] == p[j])
		{
			//①如果当前字符匹配成功（即S[i] == P[j]），则i++，j++    
			i++;
			j++;
		}
		else
		{
			//如果失配（即S[i]! = P[j]），令i = i - (j - 1)，j = 0    
			i = i - j + 1;
			j = 0;
		}
	}
	//匹配成功，返回模式串p在文本串s中的位置，否则返回-1
	if (j == pLen)
		return i - j;
	else
		return -1;
}

这种方法i需要回溯到最开始位置，然而P[0]!=P[1]所以i还需要前进，浪费时间

"""
def getNext(P):
	plen = len(P)
	next = [0] * plen
	next[0] = -1
	k = -1
	j = 0
	while j < plen - 1:
		if k == -1 or P[j] == P[k]:
			"""
			如果P[j] == P[k] 则next[j] = k + 1 = next[j] + 1
			"""
			k += 1
			j += 1
			next[j] = k
		else:
			"""
			否则查看next[k]位是否与P[j]相等
			"""
			k = next[k] # 尽可能多的从后往前匹配而不是从头往后匹配
	return next

def KMP(S, P):
	next = getNext(P)
	s_len = len(S)
	p_len = len(P)
	i = 0
	j = 0

	while i < s_len and j < p_len:
		if j == -1 or S[i] == P[j]:
			i += 1
			j += 1
		else:
			j = next[j]
	if j == p_len:
		return i - j
	return -1

S = "EERWEDABCDABD"
P = "DABCDABD"
print(KMP(S, P))