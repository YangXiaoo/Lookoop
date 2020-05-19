# coding:utf-8
# start: 2020-5-15
# 剑指offer内容

class TreeNode(object):
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val 
        self.left = left
        self.right = right
        self.parent = parent
# tree
def getTree():
    """
        10
        /\
       5 12
      / \
     4  7
    """
    rootLeft = TreeNode(5, TreeNode(4), TreeNode(7))
    rootRight = TreeNode(12)
    root = TreeNode(10, rootLeft, rootRight)

    return root
def printTreePreorder(head):
    if head != None:
        print(head.val)
        printTreePreorder(head.left)
        printTreePreorder(head.right)

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

#######################################
# 03 数组中重复的数字
def findDuplicate(nums):
    """[2,3,1,0,2,5,3]"""
    for i in range(len(nums)):
        while i != nums[i]:
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    return -1

def testFindDuplicate():
    nums = [2,3,1,0,2,5,3]
    ret = findDuplicate(nums)
    print(ret)

# testFindDuplicate()

#######################################
# 06 从尾到头打印链表
def printLinkReversed(node):
    if node != None:
        printLinkReversed(node.next)
        print(node.val)

def testprintLinkReversed():
    nums = [1,2,3,4,5]
    node = getLinkedList(nums)
    printLinkReversed(node)

# testprintLinkReversed()

#######################################
# 07 重建二叉树, leetcode-105
def construct(preOrder, inOrder):
    def helper(preLeft, preRight, inLeft, inRight):
        nonlocal preOrder, inOrder
        if preLeft > preRight or inLeft > inRight:
            return None
        head = TreeNode(preOrder[preLeft])
        inIndex = inLeft
        for i, n in enumerate(inOrder):
            if n == preOrder[preLeft]:
                inIndex = i 
                break
        curLens = inIndex - inLeft
        head.left = helper(preLeft+1, preRight+curLens, inLeft, inIndex-1)
        head.right = helper(preLeft+curLens+1, preRight, inIndex+1, inRight)

        return head

    if len(preOrder) == 0 or (len(preOrder) != len(inOrder)):
        return None

    preLeft, preRight, inLeft, inRight = 0, len(preOrder)-1, 0, len(inOrder) - 1

    return helper(preLeft, preRight, inLeft, inRight)

def testConstruct():
    preOrder = [1,2,4,7,3,5,6,8]
    inOrder = [4,7,2,1,5,3,8,6]
    head = construct(preOrder, inOrder)
    printTreePreorder(head)

# testConstruct()

#######################################
# 08 二叉树的下一个节点
def nextNode(tree, node):
    if tree == None:
        return 

    nextNode = None
    if node.parent == None:
        if node.right != None:
            curNext = node.right
            while curNext != None:
                nextNode = curNext
                curNext = curNext.left 
    else:
        parent = node.parent
        if parent.right != node:
            nextNode = parent
        else:
            curNext = node.right
            while curNext != None:
                nextNode = curNext
                curNext = curNext.left

    return nextNode

def test_nextNode():
    """
        10
        /\
       5 12
      / \
     4  7
    """
    node_10 = TreeNode(10)
    node_5 = TreeNode(5)
    node_12 = TreeNode(12)
    node_4 = TreeNode(4)
    node_7 = TreeNode(7)

    node_10.left, node_10.right = node_5, node_12
    node_5.left, node_5.right = node_4, node_7
    node_5.parent, node_12.parent = node_10, node_10
    node_4.parent, node_7.parent = node_5, node_5

    ret1 = nextNode(node_10, node_4)
    ret2 = nextNode(node_10, node_10)
    ret3 = nextNode(node_10, node_12)
    ret4 = nextNode(node_10, node_5)
    ret5 = nextNode(node_10, node_7)

    print(ret1.val, ret2.val, ret3, ret4.val, ret5)

# test_nextNode()

#######################################
# 09 用两个栈实现队列
class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            print("[WARNING INFO] Queue is empty!")
            return None

        return self.stack2.pop()

def test_Queue():
    queue = Queue()
    print(queue.pop())
    queue.push(1)
    queue.push(2)
    print(queue.pop())
    queue.push(3)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

# test_Queue()

#######################################
# 11 旋转数组中的最小数字
def minNumInRoationNums(nums):
    """[3,4,5,1,2], [4,5,1,2,3]
    [2,1] - 1
    """
    if len(nums) == 0:
        return None

    left, right, mid = 0, len(nums) - 1, 0
    
    while right >= left:
        mid = left + ((right - left) >> 1)
        if right - left == 1:
            mid = right
            break

        if nums[left] <= nums[mid]:
            left = mid
        elif nums[mid] <= nums[right]:
            right = mid 

    return nums[mid]

def test_minNumInRoationNums():
    nums1 = [3,4,5,1,2]
    print(minNumInRoationNums(nums1))
    nums2 = [4,5,1,2,3]
    print(minNumInRoationNums(nums2))
    nums3 = [2,1]
    print(minNumInRoationNums(nums3))

# test_minNumInRoationNums()

# 17 打印从1到最大的n位数

