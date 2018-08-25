void GetNext(char* p,int next[])
{
	int pLen = strlen(p);
	next[0] = -1;
	int k = -1;
	int j = 0;
	while (j < pLen - 1)
	{
		//p[k]表示前缀，p[j]表示后缀
		if (k == -1 || p[j] == p[k]) 
		{
			++k;
			++j;
			next[j] = k;
		}
		else 
		{
			k = next[k];
		}
	}
}
/* 在 S 中找到 P 第一次出现的位置 */
int KMP(string S, string P, int next[])
{
    GetNext(P, next);

    int i = 0;  // S 的下标
    int j = 0;  // P 的下标
    int s_len = S.size();
    int p_len = P.size();

    while (i < s_len && j < p_len)
    {
        if (j == -1 || S[i] == P[j])  // P 的第一个字符不匹配或 S[i] == P[j]
        {
            i++;
            j++;
        }
        else
            j = next[j];  // 当前字符匹配失败，进行跳转
    }

    if (j == p_len)  // 匹配成功
        return i - j;
    
    return -1;
}

int main()
{
    int next[100] = { 0 };

    cout << KMP("bbc abcdab abcdabcdabde", "abcdabd", next) << endl; // 15
    
    return 0;
}