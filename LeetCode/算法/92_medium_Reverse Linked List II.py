"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# 2018-6-28
# Reverse Linked List II
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = l1 = ListNode(0)
        flag = 0
        k = 1
        while head:
            # print(head.val,k)
            if k < m or k > n:
                cu = ListNode(head.val)
                l1.next = cu
                l1 = cu
            else:
                if flag == 0:
                    d = e = ListNode(head.val)
                    flag = 1
                else:
                    cur = ListNode(head.val)
                    cur.next = e
                    e = cur
            if k == n: 
                l1.next = e
                l1 = d
            k += 1
            head = head.next

        return dummy.next



l1 = [1,2,3,4,5]
m = 2
n = 4
head = lists = ListNode(0)
for i in l1:
    cur = ListNode(i)
    lists.next = cur
    lists = cur
head = head.next    


test = Solution()
res = test.reverseBetween(head,m,n)
# show lists
while res:
    print(res,res.val,res.next)
    res = res.next