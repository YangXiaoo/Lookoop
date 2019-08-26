# coding:utf-8
import sys
# base64算法
# AC 33%
def solver(s):
    maps = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    ords = []
    for c in s:
        ords.append(ord(c))
    print("[debug] ords: {}".format(ords))
    bins = ""
    for binary in ords:
        bins += '0' + str(bin(binary))[2:]
    print("[debug] bins: {}".format(bins))
    ret = ""
    for i in range(0, len(bins), 24):
        cur =  bins[i:i+24]
        gap = 0
        if len(cur) != 24:
            gap = 24 - len(cur)
            cur += gap * '0'
        # print("[debug] gap: {}".format(gap))
        for j in range(0, 24, 6):
            if j > (24 - gap):
                continue
            curIndex = int(cur[j:j+6], base=2)
            # print("[debug] i: {}, j: {}, curIndex: {} maps[curIndex]:{}".format(i, j, curIndex,maps[curIndex]))
            ret += maps[curIndex]
    # print("[debug] tmp ret: {}".format(ret))
    if len(s) % 3 == 1:
        ret = ret + "=="
    elif len(s) % 3 == 2:
        ret = ret + "="

    return ret 


def test():
    s = "Man"
    ret = solver(s)
    print(ret)


def inputs():
    line = sys.stdin.readline()
    ret = solver(line)
    print(ret)


if __name__ == '__main__':
    test()
