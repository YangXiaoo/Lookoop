// 2019-3-27
#include <stdio.h>

#include "util.hpp"
using namespace std;

void deleteNode(ListNode** pHead, ListNode* toDeleteNode) {
	if (*pHead == nullptr || toDeleteNode == nullptr) return;

	// 如果待删除节点是尾节点
	if (toDeleteNode->next == nullptr) {
		ListNode* cur = *pHead;
		while (cur->next != toDeleteNode) {
			cur = cur->next;
		}

		cur->next = nullptr;
		delete toDeleteNode;
		toDeleteNode = nullptr;
	}
	// 如果是头节点
	else if (*pHead == toDeleteNode) {
		*pHead = toDeleteNode->next;	// 	*pHead = nullptr;
		delete toDeleteNode;
		toDeleteNode = nullptr;
	}
	// 如果在链表中
	else {
		ListNode* next = toDeleteNode->next;
		toDeleteNode->val = next->val;
		toDeleteNode->next = next->next;
		delete next
		next = nullptr;
	}
}