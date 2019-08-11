def solver(L, N, nums):
    """长度为L， N颗珍珠"""
    minDist = len(nums)*L
    for i, n in enumerate(range(L)):
        curDist = getDist(i, L, nums)
        minDist = min(minDist, curDist)
        
        print(curDist)
        if i == 0:
            break

    return minDist

def getDist(i, L, nums):
    dist = 0
    half = L >> 2
    left = [-1 for _ in range(len(nums))]
    right = [-1 for _ in range(len(nums))]
    for j, n in enumerate(nums):
        r = n - i 
        l = L - 1 - n 
        if l < r:
            left[j] = l 
        else:
            right[j] = r
    print(left, right)
    count = 0
    for j,n in enumerate(right):
        if n != -1:
            dist += n - count
            count += 1
    count = 0
    for j,n in enumerate(left[::-1]):
        if n != -1:
            dist += n - count
            count += 1

    return dist

def test():
    L, N, nums = 1000, 4, [1, 4, 998, 995]
    ret = solver(L, N, nums)
    print(ret)

if __name__ == '__main__':
    test()
