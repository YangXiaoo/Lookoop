# coding:utf-8
# 复习记录
# 不使用程序入口方式执行，方便单个验证

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right
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
# 15-二进制中1的个数
def countBit01(n):
    """左移，防止负数右移时出错"""
    count = 0
    flag = 1
    for i in range(32):
        if n & flag:
            count += 1
        flag <<= 1

    return count

def countBit02(n):
    """n & (n - 1)
    1100 & 1011 -> 1000 少一个1
    """
    count = 0
    while n:
        count += 1
        n = n & (n -1)

    return count

def test_countBit():
    nums = [1, 2, 22, 33, 9, 32]
    for n in nums:
        ret1 = countBit01(n)
        ret2 = countBit02(n)

        print("ret1: {}, ret2: {}".format(ret1, ret2))

#######################################
# 16-数值的整数次方
def power(base, exponent):
    """考虑0情况，并考虑exponent正负号"""
    pass

#######################################
# 31-栈的压入弹出顺序
def isPopOrder(push, pop):
    record = []
    index = 0
    pushIndex = 0
    ret = True
    while index < len(pop):
        while len(record) == 0 or record[-1] != pop[index]:
            record.append(push[pushIndex])
            pushIndex += 1

        # print(record)
        if record[-1] != pop[index]:
            ret = False
            break

        record.pop()
        index += 1

    return ret

def test_isPopOrder():
    push = [1,2,3,4,5]
    pop = [4,5,3,2,1]

    ret = isPopOrder(push, pop)
    print("ret: {}".format(ret))
#######################################
# 33-二叉搜索树的后续遍历
# 2019-7-14
def verifyBST(seq):
    """判断数组是不是二叉搜索树的后续遍历结果
    [5, 7, 6, 9, 11, 10, 8]
    最右边的肯定为根节点，左边比根节点小的为左树反之为右树
    """
    if len(seq) == 0:
        return True

    rootValue = seq[-1]
    # 左子树
    rightSeqIndex = 0
    for i in range(len(seq)):
        if seq[i] > rootValue:
            rightSeqIndex = i 
            break

    # 验证右子树
    # print(seq[rightSeqIndex:-1])
    for v in seq[rightSeqIndex:-1]:
        if v < rootValue:
            return False

    # 左子树递归验证
    leftRet = True
    if rightSeqIndex > 0:
        leftRet = verifyBST(seq[:rightSeqIndex])

    # 右子树递归验证
    rightRet = True
    if rightSeqIndex < len(seq) - 1:
        rightRet = verifyBST(seq[rightSeqIndex:-1])

    return leftRet and rightRet

def test_verifyBST():
    # seq = [5, 7, 6, 9, 11, 10, 8]
    seq = [7, 4, 6, 5]
    print(verifyBST(seq))

# test_verifyBST()
#######################################
# 34-二叉树中和为某一直的路径,打印出路径
def pathSum(root, sums):
    """使用dfs"""
    def _helper(root, tmp):
        if root.left == None and root.right == None:
            tmp.append(root.val)
            if sum(tmp) == sums:
                seq.append(tmp[:])
            tmp.pop()
        else:
            tmp.append(root.val)
            _helper(root.left, tmp)
            _helper(root.right, tmp)
            tmp.pop()

    seq = []    # 记录路径
    _helper(root, [])

    return seq

def test_pathSum():
    root = getTree()
    print(pathSum(root, 22))    # [[10, 5, 7], [10, 12]]

# test_pathSum()
#######################################
# 35-复杂链表的复制
def copyLinkedList(linkedList):
    copyNode(linkedList)            # 复制节点与随机节点
    moveRandomNode(linkedList)      # 将复制节点的随机节点链接到对应的复制节点
    copylist = splitNode(linkedList)# 将复制节点与原节点分离

    return copylist
