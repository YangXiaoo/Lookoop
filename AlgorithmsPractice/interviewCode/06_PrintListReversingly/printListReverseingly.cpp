// 2019-3-20
#include <stdio.h>
#include <vector>
#include <iostream>
#include <stack>

#include "util.hpp"		// 定义链表
using namespace std;

/** 
 * 从尾到头打印链表
 * 输入一个链表的头结点，从尾到头打印链表的每个几点值
 */

 /* 使用栈 */
void printListReverseingly_iterate(ListNode* head) {
	stack<ListNode*> stacks;
	ListNode* p_new = head;
	while (p_new) {
		stacks.push(p_new);
		p_new = p_new->next;
	}

	while (!stacks.empty()) {
		p_new = stacks.top();
		printf("%d\t", p_new->val);
		stacks.pop();
	}
}

/* 递归 */
void printListReverseingly_recurse(ListNode* head) {
	if (head) {
		if (head->next)
			printListReverseingly_recurse(head->next);
		printf("%d\t", head->val);
	}
}



int main(int argc, char const *argv[])
{
	vector<int> list = { 1, 2, 3, 4, 5, 6 };
	ListNode* head = get_link_list(list);

	printf("using iteratively\n");
	printListReverseingly_iterate(head);

	printf("\nusing recursively\n");
	printListReverseingly_recurse(head);

	return 0;
}

// print:
// using iteratively
// 6       5       4       3       2       1
// using recursively
// 6       5       4       3       2       1