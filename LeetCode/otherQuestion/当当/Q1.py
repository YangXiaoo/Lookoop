# coding:utf-8
# 2019/9/2
# 阿拉伯数字转为中文大小写
# 11011 -> 壹万壹仟零壹拾壹元整
import sys

def solver(num):
    maps = {0:'零', 1:'壹', 2:'贰', 3:'叁', 4:'肆', 5:'伍', 6:'陆', 7:'柒', 8:'捌', 9:'玖'}
    unit = {1:'元', 10:'拾', 100:'佰', 1000:'仟', 10000:'万', 100000:'拾万', 1000000:'佰万', 10000000:'仟万', 100000000:'亿'}

    ret = "整"
    high = 1
    while num:  
        cur = num % 10
        if cur != 0:
            ret = unit.get(high, '') + ret
        if high == 1 and cur == 0:
            pass
        else:
            ret = maps[cur] + ret 
        num //= 10
        high *= 10

    return ret 

def test():
    num = 1101
    ret = solver(num)
    expect = "壹拾壹元整"
    print(ret)

def inputs():
    num = int(sys.stdin.readline().strip())
    ret = solver(num)
    print(ret)

if __name__ == '__main__':
    test()