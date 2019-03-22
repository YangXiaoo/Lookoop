// 2019-3-22
#include <stdio.h>
#include <vector>
#include <string>
#include <exception>
#include <stack>

using namespace std;

/* 矩阵中的路径 */
bool helper(vector<string>& matrix, vector<vector<bool>>& visited,
			int r, int c, string& str, int& p);

bool hasPath(vector<string>& matrix, string& str) {
	if (matrix.empty()) return false;
	if (str.empty()) return true;

	int row = matrix.size(), col = matrix[0].size();

	// printf("getting visited\n");
	vector<vector<bool>> visited;
	for (int i = 0; i < row; ++i) {
		vector<bool> tmp;
		for (int j = 0; j < row; ++j) {
			tmp.push_back(false);
		}
		visited.push_back(tmp);
	}
	printf("visited.size(): %d\n", visited.size());
	// printf("getting path\n");
	bool ret = false;
	int p = 0;
		for (int r = 0; r < row; ++r) {
			for (int c = 0; c < col; ++c) {
				if (helper(matrix, visited, r, c, str, p))
					return ret;
			}
		}

	return ret;
}

bool helper(vector<string>& matrix, vector<vector<bool>>& visited,
			int r, int c, string& str, int& p) {
	// printf("debug p: %d\n", p);
	if (p == str.size()) return true;

	bool ret = false;

	if (r >= 0 && r < matrix.size()
		&& c >= 0 && c < matrix[0].size()
		&& !visited[r][c] && matrix[r][c] == str[p])
	{
		visited[r][c] = true;
		++p;
		ret = helper(matrix, visited, r + 1, c, str, p)
			|| helper(matrix, visited, r, c - 1, str, p)
			|| helper(matrix, visited, r - 1, c, str, p)
			|| helper(matrix, visited, r, c + 1, str, p);

		if (!ret) {
			--p;
			visited[r][c] = false;
		}

	}
	return ret;
}


void test(const char* call_name, vector<string>& matrix, 
		  string& str, bool except) {
	printf("%s, result: ", call_name);

	bool ret = hasPath(matrix, str);
	if (ret == except)
		printf("passed.\n");
	else
		printf("failed.\n");
}

int main(int argc, char const *argv[])
{
	vector<string> matrix = { { "abtg" },
							  { "cfcs" },
							  { "jdeh"} };

	string str1 = { "bfce" };
	string str2 = { "abfb" };

	test("test1", matrix, str1, true);
	test("test2", matrix, str2, false);

	return 0;
}