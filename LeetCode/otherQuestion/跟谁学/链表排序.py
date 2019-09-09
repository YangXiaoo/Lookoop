# coding:utf-8
# 链表排序
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next

def getLinkedList(nums):
    """根据数组生成链表，返回链表头节点"""
    dummy = head = ListNode(0)
    for n in nums:
        curNode = ListNode(n)
        dummy.next = curNode
        dummy = curNode

    return head.next

def printLinkedList(head):
    """打印链表"""
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


def solver(head):
	"""使用插入排序或者归并排序, 推荐使用归并排序"""
	dummy = head
	dummy.next = None
	cur = head.next

	while cur != None:
		pre = dummy
		while pre.next != None and pre.next.val > cur.val:
			pre = pre.next

		nextNode = cur.next 
		preNext = pre.next 
		pre.next = cur
		cur.next = preNext
		cur = nextNode

	return dummy

def solver2(head):
	"""使用归并排序"""
	# 使用快慢指针获得两段链表
	# 使用归并算法进行排序
	pass 

def test():
	nums = [1,4,5,2,3,8,7]
	head = getLinkedList(nums)

	ret = solver(head)
	printLinkedList(ret)

if __name__ == '__main__':
	test()