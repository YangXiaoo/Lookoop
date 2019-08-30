# coding=utf-8
import sys 
# 环形链表实现队列
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class Queue(object):
    def __init__(self, size=10):
        self.size = size    # 队列大小
        self.head = None    
        self.tail = None
        self.init()
    
    def init(self):
        """初始化链表"""
        self.head = self.tail = Node()    # 头结点
        for i in range(self.size - 1):
            curNode = Node()
            self.tail.next = curNode
            self.tail = self.tail.next
            
        self.tail.next = self.head    # 头尾相连
        self.tail = self.head    # 初始时链表中无数据
            
    def add(self, val):
        """添加一个节点"""
        print("[DEBUG] add node val:{}".format(val))
        if self.tail.next != self.head:
            self.tail.val = val
            self.tail = self.tail.next
        else:
            self.resize()    # 扩容
            self.add(val)
    
    def resize(self):
        """链表扩容"""
        newSize = int(self.size * 1.5)    # 扩容1.5倍长度
        curTail = self.tail     # 当前链表尾节点
        for i in range(self.size, newSize):
            cur = Node()
            curTail.next = cur
            curTail = cur

        print("[DEBUG] resize queue, old size:{}, newSize:{}".format(self.size, newSize))
        self.size = newSize         # 面试时没有考虑，导致有问题
        curTail.next = self.head    # 头尾相接
        
        
    def remove(self):
        """删除一个节点，删除头结点"""
        if self.head == self.tail:
            print("[WARNING] queue is empty")
        else:
            print("[INFO] delete node val:{}".format(self.head.val))
            self.head.val = None
            self.head = self.head.next    # 下一个节点
            
            # self.shrink()    # 删除多余节点
def test():
    queue = Queue()
    for i in range(20):
        queue.add(i)
    for i in range(24):
        queue.remove()

if __name__ == '__main__':
    test()

"""
[DEBUG] add node val:0
[DEBUG] add node val:1
[DEBUG] add node val:2
[DEBUG] add node val:3
[DEBUG] add node val:4
[DEBUG] add node val:5
[DEBUG] add node val:6
[DEBUG] add node val:7
[DEBUG] add node val:8
[DEBUG] add node val:9
[DEBUG] resize queue, old size:10, newSize:15
[DEBUG] add node val:9
[DEBUG] add node val:10
[DEBUG] add node val:11
[DEBUG] add node val:12
[DEBUG] add node val:13
[DEBUG] add node val:14
[DEBUG] resize queue, old size:15, newSize:22
[DEBUG] add node val:14
[DEBUG] add node val:15
[DEBUG] add node val:16
[DEBUG] add node val:17
[DEBUG] add node val:18
[DEBUG] add node val:19
[INFO] delete node val:0
[INFO] delete node val:1
[INFO] delete node val:2
[INFO] delete node val:3
[INFO] delete node val:4
[INFO] delete node val:5
[INFO] delete node val:6
[INFO] delete node val:7
[INFO] delete node val:8
[INFO] delete node val:9
[INFO] delete node val:10
[INFO] delete node val:11
[INFO] delete node val:12
[INFO] delete node val:13
[INFO] delete node val:14
[INFO] delete node val:15
[INFO] delete node val:16
[INFO] delete node val:17
[INFO] delete node val:18
[INFO] delete node val:19
[ERROR] queue is empty
[ERROR] queue is empty
[ERROR] queue is empty
[ERROR] queue is empty
"""