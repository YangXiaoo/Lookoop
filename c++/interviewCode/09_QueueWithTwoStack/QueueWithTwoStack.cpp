// 2019-3-21
#include <stdio.h>
#include <vector>
#include <exception>
#include <stack>

using namespace std;
/**
 * 用两个栈实现列队
 * 列队声明如下
 */

template <typename T>
class CQueue {
public:
	CQueue();
	~CQueue();

	void appendTail(const T& node);
	T deleteHead();
private:
	stack<T> stack1;
	stack<T> stack2;
};


/**
 * 栈 - 后入先出
 * 列队 - 先入先出
 * stack1 添加， stack2删除
 */


template <typename T>
CQueue<T>::CQueue(void) {}

template <typename T>
CQueue<T>::~CQueue(void) {}

/* 添加到末尾 */
template <typename T>
void CQueue<T>::appendTail(const T& node) {
	stack1.push(node);
}

/* 删除 */
template <typename T>
T CQueue<T>::deleteHead() {
	if (stack2.empty()) {
		while (!stack1.empty()) {
			T top = stack1.top();
			stack2.push(top);
			stack1.pop();
		}
	}

	if (stack2.empty()) {
		// throw new exception("queue is empty!");
		printf("queue is empty\n");
		return -1;
	}


	T head;
	head = stack2.top();
	stack2.pop();

	return head;
}

void test(const char* call_name, int head, int expect) {
	printf("call test name: %s, result: ", call_name);
	if (head == expect)
		printf("passed.\n");
	else
		printf("failed.\n");
}


int main(int argc, char const *argv[])
{
	CQueue<int> queue;
	int head;

	queue.appendTail(1);
	queue.appendTail(2);
	queue.appendTail(3);
	head = queue.deleteHead();
	test("delete 1", head, 1);
	queue.appendTail(4);
	head = queue.deleteHead();
	test("delete 2", head, 2);
	head = queue.deleteHead();
	test("delete 3", head, 3);
	head = queue.deleteHead();
	test("delete 4", head, 4);
	head = queue.deleteHead();
	test("delete 5", head, 0);

	return 0;
}
// print:
// call test name: delete 1, result: passed.
// call test name: delete 2, result: passed.
// call test name: delete 3, result: passed.
// call test name: delete 4, result: passed.
// queue is empty
// call test name: delete 5, result: failed.