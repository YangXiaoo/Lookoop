def solver(n, m):
    ret = 0
    flag = -1
    it = 0
    for i in range(1, n+1):
        if it == m:
            flag *= -1
            it = 0
        # print(flag*i)
        ret += flag * i
        it += 1

    return ret

def test():
    n, m = 8, 2
    ret = solver(n, m)
    print(ret)

if __name__ == '__main__':
    test()