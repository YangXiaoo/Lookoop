# coding:utf-8
# start: 2020-5-15
# 剑指offer内容
from queue import PriorityQueue, Queue
import heapq

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
class _Queue():
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
    queue = _Queue()
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

# test_subTree()

#######################################
# 最长公共子字符串
def getLCS(s1, s2):
    dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    maxLength = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = 0

            maxLength = max(maxLength, dp[i][j])

    return maxLength

def test_getLCS():
    s1 = "acbcbcef"
    s2 = "abcbced"

    ret = getLCS(s1, s2)
    print(ret)

# test_getLCS()

#######################################
# 27 二叉树的镜像
def mirrorTree(root):
    if root == None: return 
    if root.left == None and root.right == None: return 

    root.left, root.right =  root.right, root.left 

    if root.left:
        mirrorTree(root.left)

    if root.right:
        mirrorTree(root.right)

def invertTree(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend([node.left, node.right])
    return root

def test_mirrorTree():
    root = getTree()
    ret = mirrorTree(root)

    printTreePreorder(root)

def test_invertTree():
    root = getTree()
    ret = invertTree(root)
    printTreePreorder(ret)

# test_mirrorTree()
# test_invertTree()

#######################################
# 28 对称的二叉树

#######################################
# 29 顺时针打印矩阵

#######################################
# 31 栈的压入弹出顺序
def isPopOrder(push, pop):
    pass

#######################################
# 32 从上到下打印二叉树
def printTreeFromTop2Bottom(root):
    stack = [root]
    while stack:
        curSize = len(stack)
        tmp = []
        for i in range(curSize):
            cur = stack.pop()
            print(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)

        stack = tmp[::-1]

def test_printTreeFromTop2Bottom():
    root = getTree()
    printTreeFromTop2Bottom(root)

# test_printTreeFromTop2Bottom()

#######################################
# 33 二叉搜索树的后续遍历序列
def verifyBST(seq):
    pass

#######################################
# 34 二叉树中和为某一值的路径 
# LC-113(bbc), 114(bbd)
def pathSum(root, sums):
    pass

#######################################
# 35 复杂链表的复制
# LC-138
def copyLinkedList(head):
    insertNewNode(head)
    linkedRandomNode(head)
    newHead = splitLinkedList(head)

#######################################
# 36 二叉搜索树与双向链表
def convertBSTToLinkedList(root):
    pass

#######################################
# 38 字符串的排序
def stringPermutation(s):
    pass

#######################################
# 39 数组中出现次数超过一半的数字

#######################################
# 40 最小的K个数
# 23 merge k sorted list
def minK(nums, k):
    q = PriorityQueue()
    for n in nums:
        q.put(tuple([n, n]))

    ret = []
    for j in range(k):
        ret.append(q.get()[-1])

    return ret 

def test_minK():
    nums = [4,5,1,6,2,7,3,8]
    k = 4
    ret = minK(nums, k)
    print(ret)

# test_minK()
#######################################
# 41 数据流中的中位数
class medianNumber():
    """最小堆与最大堆组合"""
    def __init__(self):
        self.minStack = []
        self.maxStack = []

    def peekMin(self):
        return self.minStack[0]

    def popMin(self):
        return heapq.heappop(self.minStack)

    def peekMax(self):
        return -self.maxStack[0]

    def popMax(self):
        return heapq.heappop(self.maxStack)

    def pushMin(self, x):
        heapq.heappush(self.minStack, x)

    def pushMax(self, x):
        heapq.heappush(self.maxStack, -x)

    def insert(self, num):
        """插入数据"""
        if (len(self.minStack) + len(self.maxStack)) & 1 == 0:
            if len(self.maxStack) != 0 and self.peekMax() > num:
                tmp = self.popMax()
                self.pushMax(num)
                num = tmp
            self.pushMin(num)
        else:
            if len(self.minStack) != 0 and self.peekMin() < num:
                tmp = self.popMin()
                self.pushMin(num)
                num = tmp 
            self.pushMax(num)

    def getMedian(self):
        """偶数长度则取中间两个数的平均值，奇数长度则取中间数"""
        numsSize = len(self.minStack) + len(self.maxStack)

        if numsSize == 0:
            return '-1'

        median = 0
        if numsSize & 1 == 0:
            median = (self.peekMin() + self.peekMax()) / 2.0
        else:
            median = self.peekMin()

        return median

def test_medianNumber():
    nums = [1,2,3,4,5,6,7,8,9,10]
    q = medianNumber()
    tmp = []
    for n in nums:
        q.insert(n)
        tmp.append(n)
        median = q.getMedian()
        print("data: {}, median: {}".format(tmp, median))

# test_medianNumber()

#######################################
# 42 连续子数组的最大和(最长递增数组)
# LC-54
def findGreastSumOfSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] +=  nums[i-1]
    return max(nums)

