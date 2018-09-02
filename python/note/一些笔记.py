# 一些笔记

\  reduce()
reduce()函数也是Python内置的一个高阶函数。
reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
例如，编写一个f函数，接收x和y，返回x和y的和：
def f(x, y):
    return x + y
调用 reduce(f, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：
先计算头两个元素：f(1, 3)，结果为4；
再把结果和第3个元素计算：f(4, 5)，结果为9；
再把结果和第4个元素计算：f(9, 7)，结果为16；
再把结果和第5个元素计算：f(16, 9)，结果为25；
由于没有更多的元素了，计算结束，返回结果25。

\  cmp(x, y)
cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。


\heappush heappop
heap = [] #创建了一个空堆 
heappush(heap,item) #往堆中插入一条新的值 
item = heappop(heap) #从堆中弹出最小值 
item = heap[0] #查看堆中最小值，不弹出 


\ from queue import PriorityQueue
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

q.put((1, 'code'))
q.put((1, 'eat'))
q.put((1, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)
    time.sleep(1)