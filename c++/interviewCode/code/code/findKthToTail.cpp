// findKthToTail.cpp
// 2019-3-19
/**
 * 寻找链表中的倒数第k个节点
 */

#include <stdio.h>
#include <vector>
#include <iostream>

#include "util.hpp"		// 定义链表
using namespace std;


ListNode* findKthToTail(ListNode* head, unsigned int k);

// int main(int argc, char const *argv[])
// {
// 	vector<int> list = { 1, 2, 3, 4, 5 };
// 	ListNode* head;
// 	head = get_link_list(list);
	
// 	// 测试
// 	for (unsigned int k = 0; k < 8; ++k) {
// 		ListNode* kth_node = findKthToTail(head, k);
// 		// cout << "倒数第 " << k << " 个节点值为: " << kth_node->val;
// 		if (kth_node)
// 			printf("倒数第 %d 个节点的值为 %d\n", k, kth_node->val);
// 		else
// 			if (k < 1)
// 				printf("k %d is smaller than 1\n", k);
// 			else
// 				printf("k %d is larger than the length of link-list\n", k);
// 	}
// 		// print
// 		//k 0 is smaller than 1
// 		//倒数第 1 个节点的值为 5
// 		//倒数第 2 个节点的值为 4
// 		//倒数第 3 个节点的值为 3
// 		//倒数第 4 个节点的值为 2
// 		//倒数第 5 个节点的值为 1
// 		//k 6 is larger than the length of link - list
// 		//k 7 is larger than the length of link - list

// 	return 0;
// }


ListNode* findKthToTail(ListNode* head, unsigned int k) {
	// 判断链表头结点是否为空
	if (head == NULL)
		return NULL;

	// k 小于1的情况
	if (k < 1) return NULL;

	// 定义快慢指针
	ListNode *fast = head;
	ListNode *slow = head;

	// 快指针先走 k-1 步
	for (unsigned int i = 0; i < k - 1; ++i) {
		// 判断k是否超出链表长度
		if (fast != NULL)
			fast = fast->next;
		else return NULL;
	}

	// k超出链表长度
	if (fast == NULL) return NULL;
	
	while (fast->next != NULL) {
		fast = fast->next;
		slow = slow->next;
	}

	return slow;
}
