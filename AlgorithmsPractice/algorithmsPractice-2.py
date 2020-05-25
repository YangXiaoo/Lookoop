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
# 23 链表中环的入口
# LC-142
def entryNodeOfLoopLinkedList(head):
    pass

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
def isSymetry(root):
    pass

#######################################
# 29 顺时针打印矩阵
def printMatrixClockwisely(maxtrix):
    pass

#######################################
# 30 包含min函数的栈
class Stack():
    pass

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
# 37 序列化二叉树
def serialize(root):
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
# 43 1~n整数中1出现的次数
def numberOf1Between1AndN(n):
    pass

#######################################
# 44 数字序列中某一位的数字
def digitInSerial(index):
    pass
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
    
################### 2020-5-23 #####################
# 50 第一个只出现一次的字符
def firstNotRepeatingChar(s):
    table = [0 for _ in range(256)] # 字符长度为女8即256种可能
    for i in range(len(s)):
        index = ord(s[i])
        table[index] += 1
    for i in range(len(s)):
        if table[ord(s[i])] == 1:
            return s[i]

    return '\0'

def test_firstNotRepeatingChar():
    s = "abaccdeff"
    ret = firstNotRepeatingChar(s)
    print(ret)

# test_firstNotRepeatingChar()

#######################################
# 51 数组中的逆序对
def inversePair(nums):
    """[7,5,6,4]-->[7,6], [7,5], [7,4], [6,4], [5,4]"""
    def helper(nums):
        nonlocal ret 
        if len(nums) == 1 or len(nums) == 0: return nums
        mid = len(nums) >> 1
        left = helper(nums[:mid])
        right = helper(nums[mid:])

        seq = []
        while len(left) > 0 and len(right) > 0:
            if left[-1] > right[-1]:
                seq.insert(0, right[-1])
                for n in left:
                    ret.append([n, right[-1]])
                right.pop()
            else:
                seq.insert(0, left[-1])
                left.pop()

        seq = left + seq
        seq = right + seq
        # print(seq, ret)
        return seq

    ret = []
    helper(nums)

    return ret 

def test_inversePair():
    nums = [7, 5, 6, 4]
    print(inversePair(nums)) 

# test_inversePair()

#######################################
# 52 两个链表的第一个公共节点
def firstCommonNodeOfLinkedList(head1, head2):
    pass

#######################################
# 53 在排序数组中查找数字
# LC-34
def getCounterOfN(nums, n):
    """数字在排序数组中出现的次数"""
    pass

def getMissingNumber(nums):
    """0~n-1中缺失的数字
    转换为其它问题
    """
    pass

def getNumberSameAsIndex(nums):
    """数组中数值和下标相等的元素
    单调递增的数组里的每一个元素都是整数并且唯一，找出数组中任意一个数值等于其下标的元素
    """
    pass

#######################################
# 54 二叉搜索树的第K大节点
def kthNodeOfBinaryTree(root, k):
    def helper(root):
        nonlocal k 
        ret = None
        if root.left:
            ret = helper(root.left)
        
        if not ret:
            if k != 1:
                k -= 1
            else:
                ret = root 

        if not ret and root.right:
            ret = helper(root.right)

        return ret 
    ret = helper(root)

    return ret

def test_kthNodeOfBinaryTree():
    """
        10
        /\
       5 12
      / \
     4  7
    """
    root = getTree()
    ks = [1,2,3,4,5]
    for k in ks:
        ret = kthNodeOfBinaryTree(root, k)
        print(ret.val)

# test_kthNodeOfBinaryTree()

#######################################
# 55 二叉树的深度
def maxDepthOfTree(root:TreeNode) -> int:
    if not root:
        return 0
    left = maxDepthOfTree(root.left)
    right = maxDepthOfTree(root.right)

    return 1 + max(left, right)

def test_maxDepthOfTree() -> None:
    root = getTree()
    ret = maxDepthOfTree(root)

    print(ret)

# test_maxDepthOfTree()

#######################################
# 55-2 判断平衡二叉树
def isBalanceTree(root) -> bool:
    """dfs"""
    if not root:
        return True

    if abs(maxDepthOfTree(root.left) - maxDepthOfTree(root.right)) > 1:
        return False

    return isBalanceTree(root.left) and isBalanceTree(root.right)

