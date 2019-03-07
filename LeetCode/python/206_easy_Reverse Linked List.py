'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# 2018-10-4
# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# iteratively
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        new_node = old_node = ListNode(head.val)

        while head.next != None:
            # print(head.val)
            new_node = ListNode(head.next.val)
            new_node.next = old_node
            old_node = new_node
            head = head.next

        return new_node



# recursively
class Solution2(object):
    def __init__(self):
        self.que = []
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.que.append(head.val)
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        # print(head.val)
        head.next.next = head
        head.next = None
        # print(self.que)
        return node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next
        return pre



# python3.6 新特性
from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]

def inproduct(v: Vector[T]) -> T:
    return sum(x*y for x, y in v)


def dilate(v: Vector[T], scale: T) -> Vector[T]:
    return ((x * scale, y * scale) for x, y in v)
vec = []  # type: Vector[float]




nums = [1,2,3,4,5]
li = dummy = ListNode(0)
for i in nums:
    dummy.next = ListNode(i)
    dummy = dummy.next
li = li.next

test = Solution3() 
res = test.reverseList(li)
while res != None:
    r = res.val
    print(r)
    res = res.next

