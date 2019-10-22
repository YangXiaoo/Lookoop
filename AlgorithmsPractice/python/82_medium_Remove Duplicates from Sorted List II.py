"""

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# 2018-6-27
# Remove Duplicates from Sorted List II
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        old_val = 0
        nums = []
        h = head
        while head:
            nums.append(head.val)
            head = head.next
        dic = {}
        i = 0
        tmp = []
        while i < len(nums):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
            i += 1
        j = 0
        while j < len(nums):
            if dic[nums[j]] == 1:
                tmp.append(nums[j])
            j += 1
        dummy = li = ListNode(0)
        for n in tmp:
            cur = ListNode(n)
            li.next = cur
            li = cur

        return dummy.next

class Solution2:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        map = []
        h = dummy = ListNode(0)
        pre = head

        while head:
            if head.val not in map:
                map.append(head.val)
                dummy.next = head
                pre = dummy
                dummy = dummy.next

            else:
                pre.next = None
                dummy = pre
            head = head.next
        return h.next
        

l1 = [1,2,2,3]
head = lists = ListNode(0)
for i in l1:
    cur = ListNode(i)
    lists.next = cur
    lists = cur
head = head.next    


test = Solution2()
res = test.deleteDuplicates(head)
# show lists
while res:
    print(res,res.val,res.next)
    res = res.next