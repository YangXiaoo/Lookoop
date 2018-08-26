/**
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
*/

// 2018-8-26
//  166. Fraction to Recurring Decimal
// https://leetcode.com/problems/fraction-to-recurring-decimal/description/


#include <stdio.h>

char* fractionToDecimal(int numerator, int denominator);

int main()
{
  int numerator = 2;
  int denominator = 1;
  char *res;
  res = fractionToDecimal(numerator, denominator);
  printf("%s\n", res); 
  return 0;
}

char* fractionToDecimal(int numerator, int denominator) {
    
}