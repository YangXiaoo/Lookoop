'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# 2018-6-18
# Reverse Nodes in k-Group
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = lis = ListNode(0)
        h = head
        c = 0
        while h:
        	c += 1
        	h = h.next
        e = c//k
        j = 0
        # print(head,e)
        while head and j < e:
        	tmp = []
        	i = 0
        	while  i < k:
        		# print(head,head.val)
        		tmp.append(head.val)
        		head = head.next
        		i += 1
        	# print(tmp)
        	for m in range(len(tmp)-1,-1,-1):
        		cur = ListNode(tmp[m])
        		lis.next = cur
        		lis = cur
        	j += 1
        while head:
        	cur = ListNode(head.val)
        	lis.next = cur
        	lis = cur
        	head = head.next
        return dummy.next





lis = [1,2,3,4,5,6,7,8,9,10]
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
res = test.reverseKGroup(head,5)
while res:
    print(res,res.val,res.next)
    res = res.next