def isBalanceTree2(root) -> bool:
    """通过BFS，可以提前截断"""
    if not root:
        return True

    stack = [root]
    minDepth = 0
    curDepth = 0
    while stack:
        curSize = len(stack)
        tmp = []
        curDepth += 1
        while curSize != 0:
            curRoot = stack.pop()
            if not curRoot.left and not curRoot.right:
                if minDepth == 0:
                    minDepth = curDepth
                else:
                    stack = []
                    break
            if curRoot.left:
                tmp.append(curRoot.left)
            if curRoot.right:
                tmp.append(curRoot.right)

            curSize -= 1

        stack = tmp[:]
        # print(stack, curDepth)

    # print(curDepth, minDepth)
    return [False, True][curDepth-minDepth <= 1]

def test_isBalanceTree() -> None:
    root = getTree()

    ret = isBalanceTree2(root)
    print(ret)

# test_isBalanceTree()

#######################################
# 55-3 最小二叉树
# LC-111
def minDepthOfTree(root):
    """二叉树最小深度"""
    pass

#######################################
# 56-0 数组中只出现一次的一个数字
# LC-136
def findOneNumAppearOnce(nums):
    n = nums[0]
    for x in nums[1:]:
        n = n ^ x

    return n

def findOneNumAppearOnce2(nums):
    """使用字典即可解决"""
    pass

def test_findOneNumAppearOnce():
    nums = [2, 5, 3, 4, 7, 3, 4, 2, 5]
    ret = findOneNumAppearOnce(nums)
    print(ret)

# test_findOneNumAppearOnce()

#######################################
# 56-1 数组中只出现一次的两个数字
def findTwoNumAppearOnce(nums):
    """数组中只有两个数字出现一次，其余数字出现两次"""
    xor = 0
    for n in nums:
        xor ^= n 

    index = findLast1BitIndex(xor)

    num1, num2 = 0, 0
    for n in nums:
        is1Bit = (n >> index) & 1
        if is1Bit:
            num1 ^= n 
        else:
            num2 ^= n 

    return num1, num2 

def findLast1BitIndex(n):
    """寻找二进制中最右边第一个出现的1的索引"""
    lastIndex = 0
    while n and n & 1 == 0:
        lastIndex += 1
        n >>= 1

    return lastIndex

def test_findTwoNumAppearOnce():
    nums = [2, 5, 3, 4, 7, 3, 4, 2, 5, 0]
    ret = findTwoNumAppearOnce(nums)

    print(ret)

# test_findTwoNumAppearOnce()

#######################################
# 56-2 数组中唯一出现一次的数字
# LC-137
def findNum(nums):
    """数组中除了一个数字出现一次之外，其余数字都出现三次"""
    pass

#######################################
# 57-1 和为S的数字
# LC-01
def findPairWithSum(nums, s):
    """双指针和哈希"""
    pass

#######################################
# 57-2 和为S的连续正数序列
def findSequenceWithSum(nums, s):
    curSum = 0
    preIndex = 0
    ret = []
    for i in range(len(nums)):
        curSum += nums[i]
        while curSum > s and preIndex <= i:
            curSum -= nums[preIndex]
            preIndex += 1
        if curSum == s:
            tmp = []
            for j in range(preIndex, i+1):
                tmp.append(nums[j])
            ret.append(tmp)

    return ret 

def test_findSequenceWithSum():
    nums = [1,2,3,4,5,6,7,8,9,10]
    k = 15

    ret = findSequenceWithSum(nums, k)
    print(ret)

# test_findSequenceWithSum()
#######################################
# 58-1 翻转字符串
def reverseSentence(s):
    """i am a student. -> student. a am i"""
    s = s[::-1]
    sNums = s.split(' ')
    for i in range(len(sNums)):
        sNums[i] = sNums[i][::-1]

    return " ".join(sNums)

def test_reverseSentence():
    s = "i am a student."

    ret = reverseSentence(s)
    print(ret)

# test_reverseSentence()

#######################################
# 58-2 左旋转字符串
def leftRotateString(s, n):
    """将s中的前n个移到后面"""
    pass

#######################################
# 59 滑动窗口的最大值
# LC-239
def maxValueInSliceWindow(nums, windowSize):
    window = []
    curWindowSize = 0
    ret = []
    for i, n in enumerate(nums):
        while window and nums[window[-1]] < n:
            window.pop()

        window.append(i)
        curWindowSize += 1
            
        if i - window[0] == windowSize:
            window.pop(0)
        
        ret.append(nums[window[0]])

    return ret[windowSize-1:]

def test_maxValueInSliceWindow():
    nums = [2,3,4,2,6,2,5,1]
    windowSize = 3

    ret = maxValueInSliceWindow(nums, windowSize)
    print(ret)

# test_maxValueInSliceWindow()

