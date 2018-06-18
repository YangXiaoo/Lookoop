'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''



# 2018-6-18
# Merge k Sorted Lists
# 超出内存限制
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        lens = len(lists)
        if lens == 0:
            return lists
        res = self.toLists(res,lists)
        res = sorted(res)
        dummy = l = ListNode(0)
        for i in res:
            cur = ListNode(i)
            l.next = cur
            l = cur
        return dummy.next

    def toLists(self,res,lists):
        if len(lists) == 0:
            return res
        head = lists[0]
        while head:
            res.append(head.val)
            head = head.next
        return self.toLists(res,lists[1:])






lis = [[1,2,4],[1,3,4],[7],[49],[73],[58],[30],[72],[44],[78],[23],[9],[40],[65],[92],[42],[87],[3],[27],[29],[40],[12],[3],[69],[9]]
l = []
for j in lis:
    head = lists = ListNode(0)
    for i in j:
        cur = ListNode(i)
        lists.next = cur
        lists = cur
    l.append(head.next)    


test = Solution()
res = test.mergeKLists(l)
# show lists
while res:
    print(res,res.val,res.next)
    res = res.next