#######################################
# 36- 二叉搜索树与双向链表
def convertBSTToLinkedList(root):
    def _helper(node):
        nonlocal pre    # 闭包变量作用域
        if not node:
            return

        curNode = node
        if curNode.left:
            # print(curNode.left.val)
            _helper(curNode.left)
        
        curNode.left = pre
        if pre:
            pre.right = curNode

        pre = curNode
        if curNode.right:
            _helper(curNode.right)
    pre = None
    _helper(root)
    # print(pre)

    while pre != None and pre.left != None:
        pre = pre.left

    return pre 

def test_convertBSTToLinkedList():
    root = getTree()
    head = convertBSTToLinkedList(root)
    while head != None:
        print(head.val, end=" ")
        head = head.right   # 4 5 7 10 12


# test_convertBSTToLinkedList()

#######################################
# 37-序列化二叉树
def serialize(root):
    pass

def deSerialize(serializeList):
    pass
#######################################
# 38-字符串的排序
def stringSeq(string):
    """"abc依次交换第i个位置与后面的值, i -> [0, len(string)]
    """
    pass

#######################################
# 39-数组中次数超过一半的数字
def halfNumber(nums):
    """相同则加1，不相同则减1，最后表示的数一定超过一半"""
    numberCount, number = 1, nums[0]
    for n in nums[1:]:
        if number == n:
            numberCount += 1
        else:
            if numberCount > 1:
                numberCount -= 1
            else:
                number = n

    return number

def test_halfNumer():
    nums = [1, 2, 3, 2, 2,2,5,4,2]
    print(halfNumber(nums))

# test_halfNumer()
#######################################
# 40-最小的K个数
def minKNumber_01(nums, k):
    """使用堆或红黑树"""
    from queue import PriorityQueue

    queue = PriorityQueue()
    for n in nums:
        queue.put(tuple([n, n]))
    ret  = []
    for i in range(k):
        ret.append(queue.get()[-1])

    return ret 

def minKNumber_02(nums, k):
    """使用快排思想"""
    def _helper(nums, left, right):
        mid = (right - left) >> 1
        flagNumber = nums[mid]
        nums[mid], nums[right] = nums[right], nums[mid]

        for i in range(left, right):
            if nums[i] <= flagNumber:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        nums[left], nums[right] = nums[right], nums[left]

        return left

    left, right = 0, len(nums) - 1
    boundary = _helper(nums, left, right)
    it = 0
    while boundary != k:
        excursion = (len(nums) - right) >> 1
        # print(excursion, boundary, nums)
        if k > boundary:
            right += excursion
            boundary = _helper(nums, left, right)
        elif k < boundary:
            right -= excursion
            boundary = _helper(nums, left, right)

        it += 1
        if it > len(nums)**2:
            break

    return nums[:k]
            
def test_minKNumber():
    nums = [2,4,5,6,7,43,21,1,43,65,7]
    print(minKNumber_02(nums, 3))

# test_minKNumber()
#######################################
# 41-数据流的中位数
def medianNumber(nums):
    """最小堆与最大堆组合"""
    pass
#######################################
# 42-连续子数组的最大和
"""最长递增数组"""
#######################################
# 48-最长不包含重复字符的子字符串
def longestSubSeq(string):
    pass
#######################################
# 49-丑数
def uglyNumber(n):
    """求从小到大顺序排列的第n个丑数
    以空间换时间，时间复杂度O(n)
    """
    ugly2, ugly3, ugly5 = 0, 0, 0
    uglyNums = [0 for _ in range(n)]
    uglyNums[0] = 1 # 第一个丑数
    for i in range(n)[1:]:
        nextUgly = min(uglyNums[ugly2]*2, uglyNums[ugly3]*3, uglyNums[ugly5]*5)
        # print(nextUgly)
        uglyNums[i] = nextUgly
        while uglyNums[ugly2]*2 <= nextUgly:
            ugly2 += 1
        while uglyNums[ugly3]*3 <= nextUgly:
            ugly3 += 1      
        while uglyNums[ugly5]*5 <= nextUgly:
            ugly5 += 1
    # print("-"*30)
    return uglyNums[-1]

