# 2018-6-7
# 归并排序
# https://www.cnblogs.com/Lin-Yi/p/7309143.html
# 1. 从中间分为两部分
# 2. 将分开的每个数据再一分为二直到不能分
# 3. 组合

def merge_sort(lists):
    if len(lists) == 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right =merge_sort(lists[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append( left.pop(0) )
        else:
            result.append( right.pop(0) )
    result += left
    result += right
    return result

if __name__ == '__main__':
    lists = [5, 4, 3, 2, 1, 9, 7, 8, 6]
    li = merge_sort(lists)
    print(li)

