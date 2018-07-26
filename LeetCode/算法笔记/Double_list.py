'''
 双向链表
 python: 
    https://blog.csdn.net/qq490691606/article/details/49948263
    https://www.cnblogs.com/yupeng/p/3413800.html
 java: 
    https://www.cnblogs.com/linlf03/p/5278629.html
    https://blog.csdn.net/as02446418/article/details/47114711
'''
# 2018-7-25
"""节点类"""
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None

"""初始化双向链表"""

    def __init__(self):
        """
        设置头尾，操作比较容易
        头－－（next）－－》尾
        尾－－（pre）－－》头
        :return:
        """
        head = Node()
        tail = Node()
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.pre = self.head

    """获取链表长度"""

    def __len__(self):
        length = 0
        node = self.head
        while node.next != self.tail:
            length += 1
            node = node.next
        return length

    """追加节点"""

    def append(self, data):
        """
        :param data:
        :return:
        """
        node = Node(data)
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        self.tail.pre = node
        node.next = self.tail
        return node

     """获取节点"""
    def get(self, index):
        """
        获取第index个值，若index>0正向获取else 反向获取
        :param index:
        :return:
        """
        length = len(self)
        index = index if index >= 0 else length + index
        if index >= length or index < 0: return None
        node = self.head.next
        while index:
            node = node.next
            index -= 1
        return node

    """设置节点"""

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        return node

    """插入节点"""

    def insert(self, index, data):
        """
        因为加了头尾节点所以获取节点node就一定存在node.next 和 node.pre
        :param index:
        :param data:
        :return:
        """
        length = len(self)
        if abs(index + 1) > length:
            return False
        index = index if index >= 0 else index + 1 + length

        next_node = self.get(index)
        if next_node:
            node = Node(data)
            pre_node = next_node.pre
            pre_node.next = node
            node.pre = pre_node
            node.next = next_node
            next_node.pre = node
            return node

    """删除节点"""

    def delete(self, index):
        node = self.get(index)
        if node:
            node.pre.next = node.next
            node.next.pre = node.pre
            return True

        return False

    """反转链表"""
    def __reversed__(self):
        """
        1.node.next --> node.pre
          node.pre --> node.next
        2.head.next --> None
          tail.pre --> None
        3.head-->tail
         tail-->head
        :return:
        """
        pre_head = self.head
        tail = self.tail

        def reverse(pre_node, node):
            if node:
                next_node = node.next
                node.next = pre_node
                pre_node.pre = node
                if pre_node is self.head:
                    pre_node.next = None
                if node is self.tail:
                    node.pre = None
                return reverse(node, next_node)
            else:
                self.head = tail
                self.tail = pre_head

        return reverse(self.head, self.head.next)

    """清空链表"""
    def clear(self):
        self.head.next = self.tail
        self.tail.pre = self.head