def test_uglyNumber():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for n in nums:
        ret = uglyNumber(n)
        print("ret: {}".format(ret))

#######################################
# 51-数组中的逆序对
def inversePair(nums):
    """[7, 5, 6, 4]
    逆序对： [7,5], [6,4], [7,6], [7,4], [5, 4]
    """
    def _helper(nums, seq):
        if len(nums) == 1:
            return nums
        mid = len(nums) >> 1
        left = _helper(nums[:mid], seq)
        right = _helper(nums[mid:], seq)
        ret = []
        
        while len(left) != 0 and len(right) != 0:
            if left[-1] > right[-1]:
                ret.append(left[-1])
                tmp = [left[-1], right[-1]]
                left.pop()
                seq.append(tmp)
            else:
                ret.append(right[-1])
                right.pop()

        ret += left
        ret += right

        return ret

    seq = []
    _helper(nums, seq)

    return seq
def test_inversePair():
    nums = [7, 5, 6, 4]
    print(inversePair(nums))    # [[7, 5], [6, 4], [5, 4], [7, 4]]

# test_inversePair()
#######################################
# 55-03-二叉树的最小深度[leetcode-111]
def minDepthOfBT(root):
    pass 

# 55-02-平衡二叉树
def balanceBT(root):
    if not root:
        return True

    if abs(depth(root.left)-depth(root.right)) > 1:
        return False

    return balanceBT(root.left) and balanceBT(root.right)

def depth(root):
    if not root:
        return 0

    return max(depth(root.left), depth(root.right)) + 1

#######################################
# 60-n个骰子的点数
def probability(n):
    def _helper(n, pro):
        """计算每一种可能"""
        for i in range(1, maxValue + 1):
            countPro(n, n, i, pro)

    def countPro(orig, cur, sums, pro):
        """计算概率
        @param orig 基数
        @param cur 当前骰子数
        @param sums 骰子和
        @param pro 概率
        """
        if cur == 1:
            pro[sums - orig] += 1
        else:
            for i in range(1, maxValue + 1):
                countPro(orig, cur - 1, i + sums, pro)

    maxValue = 6
    pro = [0 for _ in range(maxValue * 6 - 6 + 1)]
    _helper(n, pro)

    total = maxValue**n 
    for i in range(len(pro)):
        pro[i] /= total

    return pro

def test_probability():
    n = 6
    ret = probability(n)
    print("ret: {} \nverify sum(pro): {}".format(ret, sum(ret)))

#######################################
# 62-圆圈中最后剩下的数字
def lastNumber(n, m):
    """每次从n个数中删除第m个数字"""
    nums = [i for i in range(n)]
    preIndex = 0
    while len(nums) > 1:
        curIndex = preIndex
        curLength = len(nums)
        for i in range(m-1):
            curIndex += 1
            if curIndex > curLength - 1:
                curIndex = curIndex - curLength

        print("cur nums: {}, delete num: {}, delete index: {}, preIndex: {}".format(nums, nums[curIndex], curIndex, preIndex))
        nums.pop(curIndex)
        preIndex  = curIndex

    return nums[0]

def test_lastNumber():
    n, m = 5, 2
    ret = lastNumber(n, m)
    print("ret: {}".format(ret))

#######################################
# 64-求1+2+...+n
"""不使用乘除法以及for,while,if, else, switch,case,条件判断"""
"""java 
    
    //方法一：利用库函数+位运算
    public int sumN01(int n) {
        int sum = (int)(Math.pow(n, 2)+n) >> 1;

        return sum;
    }

    //方法二：利用 && 运算符实现短路结束递归条件
    public int sumN02(int n) {
        int sums = n;
        boolean dummy = (n > 0) && (sums = sums + sumN02(n-1) > 0);

        return sums;
    }
"""
########################################
# 65-不用加减乘除做加法
def add(num1, num2):
    while True:
        sums = num1 ^ num2
        carry = (num1 & num2) << 1
        print("sums: {}, carry: {}, bin(num1): {}, bin(num2): {}".format(sums, carry, bin(num1), bin(num2)))
        num1 = sums
        num2 = carry

        if num2 == 0:
            break
    return num1

