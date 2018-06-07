# 2018-6-7
# 搜索最小值，顺序搜索一个表，有序列表二叉树(+递归)


# lists = [3,5,6,8,29,345,2,44,9]


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

# 有序列表二叉树
