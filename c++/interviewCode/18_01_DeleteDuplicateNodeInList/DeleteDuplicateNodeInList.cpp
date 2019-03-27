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
		ListNode* next = cur->next;
		if (next && next->val == cur->val) {
			dup = true;
		}

		if (!dup) {
			pre = cur;
			cur = cur->next;
		} else {
			ListNode* toDelete = cur;
			int dupVal = cur->val;

			while (toDelete && toDelete->val == dupVal) {
				next = toDelete->next;
				delete toDelete;
				toDelete = nullptr;
				toDelete = next;
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

void test(const char* call_name, vector<int> list) {
	printf("%s, after delete duplicate: ", call_name);
	ListNode* head;
	head = get_link_list(list);

	deleteDuplicate(&head);

	if (!head) printf("null");
	while (head) {
		printf("%d\t", head->val);
		head = head->next;
	}

	printf("\n");
}


int main(int argc, char const *argv[])
{

	test("test1", {});
	test("test2", {1, 2, 3, 4});
	test("test3", {1, 2, 4, 4, 4, 3});
	test("test4", {2, 2, 4, 4, 4, 3});
	test("test4", {2, 2, 4, 4, 4});


	return 0;
}

// print 
// test1, after delete duplicate: null
// test2, after delete duplicate: 1        2       3       4
// test3, after delete duplicate: 1        2       3
// test4, after delete duplicate: 3
// test4, after delete duplicate: null