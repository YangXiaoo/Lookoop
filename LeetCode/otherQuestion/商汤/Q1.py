# coding=utf-8
def solver(nums):
    x1, y1, w1, h1, x2, y2, w2, h2 = nums
    w = min(x1 + w1, x2 + w2)
    h = min(y1 + h1, y2 + h2)

    x = max(x1, x2)
    y = max(y1, y2)

    if x >= w and y >= h:
        return "null"

    ret = [x, y, w-x, h-y]

    return " ".join([str(x) for x in ret])

def test():
    nums = [0,0,200,200,100,100,100,100]
    ret = solver(nums)

    print(ret)
    
if __name__ == '__main__':
    test()
