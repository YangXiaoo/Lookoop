# 2018-6-7
# 快速排序，合并排序
# 说明：
# 1. 找到基准点
# 2. 将基准点与最后一项交换
# 3. 在第一项之前建立一个边界
# 4. 扫描小于基准点的第一项
# 5. 找到后将这一项与边界后面的项交换
# 6. 交换边界与后一项
# 7. 重复4到6步骤，直到没有找到小于基准点的项
# 8. 将边界后面一项与列表最后一项交换位置，执行7——8步，直到子表的长度最大为1

def swap(lists, i, j):
    tmp = lists[i]
    lists[i] = lists[j]
    lists[j] = tmp

# 找到基准点，并与最后一项排序
def findPivot(lists, left, right):
    # 找到基准并与最后一项交换顺序
    middle = (left + right) // 2
    pivot = lists[middle]
    lists[middle] = lists[right]
    lists[right] = pivot

    # 设置边界
    boundary = left
    for index in range(left, right):
        if lists[index] < pivot:
            swap(lists, index, boundary)
            boundary += 1
    swap(lists, right, boundary) 

    return  boundary

def quickSort(lists):
    n = 0
    m = 0
    quicksortHelper(lists, 0, len(lists) - 1, n, m)
    return lists

def quicksortHelper(lists, left, right, n, m):
    n += 1
    m += 1
    if left < right:
        pivot_location = findPivot(lists, left, right)
        quicksortHelper(lists, left, pivot_location - 1, n, m)
        print ("on %s" % n)
        quicksortHelper(lists, pivot_location + 1, right, n, m)
        print ("to %s" % m)

def main():
    lists = [5,2,1,4,3,9,6,7]
    li = quickSort(lists)
    print(li)

if __name__ == "__main__":
    main()


