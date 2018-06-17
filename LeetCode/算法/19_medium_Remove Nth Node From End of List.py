'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lens = 0
        h_1 = head
        while head:
            head = head.next
            lens += 1
        head = h_1
        h = l_1 = ListNode(0)
        i = 0
        while head:
            if i == lens - n:
                head = head.next
                i += 1
            else:
                l2 = ListNode(head.val)
                l_1.next = l2
                l_1 = l2
                head = head.next
                i += 1
        if not h.next:
            return []
        else:
            return h.next

# test
lis = [1,2,3,4,5]
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
res = test.removeNthFromEnd(head,2)
while res:
    print(res,res.val,res.next)
    res = res.next
