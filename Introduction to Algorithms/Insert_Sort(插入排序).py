# 2018-7-31
# 插入排序 insert sort
# 第i次循环之后，前i+1项已经排序
# 升序
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