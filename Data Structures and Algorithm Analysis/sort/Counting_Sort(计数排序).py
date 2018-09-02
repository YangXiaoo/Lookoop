# 2018-7-30
# Counting Sort
# Introduction to Algrithms P108

"""
Input A
Output B
temp C
"""
def countingSort(A):

    lens = len(A)
    B = [0] * lens # intinalize B

    # find k in A
    k = A[0]
    for n in A:
        if n > k:
            k = n

    # Initialize C
    C = [0] * (k + 1)
    lensC = len(C)

    # Record the occurence of each element in arry A
    for i in range(lens):
        C[A[i]] = C[A[i]] + 1

    # print(C)
    # Record how many element is less or equal to i
    for i in range(1, lensC):
        C[i] += C[i-1]

    # print(C, "c")

    for i in range(0, lens):
        # print(B)
        B[C[A[i]] - 1] = A[i]
        C[A[i]] = C[A[i]] - 1

    return B

A = [2,5,3,0,2,3,0,3]
res = countingSort(A)
print(res)


