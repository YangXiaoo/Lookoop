// 2019-3-27
#include <stdio.h>
#include "util.hpp"
using namespace std;

/* 删除重复值的节点(全都删除) */

void deleteDuplicate(ListNode** pHead) {
	if (pHead == nullptr) return;

	ListNode* pre = nullptr;
	ListNode* cur = *pHead;

	while (cur) {
		
		bool dup = false;
		if (cur->next) {
			if (cur->next->val == cur->val) {
				dup = true;
			}
		}

		if (!dup) {
			pre = cur;
			cur = cur->next;
		} else {
			ListNode* next = cur->next;
			int dupVal = cur->val;

			while (next && next->val != dupVal) {
				ListNode* tmp = next->next;
				delete next;
				next = tmp;
			}

			// 如果是头节点
			if (pre == nullptr) {
				*pHead = next;
			} else {
				pre->next = next;
			}
			cur = next;
			// pre = cur;	// 因为有重复的都删除了，所以pre节点不变
		}
	}
}