"""

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# 2018-6-27
# Remove Duplicates from Sorted List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = li = ListNode(0)
        if not head:
            return []
        old = head.val
        head = head.next
        cu = ListNode(old)
        li.next = cu
        li = cu
        while head:
            if head.val == old:
                head = head.next
            else:
                cur = ListNode(head.val)
                li.next = cur
                li = cur
                old = head.val
                head = head.next
        return dummy.next


l1 = []
head = lists = ListNode(0)
for i in l1:
    cur = ListNode(i)
    lists.next = cur
    lists = cur
head = head.next    


test = Solution()
res = test.deleteDuplicates(head)
# show lists
while res:
    print(res,res.val,res.next)
    res = res.next