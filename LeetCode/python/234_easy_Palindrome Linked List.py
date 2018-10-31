'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# 2018-10-30
# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]



class Solution2:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return True

        def reverseLinkedList(head):
            prev = None
            while head:
                myNext = head.next
                head.next = prev
                prev = head
                head = myNext
            return prev

        # find the middle of a linked list in running time O(N) and space O(1)
        slow, fast = head, head
        
        # Do not increase extra space, just move the place where slow, fast
        # point to step by step
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # now slow point at the begining of the last half linked list
        # slow = slow.next
        # reverse the slow part
        rev = reverseLinkedList(slow)
        while rev:
            if head.val != rev.val:
                return False   
            head = head.next
            rev = rev.next
            
        return True
        

# class Solution:
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         slow, fast, prev = head, head, None
#         while fast and fast.next:
#             fast = fast.next.next
#             slow.next, prev, slow = prev, slow, slow.next
            
#         if fast:
#             slow = slow.next
            
#         while slow and prev:
#             if slow.val != prev.val:
#                 return False
#             prev, slow = slow.next, prev.next
#         return True