#######################################
# 60 n个骰子的点数
def probilityOfValue(n):
    """把n个骰子扔地上，朝上一面点数之和为s，打印出s的所有可能的值出现的概率"""
    def helper(n):
        for i in range(1, maxValue+1):
            countPro(n, i)

    def countPro(count, sum):
        if count == 1:
            pro[sum - maxValue] += 1
        else:
            for i in range(1, maxValue+1):
                countPro(count-1, sum+i)

    maxValue = 6
    pro = [0 for _ in range(maxValue*n - 6 + 1)]
    helper(n)

    total = maxValue**n 
    for i in range(len(pro)):
        pro[i] /= total

    return pro 

def test_probilityOfValue():
    n = 6
    ret = probilityOfValue(n)
    print("ret: {} \nverify sum(pro): {}".format(ret, sum(ret)))

# test_probilityOfValue()
#######################################
# 61 扑克牌中的顺序
def isContinuous(nums):
    """从扑克排中随机抽取5张，判断是不是一个顺子"""
    pass
################# 2020-5-24 ######################
# 62 圆圈中最后剩下的数字
def lastRemaining(n, m):
    """0~n-1数字排成一个圆圈，从数字0开始，每次从圆圈中删除第m个数字，求出最后剩下的数字"""
    nums = [x for x in range(n)]
    preIndex = 0
    while len(nums) > 1:
        curIndex = preIndex
        curLength = len(nums)
        for i in range(m-1):
            curIndex += 1
            if curIndex > curLength - 1:
                curIndex = curIndex - curLength
        nums.pop(curIndex)
        preIndex = curIndex

    return nums[0]

def test_lastRemaining():
    n, m = 5, 3
    ret = lastRemaining(n, m)
    print(ret)

# test_lastRemaining()
#######################################
# LC-236 树中两个节点的最低公共祖先
def lowestCommonAncestor(root, p, q):
    if root == p or root == q or not root:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if right and left:
        return root 

    return [right, left][right == None]

def test_lowestCommonAncestor():
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

    ret = lowestCommonAncestor(node_10, node_4, node_12)
    print(ret.val)

# test_lowestCommonAncestor()

################ LeetCode #######################
# LC-139 word break
def wordBreak(s, wordDict) -> bool:
    """"s = "leetcode", wordDict = ["leet", "code"], 判断s是否能由wordDict中的字符串组成"""
    sLength = len(s)
    if sLength == 0:
        return False
    stack = [0]
    while stack:
        preIndex = stack.pop()
        for string in wordDict:
            curStringLength = len(string)
            curIndex = preIndex + curStringLength
            if s[preIndex:curIndex] == string:
                if curIndex == sLength:
                    return True 
                stack.append(curIndex)

    return False

def test_wordBreak():
    s = "leetcode"
    wordDict = ["leet", "code"]

    ret = wordBreak(s, wordDict)
    print(ret)

# test_wordBreak()

#######################################
# 当当-1
# 阿拉伯数字转为中文大小写
# 11011 -> 壹万壹仟零壹拾壹元整
def arabic2Chinese(num):
    pass

def convert(n):
    units = ['', '万', '亿']
    nums = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
    decimal_label = ['角', '分']
    small_int_label = ['', '拾', '佰', '仟']
    int_part, decimal_part = str(int(n)), str(n - int(n))[2:]  # 分离整数和小数部分

    res = []
    if decimal_part:
        res.append(''.join([nums[int(x)] + y for x, y in zip(decimal_part, decimal_label) if x != '0']))

    if int_part != '0':
        res.append('圆')
        while int_part:
            small_int_part, int_part = int_part[-4:], int_part[:-4]
            tmp = ''.join([nums[int(x)] + (y if x != '0' else '') for x, y in list(zip(small_int_part[::-1], small_int_label))[::-1]])
            print(tmp, list(zip(small_int_part[::-1], small_int_label)))
            tmp = tmp.rstrip('零').replace('零零零', '零').replace('零零', '零')
            unit = units.pop(0)
            if tmp:
                tmp += unit
                res.append(tmp)
    return ''.join(res[::-1])

def test_arabic2Chinese():
    num = 1011011
    ret = convert(num)
    print(ret)

# test_arabic2Chinese()

#######################################
# 携程-2
def reverseExpr(s):
    """
    表达式中括号表示将里面的字符串翻转
    输入
    一行字符串

    输出
    一行字符串
    如果表达式括号不匹配，输出空字符串
    样例输入
    ((ur)oi)
    样例输出
    iour
    """
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            curString = ""
            while stack[-1] != '(':
                curString = stack.pop() + curString
            stack[-1] = curString[::-1]
        else:
            if stack[-1] == '(':
                stack.append('')
            stack[-1] = stack[-1] + c 
        print(stack)
    return stack[-1]

