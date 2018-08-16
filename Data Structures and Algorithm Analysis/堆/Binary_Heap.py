# 2018-8-5
# Binary_Heap.py

# Reference
# Introduction to Algorithms [P84]
# Data Structures and Algorithm Analysis in C [P133]
# http://python.jobbole.com/85338/

class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def swap(self, k1, k2):
        tmp = k1
        k1 = k2
        k2 = tmp


    def insert(self, value):
        self.heapList.append(value)
        self.size += 1
        self.Up(self.size)

    def Up(self, k):
        while k // 2 > 0:
            if self.heapList[k] < self.heapList[k // 2]:
                self.swap(self.heapList[k], self.heapList[k // 2])
            k = k // 2

    def delMin(self):
        res = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]

        self.size -= 1
        self.heapList.pop()
        self.Down(1)

        return res

    def Down(self, k):
        while (k * 2) < self.size:
            minc = self.minChild(k)
            if self.heapList[k] > self.heapList[minc]:
                self.swap(self.heapList[k], self.heapList[minc])
            k = minc

    def minChild(self, k):
        if (k * 2 + 1) > self.size:
            return k * 2
        else:
            if self.heapList[k * 2] > self.heapList[k * 2 + 1]:
                return k * 2 + 1
            else:
                return k * 2

    """
    # Delete Min by percloate down
    def delMin(self):
        m = self.heapList[1]
        self.percolateDown(1)
        self.size -= 1
        self.heapList.pop()

        return m

    def percolateDown(self, k):
        m = k   # gloable variable
        while (k * 2) < self.size:
            m = self.minChild(k)
            self.swap(self.heapList[k], self.heapList[m])

        self.heapList[m] = self.heapList[-1]

    """



