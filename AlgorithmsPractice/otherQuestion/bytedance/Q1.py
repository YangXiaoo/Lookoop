import copy
def solver(N, alarm, X, end):
    """
    N 为闹钟个数
    alarm [[h, min], ...]
    X 起床时间 min
    end 上课时间"""

    endGetUP = endTime(X, end)  # 获得起床最晚时间
    print(endGetUP)
    alarm = sorted(alarm, key = lambda x : x[0])
    # print(alarm)
    for alm in alarm[::-1]:
        if alm[0] <= endGetUP[0] and alm[1] <= endGetUP[0]:
            ret = [str(x) for x in alm]
            return " ".join(ret)

    ret = [str(x) for x in alarm[-1]]
    return " ".join(ret)

def endTime(X, start):
    end = copy.deepcopy(start)
    if X <= end[-1]:
        end[-1] -= X
    elif X <= end[-1] + 60:
        if end[0] == 0:
            end[0] = 23
        else:
            end[0] -= 1
        end[-1] = end[-1] + 60 - X
    else:
        if end[0] <= 2:
            end[0] = 23 + end[0] - 2
        else:
            end[0] -= 2
        end[-1] = end[-1] + 120 - X

    return end


def test():
    N = 3
    alarm = [[23, 0],
             [6, 45],
             [7, 0]]
    X = 100
    end = [0, 12]

    ret = solver(N, alarm, X, end)
    print(ret)

if __name__ == '__main__':
    test()