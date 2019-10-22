# coding:utf-8
"""
给定n个进程，这些进程满足以下条件：

（1）每个进程有唯一的PID，其中PID为进程ID

（2）每个进程最多只有一个父进程，但可能有多个子进程，用PPID表示父进程ID

（3）若一个进程没有父进程，则其PPID为0

（4）PID、PPID都是无符号整数

结束进程树的含义是当结束一个进程时，它的所有子进程也会被结束，包括子进程的子进程。


现在给定大小为n的两组输入列表A和B（1 <= n <= 100），列表A表示进程的PID列表，列表B表示列表A对应的父进程的列表，即PPID列表。

若再给定一个PID，请输出结束该PID的进程树时总共结束的进程数量。

输入
3 1 5 21 10

0 3 3 1 5

5

输出
2


样例输入
3 1 5 21 10
0 3 3 1 5
3

样例输出
5
"""
class Node(object):
	def __init__(self, ppid):
		self.ppid = ppid 
		self.child = []

def solver(pidNums, ppidNums):
	nums =  []
	for p in set(ppidNums):
		nums.append(Node(p))

	for p