def test_add():
    num1, num2 = 98, 99
    ret = add(num1, num2)
    print("ret: {}".format(ret))
########################################
# 29-Divide Two Integers
def divide(dividend, divisor):
    # 判断符号 pass
    ret = 0
    it = 0
    while dividend >= divisor:
        tmp = divisor
        k = 0
        while dividend >= tmp:
            dividend -= tmp
            ret += 1 << k
            tmp <<= 1
            k += 1
            
    return ret 

def test_divide():
    dividend = 16
    divisor = 2
    ret = divide(dividend, divisor)
    print(ret)

# test_divide()
########################################
# 32-最长有效括号
def longestValidParentheses(s):
    stack = [0]
    maxLens = 0
    for c in s:
        if c == '(':
            stack.append(0)
        else:
            if len(stack) > 1:
                last = stack.pop() + 2
                stack[-1] += last
                maxLens = max(maxLens, stack[-1])
            else:
                stack = [0]

    return maxLens

def test_longestValidParentheses():
    s = "())))((())(())()(("
    ret = longestValidParentheses(s)
    print(ret)

# test_longestValidParentheses()
########################################
# 37-sudoku solver
def solveSudoku(board):
    def _helper(board, unfilled, i, found):
        if i == len(unfilled):
            found[0] = True

        r, c = unfilled[i]
        for x in range(1, 10):
            board[r][c] = str(x)
            if isValid(board):
                _helper(board, unfilled, i + 1, found)
            if not found[0]:
                board[r][c] = '.'
            else:
                break

    unfilled = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                unfilled.append((i, j))

    found = [False]
    _helper(board, unfilled, 0, found)

    return board

########################################
# 39-combination sum
def combinationSum(candidates, target):
    def _dfs(tmp, i):
        nonlocal ret, candidates, target
        if sum(tmp) == target:
            ret.append(tmp[:])
            return 

        for j in range(i, len(candidates)):
            if sum(tmp) + candidates[j] <= target:
                tmp.append(candidates[j])
                _dfs(tmp, j)
                tmp.pop()
    ret = []
    _dfs([], 0)

    return ret 

def test_combinationSum():
    candidates = [2,3,5]
    target = 8
    ret = combinationSum(candidates, target)
    print(ret)  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# test_combinationSum()
########################################
# 45-jump game II
# 贪心思想
def jumpGame(nums):
    ret = 0
    pre = 0
    last = 0
    for i in range(len(nums)):
        print("pre: {}".format(pre))
        if i > pre:
            pre = last
            ret += 1
        last = max(last, i + nums[i])
        
    return ret

def test_jumpGame():
    nums = [2,3,1,1,4]
    ret = jumpGame(nums)
    print(ret)

# test_jumpGame()
########################################
# 50-Pow(x.n)
def pow(x, n):
    """使用递归
    折半进行
    """
    if n < 0:
        x  = 1 / x
        n = -n
    if n == 0: return 1
    if n == 1: return x

    ret = pow(x, n >> 1)
    if n % 2 == 0:
        return ret * ret 
    else:
        return ret * ret * x

def test_pow():
    x, n = 2.0, 10
    ret = pow(x, n)
    print(ret)

# test_pow()
########################################
# 55-jump game
def jump(nums):
    """判断是否能跳到最后位置
    [2,3,1,1,4]
    """
    counter = 1
    for i in range(len(nums)):
        if counter < 1:
            return False
        counter = max(counter - 1, nums[i])

    return True
########################################
def inputPara(default=10):
    print("default val: {}".format(default))

# inputPara(20)
# inputPara()