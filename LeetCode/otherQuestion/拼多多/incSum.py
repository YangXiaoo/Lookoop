def getAsm(n, s):
    ret = []
    def dfs(index, tmp):
        nonlocal ret, s, n
        if len(tmp) == n - 1:
            curSum = sum(tmp)
            ret.append(tmp.append(s - curSum))
            tmp.pop()
        else:
            for i in range(index, s):
                tmp.append(i)
                curSum = sum(tmp)
                if len(tmp) < n:
                    if s - curSum > tmp[-1]:
                        dfs(i + 1, tmp)
                if tmp:
                    tmp.pop()

    dfs(1, [])

    return ret 

def solver(n, s):
    asm = getAsm(n, s)
    return len(asm) % 1000000007
#####################################

def test():
    n, s = 3, 10
    asm = solver(n, s)
    print(asm)

if __name__ == '__main__':
    test()
