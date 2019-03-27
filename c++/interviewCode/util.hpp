#include <vector>
#include <iostream>

// 定义链表结构
struct ListNode {
	int val;
	ListNode* pre;
	ListNode* next;
	ListNode(int _val = 0, ListNode* _pre = NULL, ListNode* _next = NULL) : val(_val), pre(_pre), next(_next) {}
};

/**
 * 由列表生成指针
 * @param list 列表
 * @return ListNode* 链表头结点
 */
ListNode* get_link_list(const std::vector<int>& list);