// 2019-3-24
#include <stdio.h>
#include <string>

using namespace std;

/**
 * 打印从1到最大的n位数
 * 输入数字n, 按顺序打印从1到最大的n位十进制数。
 */

void print1ToMaxOfN(int n);
bool increate(string& seq);
void printHelper(string& seq);


void test(const char* call_name, int n) {
	printf("%s, result: ", call_name);

	print1ToMaxOfN(n);
	printf("\n");
}

int main(int argc, char const *argv[])
{
	test("test1", 1);
	test("test2", 2);
	return 0;
}

// print:
// test1, result: 1        2       3       4       5       6       7       8       9
// test2, result: 1        2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      20      21      22      23      24      25      26      27      28      29      30      31      32      33      34      35      36      37      38      39      40      41      42      43      44      45      46      47      48      49      50      51      52      53      54      55      56      57      58      59      60      61      62      63      64      65      66      67      68      69      70      71      72      73      74      75      76      77      78      79      80      81      82      83      84      85      86      87      88      89      90      91      92      93      94      95      96      97      98      99

void print1ToMaxOfN(int n) {
	if (n < 1) return;

	string seq(n, '0');

	while (increate(seq)) {
		printHelper(seq);
	}
}

bool increate(string& seq) {
	for (int i = seq.size() - 1; i >= 0; --i) {
		if ((seq[i] - '0') < 9) {
			seq[i] = seq[i] + 1;
			return true;
		}
		else {
			seq[i] = '0';
		}
	}

	return false;
}

void printHelper(string& seq) {
	bool flag = false;
	for (int i = 0; i < seq.size(); ++i) {
		if (seq[i] == '0' && !flag) {
			continue;
			flag = true;
		}
		else {
			printf("%c", seq[i]);
		}
	}
	printf("\t");
}