#######################################
# 18 删除链表的节点
def deleteDuplicateNode(head, node):
    if not head:
        return 

    # 如果是尾结点
    if node.next != None:
        nextNode = node.next 
        node.val = nextNode.val
        node.next = nextNode.next
    elif node == head: 
        head = None
    else:
        preNode = head
        while preNode.next != node:
            preNode = preNode.next

        preNode.next = None


def test_deleteDuplicateNode():
    head = ListNode(0)
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_3.next = node_4
    node_2.next = node_3
    node_1.next = node_2
    head.next = node_1
    
    deleteDuplicateNode(head, node_4)
    printLinkedList(head)

    deleteDuplicateNode(head, node_2)
    printLinkedList(head)

    deleteDuplicateNode(head, head)
    printLinkedList(head)

    deleteDuplicateNode(head, head)
    printLinkedList(head)

# test_deleteDuplicateNode()

#######################################
# 20 表示数值的字符串
def numericStrings(string):
    def scanInteger(string):
        nonlocal pIndex
        if pIndex >= len(string): return False
        if string[pIndex] == '+' or string[pIndex] == '-':
            pIndex += 1

        return scanUnsignInteger(string)

    def scanUnsignInteger(string):
        nonlocal pIndex
        before = pIndex
        while pIndex < len(string) and string[pIndex] >= '0' and string[pIndex] <= '9':
            pIndex += 1

        return pIndex > before

    length = len(string)
    pIndex = 0
    numeric = scanInteger(string)

    if pIndex < length and string[pIndex] == '.':
        pIndex += 1
        numeric = scanUnsignInteger(string) or numeric  # 1. 小数可以没有整数部分
                                                        # 2. 小数点后面可以没有数字
                                                        # 3. 小数点前后都有数字

    if pIndex < length and (string[pIndex] == 'e' or string[pIndex] == 'E'):
        pIndex += 1
        numeric = numeric and scanInteger(string)


    return numeric and (pIndex == length)

def test_numericStrings():
    string = ["+100", "+5e2","3.14156", "1E-16", ".123", "123.", 
                "12e","1.2.3"]
    for s in string:
        print(numericStrings(s))

# test_numericStrings()

#######################################
# 21 调整数组顺序使奇数位于偶数前面
def reorderOddEvent(nums):
    """[1,2,3,4,5,6,7]"""
    def event(num):
        return (num % 2) == 0

    leftIndex, rightIndex = 0, len(nums) - 1 
    while leftIndex < rightIndex:
        while leftIndex < rightIndex and not event(nums[leftIndex]):
            leftIndex += 1

        while leftIndex < rightIndex and event(nums[rightIndex]):
            rightIndex -= 1

        if leftIndex < rightIndex:
            nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]


    return nums

def test_reorderOddEvent():
    nums = [1,2,3,4,5,6,7,3,3]
    ret = reorderOddEvent(nums)
    print(ret)

# test_reorderOddEvent()

#######################################
# 22 链表中倒数第k个节点
def findKthToTail(head, k):
    node1, node2 = head, head
    for i in range(k):
        if node2:
            node2 = node2.next
        else:
            return None

    while node2:
        node1 = node1.next
        node2 = node2.next 

    return node1.val 

def test_findKthToTail():
    nums = [1,2,3,4,5,6,7]
    k = 20
    head = getLinkedList(nums)

    ret = findKthToTail(head, k)
    print(ret)

# test_findKthToTail()

#######################################
# 24 翻转链表
def reverseLinkedList(head):
    pre, cur = None, head
    while cur:
        nextNode = cur.next 
        cur.next = pre 
        pre = cur 
        cur = nextNode

    return pre 

def test_reverseLinkedList():
    nums = [1,2,3,4,5,6]
    head = getLinkedList(nums)
    ret = reverseLinkedList(head)
    printLinkedList(ret)

# test_reverseLinkedList()

#######################################
# 25 合并两个递增排序的链表
def mergeLinkedList(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    head = None
    if head1.val < head2.val:
        head = head1
        head.next = mergeLinkedList(head1.next, head2)

    else:
        head = head2
        head.next = mergeLinkedList(head1, head2.next)

    return head

def test_mergeLinkedList():
    nums1 = [2,5,7,9,13]
    nums2 = [6,7,8,15,34]
    head1 = getLinkedList(nums1)
    head2 = getLinkedList(nums2)
    ret = mergeLinkedList(head1, head2)
    printLinkedList(ret)

# test_mergeLinkedList()

#######################################
# 26 树的子结构
def subTree(root, node):
    """输入两棵二叉树"""
    def checkNode(node1, node2):
        if node2 == None:
            return True
        if node1 == None:
            return False

        if node1.val != node2.val:
            return False

        return checkNode(node1.left, node2.left) and checkNode(node1.right, node2.right)
    if not node:
        return True
    if not root:
        return False

    ret = False
    if root.val == node.val:
        ret = checkNode(root, node)
    if not ret:
        ret = subTree(root.left, node)

    if not ret:
        ret = subTree(root.right, node)

    return ret

def test_subTree():
    rootLeft = TreeNode(5, TreeNode(4), TreeNode(7))
    rootRight = TreeNode(12)
    root = TreeNode(10, rootLeft, rootRight)

    node = TreeNode(5, TreeNode(4), TreeNode(7))

    ret = subTree(root, node)
    print(ret)

test_subTree()