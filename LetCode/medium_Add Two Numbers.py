'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# 2018-6-14
# add two numbers

class ListNodes(object):  
    def __init__(self):  
        self.val = None  
        self.next = None  

class ListNode_handle:  
    def __init__(self):  
        self.cur_node = None  
  
    def add(self, data):  
        # add a new node pointed to previous node  
        node = ListNodes()  
        node.val = data  
        node.next = self.cur_node  
        self.cur_node = node  
        return node        

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next

def handle(l1, l2):
    # check solution
    ListNode_1 = ListNode_handle() 
    ListNode_2 = ListNode_handle() 
    
    for i in l1:
        l_1 = ListNode_1.add(i)
    for i in l2:
        l_2 = ListNode_2.add(i)

    test = Solution()
    re = test.addTwoNumbers(l_1, l_2)

    while re:
        print(re.val)
        re = re.next

# test
l1 = [2,4,3]
l2 = [5,6,4]
handle(l1, l2)
