"""

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# 2018-6-27
# Partition List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = l1 = ListNode(0)
        d2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                cur = ListNode(head.val)
                l1.next = cur
                l1 = cur
            else:
                cur2 = ListNode(head.val)
                l2.next = cur2
                l2 = cur2
            head = head.next
        l1.next = d2.next
        return dummy.next


l1 = [1,4,3,2,5,2]
x = 1
head = lists = ListNode(0)
for i in l1:
    cur = ListNode(i)
    lists.next = cur
    lists = cur
head = head.next    


test = Solution()
res = test.partition(head,x)
# show lists
while res:
    print(res,res.val,res.next)
    res = res.next