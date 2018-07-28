'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# 2018-6-17
# Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 组合成数组然后形成链表
class Solution1:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lists = []
        while l1:
        	lists.append(l1.val)
        	l1 = l1.next
        while l2:
        	lists.append(l2.val)
        	l2 = l2.next
        lists = sorted(lists)
        head = lis = ListNode(0)
        for i in lists:
        	cur = ListNode(i)
        	lis.next = cur
        	lis = cur
        return head.next


# 直接形成链表
class Solution2:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=a=ListNode(0)
        while l1 and l2:
            if l1.val>l2.val:
                a.next=l2
                l2=l2.next
            else:
                a.next=l1
                l1=l1.next
            a=a.next
        a.next=l1 or l2
        return head.next

l1 = [1,2,4]
l2 = [1,3,4]
head = lists = ListNode(0)
for i in l1:
    cur = ListNode(i)
    lists.next = cur
    lists = cur
l1 = head.next    

head = lists = ListNode(0)
for i in l2:
    cur = ListNode(i)
    lists.next = cur
    lists = cur    
l2 = head.next

test = Solution2()
res = test.mergeTwoLists(l1,l2)
# show lists
while res:
    print(res,res.val,res.next)
    res = res.next