def test_findGreastSumOfSubArray():
    nums = [1,-2,3,10,-4,7,2,-5]
    ret = findGreastSumOfSubArray(nums)
    print(ret)

# test_findGreastSumOfSubArray()

#######################################
# 45 把数组排成最小的数
def getMinNumber(nums):
    sNums = [str(n) for n in nums]
    for i in range(1, len(nums)):
        leftComb = sNums[i-1] + sNums[i]
        rightComb = sNums[i] + sNums[i-1]
        if leftComb < rightComb:
            sNums[i] = leftComb
        else:
            sNums[i] = rightComb

    return sNums[-1]

def test_getMinNumber():
    nums = [3, 32, 321]
    ret = getMinNumber(nums)
    print(ret)

# test_getMinNumber()

#######################################
# 46 把数字翻译成字符串
# LC-91
def translateNumbers2String(num):
    if num < 0: return 0
    strNum = str(num)
    dp = [1] + [0 for _ in strNum]
    dp[1] = 1
    for i in range(1, len(strNum)):
        dp[i+1] += dp[i]
        if strNum[i-1] == '0': continue
        curComb = strNum[i-1] + strNum[i]
        if int(curComb) < 26:
            dp[i+1] += dp[i-1]
    return dp[-1]

def isValidAlpha(s1, s2):
    if int(s1+s2) < 26:
        return True

def translateNumbers2String_2(num):
    def helper(s):
        nonlocal ret
        if len(s) == 0: ret += 1

        if len(s) > 0:
            helper(s[1:])

        if len(s) > 1:
            if isValidAlpha(s[0], s[1]):
                helper(s[2:])
    strNum = str(num)
    ret = 0
    if len(strNum) == 0:
        return ret 
    helper(strNum)

    return ret 

def test_translateNumbers2String():
    num = 12258
    ret = translateNumbers2String_2(num)
    print(ret)

# test_translateNumbers2String()

#######################################
# 47 礼物的最大价值
def getMaxValueOfPresent(values):
    row, col = len(values), len(values[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = values[0][0]
    
    for r in range(1, row):
        dp[r][0] = dp[r-1][0] + values[r][0]
    for c in range(col):
        dp[0][c] = dp[0][c-1] + values[0][c]

    for r in range(1, row):
        for c in range(1, col):
            dp[r][c] = values[r][c] + max(dp[r-1][c], dp[r][c-1])

    return dp[-1][-1]

def test_getMaxValueOfPresent():
    values = [
        [1,10,3,8],
        [12,2,9,6],
        [5,7,4,11],
        [3,7,16,5]
    ]

    ret = getMaxValueOfPresent(values)
    print(ret)

# test_getMaxValueOfPresent()

#######################################
# 48 最长不含重复字符串的子字符串
def longestSubstringWithoutDuplication(s):
    container = [-1 for i in range(127)]
    preIndex = -1
    maxLength = 0
    for i, c in enumerate(s):
        cur = ord(c)
        oldIndex = container[cur]
        container[cur] = i
        if oldIndex != -1 and oldIndex > preIndex:
            preIndex = oldIndex
        
        maxLength = max(maxLength, i - preIndex)

    return maxLength

def test_longestSubstringWithoutDuplication():
    s = "arabcacfr"
    ret = longestSubstringWithoutDuplication(s)
    print(ret)

# test_longestSubstringWithoutDuplication()

#######################################
# 49 丑数
def uglyNumber(index):
    """只包含2,3,5的数称为丑数，获得第index个顺序的丑数"""
    pass

#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
