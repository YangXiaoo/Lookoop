// 2019-4-25~26
// 队列的最大值
// leetcode-239
#include <stdio.h>
#include <deque>
#include <vector>
using namespace std;

vector<int> maxInWindow(const vector<int>& nums, unsigned int size) {
	vector<int> ret;	// 定义返回列表
	deque<int> deq;		// 定义每个窗口最大值
	for (int i = 0; i < nums.size(); ++i) {
		while (!deq.empty() && (nums[deq.back()] <= nums[i])) {
			deq.pop_back();
		}

		deq.push_back(i);
		// printf("%d, ", deq.front());
		if (deq.front() == (i - size))
			deq.pop_front();

		// printf("%d, ", deq.front());
		ret.push_back(nums[deq.front()]);
	}

	vector<int>::iterator it = ret.begin();
	for (int j = 1; j < size; ++j) {
		it = ret.erase(it);
	}

	return ret;
}


void test(const char* testName, const vector<int>& nums, unsigned int size, const vector<int>& expect) {
	printf("%s, result: ", testName);
	vector<int> ret = maxInWindow(nums, size);
	for (auto x : ret) {
		printf("%d ", x);
	}
	printf(", expect: ");
	for (auto s : expect) {
		printf("%d ", s);
	}
}

int main(int argc, char const *argv[])
{
	vector<int> nums1 = { 2,3,4,2,6,2,5,1 };
	vector<int> expect1 = { 4,4,6,6,6,5 };
	int windowSize = 3;
	test("test-1", nums1, windowSize, expect1);

	return 0;
}