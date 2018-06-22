"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

Last executed input:
[1,2,3]
2000000000
"""

# 2018-6-22
# Rotated List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        init = []
        while head:
            init.append(head.val)
            head = head.next
        # print("initialize array:",init)
        if len(init) == 0:
            return 
        i = 0
        k = k%(2*len(init)) # in case of LTE
        while  i < k:
            tmp = []
            head = init[-1]
            init = init[:-1]
            tmp.append(head)
            for j in init:
                tmp.append(j)
            init = tmp
            i += 1
        if k == 0:
            tmp = init
        dummy = li = ListNode(0)
        for n in tmp:
            cur = ListNode(n)
            li.next = cur
            li = cur
        return dummy.next




lis = [1,2,3]
head = lists = ListNode(0)
for i in lis:
    cur = ListNode(i)
    lists.next = cur
    lists = cur
head = head.next
'''
while head:
    print(head,head.val,head.next)
    head = head.next
'''
test = Solution()
res = test.rotateRight(head,200000)
while res:
    print(res,res.val,res.next)
    res = res.next