#coding=utf-8
import sys 
""" Write a function to reverse a linked list.
"""
class Node(object):
    """define Node class"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    pre = None    # define return node
    cur = head
    while cur:
        nextNode = cur.next
        cur.next = pre
        pre = cur
        cur = nextNode
        
    return pre 

def getLinkedList(nums):
    """get linkedlist from nums"""
    head = dummy = Node(0)
    for n in nums:
        head.next = Node(n)
        head = head.next
    
    return dummy.next

def printLinkedList(head):
    cur = head
    print("ret: ", end=" ")
    while cur:
        print(cur.val, end=" ")
        cur = cur.next

def solver(nums):
    head = getLinkedList(nums)
    retHead = reverseLinkedList(head)
    printLinkedList(retHead)
    
def test():
    nums = [[1,2,3,4,5], [1], []]
    for n in nums:
        solver(n)
    
if __name__ == '__main__':
    test()