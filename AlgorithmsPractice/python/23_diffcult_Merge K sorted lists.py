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


#######################################################################
from queue import PriorityQueue

# class Comp:                  # 可比较对象，放入优先队列中
#     def __init__(self, priority, description):
#         self.priority = priority
#         self.description = description
#         return 

#     def __cmp__(self, other):         # 比较规则的指定，谁做根（大顶堆，小顶堆）
#                                       # 返回的是布尔类型
#         if self.priority >= other.priority:
#             return True
#         else:
#             return False

class Solution2(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()

        for index, node in enumerate(lists):
            if node:
                # print(node.val)
                # 有问题 unorderable types: ListNode() < ListNode()
                # q.put((node.val, node))
                q.put((node.val, index, node))

        while q.qsize() > 0:
            cur = q.get()
            curr.next, index = cur[2], cur[1]
            curr = curr.next
            if curr.next: 
                q.put((curr.next.val, index, curr.next))
        return dummy.next



lis = [[1,2,4],[1,3,4],[7],[49],[73],[58],[30],[72],[44],[78],[23],[9],[40],[65],[92],[42],[87],[3],[27],[29],[40],[12],[3],[69],[9]]
l = []
for j in lis:
    head = lists = ListNode(0)
    for i in j:
        cur = ListNode(i)
        lists.next = cur
        lists = cur
    l.append(head.next)    

test = Solution2()
res = test.mergeKLists(l)
# show lists
while res:
    print(res.val)
    res = res.next