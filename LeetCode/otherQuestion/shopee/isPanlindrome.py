import sys
def getox(num):
    """获得十六进制"""
    if num == 0:
        return [0]
    ret = []
    while num:
        cur = num % 16
        ret.append(cur)
        num = num // 16

    return ret

def isPanlindrome(nums):
    """验证是否为回文串"""
    if nums == nums[::-1]:
        return 1

    return 0

def solver(num):
    """方法入口"""
    ox = getox(num)
    ret = isPanlindrome(ox)
    return ret

def test():
    num = 1
    ret = solver(num)
    print(ret)

    
if __name__ == '__main__':
    test()

