// 2019-3-28
#include <stdio.h>
using namespace std;

bool scanInteger(const char** str);
bool scanUnsignedInteger(const char** str);

bool isNumeric(const char* str) {
	if (str == nullptr) return false;

	bool numeric = scanInteger(&str);

	if (*str == '.') {
		++str;
		numeric = scanUnsignedInteger(&str) || numeric;		// 小数点后面可以没有数字如 23.
															// 小数点前面可以没有数字 .23
															// 前后都有数字
	}

	if (*str == 'e' || *str == 'E') {
		++str;
		numeric = numeric && scanInteger(&str);		// 当e前面没有数字时，后面不能表示数字
													// 当e后面没有数字时也不能表示数字
	}

	return numeric && *str == '\0';
}


bool scanInteger(const char** str) {
	if (**str == '+' || **str == '-')
		++(*str);

	return scanUnsignedInteger(str);
}


bool scanUnsignedInteger(const char** str) {
	const char* before = *str;
	while (**str != '\0' && **str >= '0' && **str < '9')
		++(*str);

	return *str > before;
}