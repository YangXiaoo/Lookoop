// 2019-3-24
#include <stdio.h>

using namespace std;

/* 二进制中1的个数 */

int countOne_1(int n) {
	int count = 0;
	int i = 1;
	while (i) {
		if (n & i)	// i 每次往左挪动一位，并检查n中该位上是否有1
			++count;
		i <<= 1;
	}
}

int countOne_2(int n) {
	int count = 0;
	while (n) {
		++count;
		n = (n - 1) & n;	// 例：1100减1然后与1100求&，会减少最右端第一个为1的位数 
	}
}