/*
Given two integers representing the numerator(分子) and denominator(分母) of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"

8/2 = 4
1/ 8 = 0.125
8 / 8 = 1
8 / 3 = 2.(6)
1 / 3 = 0.(3)
11 / 6 = 1.8(3)
1 / 7  = 0.(142857)
50 / 7  = 7.(142857)
*/

// 2018-8-26
//  166. Fraction to Recurring Decimal
// https://leetcode.com/problems/fraction-to-recurring-decimal/description/


#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char* fractionToDecimal(int numerator, int denominator);

int main()
{
  int numerator = 50;
  int denominator = 7;
  char *res;
  res = fractionToDecimal(numerator, denominator);
  printf("%s\n", res); 
  return 0;
}

// 未解决
char* fractionToDecimal(int numerator, int denominator) {
	int map[100]; // 使用hash列表最好
	char tmp[100];
	int intPart = 0;
	int decimalPart = 0;
	int dummyInt = 0;
	int p = 0; // 标记结束位置

	int sign = (numerator < 0) ^ (denominator < 0);
	numerator = numerator < 0 ? -(numerator) : numerator;
	denominator = denominator < 0 ? -(denominator) : denominator;

	if (sign && numerator)
		tmp[p++] = '-';

	intPart = numerator / denominator; // 获得整数部分
	decimalPart = numerator % denominator;
	tmp[p++] = intPart;
	tmp[p++] = '.';
	int tens = 10;
	int repeatIndex = 0; // 标记重复的开始位置
	bool find = false;
	int d = 0;
	while (decimalPart != 0)
	{
		decimalPart *= tens;
		dummyInt = decimalPart / denominator;
		for (int i; i < d; i++)
		{
			if (map[i] == dummyInt)
			{
				repeatIndex = i;
				find = true;
				break;
			}

		}

		// 如果找到
		if (find)
		{
			break;
		}
		else
		{
			map[d++] = dummyInt;
		}
		decimalPart = decimalPart % denominator;
	}

	int totalSize = p + d;
	if (find)
		totalSize += 2;

    // char *res = (char *)malloc(sizeof(char) * totalSize); 
    if (find)
    {
    	for (int j = 0; j < repeatIndex; j++)
    	{
    		tmp[p++] = map[j];
    	}
    	tmp[p++] = '(';
    	for (int j = 0; j < d; j++)
    		tmp[p++] = map[j];
    	tmp[p++] = ')';
    	tmp[p++] = '\0';
    	return tmp;
    }
    else
    {
    	for (int j = 0; j < d; j++)
    		tmp[p++] = map[j];
    	tmp[p++] = '\0';
    	return tmp;
    }
}