import sys
def solver(mat):
    dist = (2**len(mat)) * (len(mat)**2)
    flag = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                dist = min(compute(i, j, mat), dist)
                flag = True
    if not flag:
        return -1
    return dist

def compute(i, j, mat):
    retDist = 0
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] != 0:
                retDist += (abs(r-i) + abs(c-j))
            
    return retDist

if __name__ == '__main__':
    mat = [[0,1,1,0],
            [1,1,0,1],
            [0,0,1,0],
            [0,0,0,0]]
    ret = solver(mat)
    print(ret)