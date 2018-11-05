# 一些笔记

# ##
# reduce()
# reduce()函数也是Python内置的一个高阶函数。
# reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
# 例如，编写一个f函数，接收x和y，返回x和y的和：
# def f(x, y):
#     return x + y
# 调用 reduce(f, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：
# 先计算头两个元素：f(1, 3)，结果为4；
# 再把结果和第3个元素计算：f(4, 5)，结果为9；
# 再把结果和第4个元素计算：f(9, 7)，结果为16；
# 再把结果和第5个元素计算：f(16, 9)，结果为25；
# 由于没有更多的元素了，计算结束，返回结果25。

##
cmp(x, y)
cmp(x,y) # 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。


## 
# heappush heappop
heap = [] #创建了一个空堆 
heappush(heap,item) #往堆中插入一条新的值 
item = heappop(heap) #从堆中弹出最小值 
item = heap[0] #查看堆中最小值，不弹出 


## 
from queue import PriorityQueue
import time
q = PriorityQueue()

# 自定义函数判断谁是最小值
# class Comp:                  # 可比较对象，放入优先队列中
#     def __init__(self, priority, description):
#         self.priority = priority
#         self.description = description
#         return 

#     def __cmp__(self, other):         # 比较规则的指定，谁做根（大顶堆，小顶堆）
#                                       # 返回的是布尔类型
#         if self.priority >= other.priority:
#             return True
#         else:
#             return False

# q.put(Comp(1, 'code'))
# leetCode 23
q.put((1, 'code'))
q.put((1, 'eat'))
q.put((1, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)
    time.sleep(1)


##
setdefault()
dic = dict()
dic = dic.setdefault(key, default=None) # 如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。

# 例子
word = "bad"
node = {}
for char in word:
    node = node.setdefault(char, {})
node['#'] = None
# {'b': {'a': {'d': {#: None}}}}


##
any(iterable)
# 参数 iterable -- 元组或列表。
# 如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。

##
dict.values() # 返回字典中所有值
radiansdict.clear() # 删除字典内所有元素
radiansdict.copy() # 返回一个字典的浅复制
radiansdict.fromkeys() # 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None) # 返回指定键的值，如果值不在字典中返回default值
key in dict # 如果键在字典dict里返回true，否则返回false
radiansdict.items() # 以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys() # 返回一个迭代器，可以使用 list() 来转换为列表
radiansdict.setdefault(key, default=None) # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2) # 把字典dict2的键/值对更新到dict里
radiansdict.values() # 返回一个迭代器，可以使用 list() 来转换为列表
pop(key[,default]) # 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem()



## 
filter
dummy = filter(function, iterable) # 根据 function的返回值过滤掉 iterable中的数据, 最终结果返回给dummy



# os
print(os.path.dirname(__file__)) # 打印出当前工作路径


np.sum(mat, axis=1) # 按列相加
np.sum(mat, axis=0) # 按行相加

# 关于sum, repeat函数的用法
weight = np.mat(np.ones((3, 2)))
print(weight)
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]
weight = weight.sum(axis=1)
print(weight)
# [[2.]
#  [2.]
#  [2.]]
weight = weight.repeat(3, axis=1)
print(weight)
# [[2. 2. 2.]
#  [2. 2. 2.]
#  [2. 2. 2.]]



#####################
import collections
queue = collections.deque()
queue.append(1)
queue.popleft()
queue.pop()
