# 2018-6-7
# 搜索最小值，顺序搜索一个表，有序列表二叉树搜索(+递归)


# 搜索最小值
def searchMin(lists):
    min_index = 0
    cur_index = 1
    while cur_index < len(lists):
        if lists[cur_index] < lists[min_index]:
            min_index = cur_index
        cur_index += 1
    return lists[min_index]

# 顺序搜索一个表
def seqSearch(target, lists):
    position = 0
    while position < len(lists):
        if target == lists[position]:
            return position
        position += 1
    return -1

# 有序列表二叉树搜索
def binarySearch(target, lists):
    left = 0
    right = len(lists) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == lists[middle]:
            return middle
        elif target < lists[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1



# 有序二叉树递归搜索
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper] 
        return upper
    else: 
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

lists = [3,5,6,8,29,45,46,47,50]
t = search(lists,6)
print(t)