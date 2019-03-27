// 2019-3-27
#include <stdio.h>
#include <string>
using namespace std;

bool helper(string& str, int s_start, string& pattern, int p_start);

bool match(string& str, string& pattern) {
	if (str.empty() || pattern.empty()) return false;

	return helper(str, 0, pattern, 0);
}

bool helper(string& str, int s_start, string& pattern, int p_start) {
	if (str.size() < s_start || pattern.size() < p_start) return false;
	if (str.size() == s_start && pattern.size() == p_start) return true;
	if (str.size() == s_start && pattern.size() != p_start) return false;

	if (pattern.size() > p_start+1 && pattern[p_start+1] == '*') {
		if (pattern[p_start] == str[s_start] || (pattern[p_start] == '.' && !str.empty())) {
			return helper(str, s_start+1, pattern, p_start+2) \
				   || helper(str, s_start+1, pattern, p_start) \
				   || helper(str, s_start, pattern, p_start+2);
		}
	}

	if (str[s_start] == pattern[p_start] || (str.size() > s_start && pattern[p_start] == '.')) {
		return helper(str, s_start+1, pattern, p_start+1);
	}

	return false;
}