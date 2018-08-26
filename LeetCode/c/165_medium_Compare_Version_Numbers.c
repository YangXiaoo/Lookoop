/*
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
*/

// 2018-8-26
// 165. Compare Version Numbers
// https://leetcode.com/problems/compare-version-numbers/description/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int compareVersion(char* version1, char* version2);

int main()
{
  char version1[] = "1";
  char version2[] = "01";
  char *v1 = version1;
  char *v2 = version2; 
  int res;
  res = compareVersion(v1, v2);
  printf("%d\n", res); 
  return 0;
}


int compareVersion(char* version1, char* version2) {
    int len1 = strlen(version1);
    // int len1 = sizeof(version1) / sizeof(version1[0]);
    int len2 = strlen(version2);

    int i = 0;
    int j = 0;

    int num1 = 0;
    int num2 = 0;
    while (i < len1 || j < len2)
    {
    	while (version1[i] != '.' && i < len1)
    	{
    		num1 = num1 * 10 + int(version1[i] - '0');// num1 = num1 * 10 + atoi(version1[i]);
    		i++;
    	}
    	while (version2[j] != '.' && j < len2)
    	{
    		num2 = num2 * 10 + int(version2[j] - '0');
    		j++;
    	}

    	if (num1 > num2)
    		return 1;
    	else if (num1 < num2)
    		return -1;

    	num1 = 0;
    	num2 = 0;
    	i++;
    	j++;
    }

    return 0;
}