'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# 2018-10-1
# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        lists = dummy = ListNode(0)
        while head:
            if head.val != val:
                dummy.next = ListNode(head.val)
                dummy = dummy.next
            head = head.next
        return lists.next

class Solution2(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        lists = dummy = ListNode(0)
        while head:
            if head.val != val:
                dummy.next = head
            else:
                dummy.next = head.next
            head = head.next
        return lists.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

dummy = List = ListNode(0)
nums = [1,2,3,6,4,5,6]
val = 6
for i in nums:
    dummy.next = ListNode(i)
    dummy = dummy.next
List = List.next

test = Solution2()
res = test.removeElements(List, val)
r = []
while res:
    print(res)
    r.append(res.val)
    res = res.next
print(r)