def test_reverseExpr():
    s = "((ur)oi(ab))"
    ret = reverseExpr(s)
    print(ret)

# test_reverseExpr()

#######################################
# 爱奇艺-2

#######################################
# 猿辅导-1
def decodeString(s):
    """ 
    "((A2B)2)2G2" -> 'AABAABAABAABGG'
    """
    stack = []
    digit = 0
    for c in s:
        if c.isdigit():
            digit = 10*digit + int(c)
            continue
        if digit != 0:
            stack[-1] = stack[-1]*digit
            digit = 0
        if c == ')':
            curString = ""
            while stack[-1] != '(':
                curString = stack.pop() + curString
            stack[-1] = curString
        elif c == '(':
            stack.append(c)
        else:
            stack.append(c)
    if digit != 0:
        stack[-1] = stack[-1]*digit
    return "".join(stack)

def test_decodeString():
    sNums = [        
        "A11B",
        "(AA)2A",
        "((A2B)2)2G",
        "(YUANFUDAO)2JIAYOU",
        "A2BC4D2"
    ]

    ans = [
        'AAAAAAAAAAAB',
        'AAAAA',
        'AABAABAABAABG',
        'YUANFUDAOYUANFUDAOJIAYOU',
        'AABCCCCDD'
    ]
    for i,s in enumerate(sNums):
        ret = decodeString(s)
        print(ret == ans[i])

# test_decodeString()

#######################################
# 途家-1
"""
法师住在喜马拉雅上脚下的一个村庄，突然一天，发生大雪崩，很快村庄就要被掩埋，所有人将会遇难。
法师的跑步的速度为13m/s,以这样的速度，是无法逃离雪崩的。但是，法师有闪跳技能，可在1s内移动50m,每次使用技能后，会消耗10点魔法值。魔法值的恢复速度为4点/s,只有在原地休息状态时才能够恢复。
现已知法师初始值为M,所在位置与安全区域的距离为S,雪崩到达村庄的时间为T。
编写一个程序，计算法师如何在最短的时间内到达安全区域，如不能够逃脱，输出法师在时间内走的最远距离。

输入
输入一行，包括空格隔开的三个非负整数M，S，T。

输出
输出两行:
第1行为字符串"Yes"或"No" (区分大小写)，即守望者是否能逃离荒岛。
第2行包含一个整数，第一行为"Yes" (区分大小写）时表示守望着逃离荒岛的最短时间
第一行为"No" (区分大小写) 时表示守望者能走的最远距离。

样例输入
36 255 10
样例输出
Yes
10
"""
def runFast(m, s, t):
    curM = m
    retDist = 0
    mDist = 0
    for i in range(1, t+1):
        retDist += 13
        if curM >= 10:
            mDist += 50
            curM -= 10
        else:
            curM += 4
        retDist = max(retDist, mDist)
        if retDist >= s:
            return "YES", i

    return "NO", retDist

def test_runFast():
    m, s, t = 36, 255, 10
    ret = runFast(m, s, t)

    print(ret)

# test_runFast()

################# 2020-5-25 ######################
# LC-5 字符串中最长的回文串
def longestPalindrome(s):
    maxLength, startIndex = 0, 0
    sLength = len(s)

    for i in range(sLength):
        if i - maxLength >= 0 and s[i-maxLength:i+1] == s[i-maxLength:i+1][::-1]:
            startIndex = i - maxLength
            maxLength += 1
        if i - maxLength >= 1 and s[i-maxLength-1:i+1] == s[i-maxLength-1:i+1][::-1]:
            startIndex = i - maxLength - 1
            maxLength += 2

    return s[startIndex: startIndex+maxLength]

def test_longestPalindrome():
    s = "ccabcbaewdf"
    ret = longestPalindrome(s)
    print(ret)

# test_longestPalindrome()

#######################################
# LC-6 ZigZag convert
#######################################
# LC-10 正则表达式匹配
# 剑指offer-19
def isMatch(s, p):
    if p == "":
        return s == ""
    if len(p) > 1 and p[1] == "*":
        return isMatch(s, p[2:]) or (s and (s[0] == p[0] or p[0] == '.') and isMatch(s[1:], p))
    else:
        return s and (s[0] == p[0] or p[0] == '.') and isMatch(s[1:], p[1:])

def test_isMatch():
    s = "ab"
    p = ".*c"
    ret = isMatch(s, p)
    if ret:
        print('True')
    else:
        print('False')

# test_isMatch()

#######################################
# LC-12 Integer to Roman
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
