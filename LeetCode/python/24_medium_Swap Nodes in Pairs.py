'''
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''

# 2018-6-18
# Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = lis = ListNode(0)
        old = 0
        while head:
        	old = head.val
        	cur = head.next
        	if cur:
        		cur_val = ListNode(cur.val)
        		lis.next = cur_val
        		lis = cur_val
        		cur1 = ListNode(old)
        		lis.next = cur1
        		lis = cur1
        		head = cur.next
        	else:
        		cur2 = ListNode(old)
        		lis.next = cur2
        		lis = cur2
        		head = cur
        return dummy.next


lis = [1,2,3,4,5]
head = lists = ListNode(0)
for i in lis:
    cur = ListNode(i)
    lists.next = cur
    lists = cur
head = head.next

test = Solution()
res = test.swapPairs(head)
while res:
	print(res.val)
	res = res.next