def solver(N, K, bins):
    orig = [0 for _ in range(N)]
    mat = [[-1 for _ in range(N + K -1)] for _ in range(K)]
    # print(mat)
    for i in range(N):
        curValue = []
        for r in range(K):
            if mat[r][i] != -1:
                curValue.append(mat[r][i])
        curBin = bins[i]
        for n in curValue:
            curBin = curBin ^ n 

        col = i 
        for r in range(K):
            mat[r][col] = curBin
            col += 1

    # print(mat)
    ret = [str(x) for x in mat[0][:N]]

    return "".join(ret)

def test():
    N, K = 2, 6
    bins = [int(x) for x in "01"]
    ret = solver(N, K, bins)
    print(ret)

if __name__ == '__main__':
    test()
