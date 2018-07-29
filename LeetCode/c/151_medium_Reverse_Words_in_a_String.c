/**
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
*/

// 2018-7-29
// 151. Reverse Words in a String
#include <stdio.h>
#include <string.h>
#include <ctype.h>
void reverse(char * s, int first, int last);
void reverseWords(char *s);

int main()
{
	char str[] = "  the sky is  blue  ";
	char * s = str;
	printf("%s\n", s);
	reverseWords(s);
	printf("%s\n", s);
	return 0;

}
 
void reverseWords(char *s) 
{
	int last = 0, now = 0;
	// 先翻转每个单词，然后再翻转整个字符串
	while (s[now]) 
	{
		while (s[now] == ' ')
			now++;
		last = now;
		while (s[now] != ' ' && s[now] != '\0')
			now++;
		reverse(s, last, now - 1);
	}
	// 翻转整个字符串
	reverse(s, 0, now - 1);
	// 删除多余空格
	last = 0;
	for (int i = 0; i < now; i++)
	{
		// last != 0
		// last && s[last - 1] != s[i]) 巧妙的多一个空格
		if (!isspace(s[i]) || (last && s[last - 1] != s[i])) 
		{
			s[last++] = s[i];
		}
	}

	// 字符串末尾空格转换为结束符'\0'
	s[last] = 0;
	if (last && s[last - 1] == ' ')
		s[last - 1] = 0;
}

// 翻转单词
void reverse(char * s, int head, int tail)
{
	while (head < tail) {
		char tmp = s[head];
		s[head++] = s[tail];
		s[tail--] = tmp;
	}
}
