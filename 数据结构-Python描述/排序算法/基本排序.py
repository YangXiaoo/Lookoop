# 2018-6-7
# 选择排序，冒泡排序，插入排序

# 交换函数
def swap(lists, i, j):
    tmp = lists[i]
    lists[i] = lists[j]
    lists[j] = tmp  

# 选择排序
# 升序
# 每一次循环将最小的排在最上面，下一轮循环将索引加1
def selectSort(lists):
    i = 0
    leng = len(lists) - 1
    while i < leng: 
        j = i + 1
        while j < leng + 1:
            if lists[j] < lists[i]: # lists[j] > lists[i]  降序
                swap(lists,i,j)
            j += 1
        i += 1
    return lists

# 冒泡排序
# 升序
# 每次循环都从0位置开始到i，i每次循环-1
def bubbleSort(lists):
    i = 0
    leng = len(lists) - 1
    while i < leng:
        j = 0
        while j < leng - i:
            if lists[j] > lists[j + 1]:
                swap(lists, j, j+1)
            j += 1
        i += 1
    return lists

# 插入排序 insert sort
# 第i次循环之后，前i+1项已经排序
# 降序
# [5,2,1,4,3] -> [5,5,1,4,3] -> [2,5,1,4,3]
# [2,5,1,4,3] -> [2,5,5,4,3] -> [2,2,5,4,3] -> [1,2,5,4,3]
# [1,2,5,4,3] -> [1,2,5,5,3] -> [1,2,4,5,3]
# [1,2,4,5,3] -> [1,2,4,5,5] -> [1,2,4,4,5] -> [1,2,3,4,5]
def insertSort(lists):
    leng = len(lists)
    i = 1
    while i < leng:
        current_item = lists[i]
        j = i - 1
        while j >= 0:
            if current_item < lists[j]:
                lists[j + 1] = lists[j]
                j -= 1
            else:
                break
        lists[j + 1] = current_item
        i += 1
    return lists


# test
lists = [3,5,6,8,29,345,2,44,9,333,890,1]

s_s_re = selectSort(lists)
print(s_s_re)

b_s_re = bubbleSort(lists)
print (b_s_re)

i_s_re = insertSort(lists)
print (i_s_re)
