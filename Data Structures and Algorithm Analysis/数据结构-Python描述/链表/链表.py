# Definition for singly-linked list.  
class ListNode(object):  
    def __init__(self):  
        self.val = None  
        self.next = None  

class ListNode_handle:  
    def __init__(self):  
        self.cur_node = None  
  
    def add(self, data):  
        # add a new node pointed to previous node  
        node = ListNode()  
        node.val = data  
        node.next = self.cur_node  
        self.cur_node = node  
        return node  
  
    def print_ListNode(self, node):  
        while node:  
            print ('\nnode: ', node, ' value: ', node.val, ' next: ', node.next ) 
            node = node.next  
  
    def _reverse(self, nodelist):  
        list = []  
        while nodelist:  
            list.append(nodelist.val)  
            nodelist = nodelist.next  
        result = ListNode()  
        result_handle = ListNode_handle()  
        for i in list:  
            result = result_handle.add(i)  
        return result  
        
ListNode_1 = ListNode_handle()  
# l1 = ListNode()  
l1_list = [1,8,3]  
for i in l1_list:  
    l1 = ListNode_1.add(i)
# l1 = ListNode_1._reverse(l1)
ListNode_1.print_ListNode(l1)