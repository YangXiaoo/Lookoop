import matplotlib.pyplot as plt
import math
import random

"""
函数里面所有以plot开头的函数都可以注释掉，没有影响
求解的目标表达式为：
y = 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
"""


def main():
    print('y = 10 * math.sin(5 * x) + 7 * math.cos(4 * x)')
    plot_obj_func()
    pop_size = 500  # 种群数量
    upper_limit = 10  # 基因中允许出现的最大值
    chromosome_length = 10  # 染色体长度
    iter = 500
    pc = 0.6 # 杂交概率
    pm = 0.01  # 变异概率
    results = []  # 存储每一代的最优解，N个二元组
    # pop = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1] for i in range(pop_size)]
    pop = init_population(pop_size, chromosome_length)
    best_X = []
    best_Y = []
    for i in range(iter):
        obj_value = calc_obj_value(pop, chromosome_length, upper_limit)  # 个体评价，有负值
        fit_value = calc_fit_value(obj_value)  # 个体适应度，不好的归0，可以理解为去掉上面的负值
        best_individual, best_fit = find_best(pop, fit_value)  # 第一个是最优基因序列, 第二个是对应的最佳个体适度
        # 下面这句就是存放每次迭代的最优x值是最佳y值
        results.append([binary2decimal(best_individual, upper_limit, chromosome_length), best_fit])

        # 查看一下种群分布
        # plot_currnt_individual(decode_chromosome(pop, chromosome_length, upper_limit), obj_value)

        selection(pop, fit_value)  # 选择
        crossover(pop, pc)  # 染色体交叉（最优个体之间进行0、1互换）
        mutation(pop, pm)  # 染色体变异（其实就是随机进行0、1取反）
        # 最优解的变化
        if iter % 20 == 0:
            best_X.append(results[-1][0])
            best_Y.append(results[-1][1])
    print("x = %f, y = %f" % (results[-1][0], results[-1][1]))
    # 看种群点的选择
    plt.scatter(best_X, best_Y, s=3, c='r')
    X1 = [i / float(10) for i in range(0, 100, 1)]
    Y1 = [10 * math.sin(5 * x) + 7 * math.cos(4 * x) for x in X1]
    plt.plot(X1, Y1)
    plt.show()
    # 看迭代曲线
    plot_iter_curve(iter, results)


# 看看我们要处理的目标函数
def plot_obj_func():
    """y = 10 * math.sin(5 * x) + 7 * math.cos(4 * x)"""
    X1 = [i / float(10) for i in range(0, 100, 1)]
    Y1 = [10 * math.sin(5 * x) + 7 * math.cos(4 * x) for x in X1]
    plt.plot(X1, Y1)
    plt.show()


# 看看当前种群个体的落点情况
def plot_currnt_individual(X, Y):
    X1 = [i / float(10) for i in range(0, 100, 1)]
    Y1 = [10 * math.sin(5 * x) + 7 * math.cos(4 * x) for x in X1]
    plt.plot(X1, Y1)
    plt.scatter(X, Y, c='r', s=5)
    plt.show()


# 看看最终的迭代变化曲线
def plot_iter_curve(iter, results):
    X = [i for i in range(iter)]
    Y = [results[i][1] for i in range(iter)]
    plt.plot(X, Y)
    plt.show()


# 计算2进制序列代表的数值
def binary2decimal(binary, upper_limit, chromosome_length):
    t = 0
    for j in range(len(binary)):
        t += binary[j] * 2 ** j
    t = t * upper_limit / (2 ** chromosome_length - 1)
    return t


def init_population(pop_size, chromosome_length):
    # 形如[[0,1,..0,1],[0,1,..0,1]...]
    pop = [[random.randint(0, 1) for i in range(chromosome_length)] for j in range(pop_size)]
    return pop


# 解码并计算值
def decode_chromosome(pop, chromosome_length, upper_limit):
    X = []
    for ele in pop:
        temp = 0
        # 二进制变成实数，种群中的每个个体对应一个数字
        for i, coff in enumerate(ele):
            # 就是把二进制转化为十进制的
            temp += coff * (2 ** i)

        # 这个是把前面得到的那个十进制的数，再次缩放为另一个实数
        # 注意这个实数范围更广泛，可以是小数了，而前面二进制解码后只能是十进制的数
        # 参考https://blog.csdn.net/robert_chen1988/article/details/79159244
        X.append(temp * upper_limit / (2 ** chromosome_length - 1))
    return X


def calc_obj_value(pop, chromosome_length, upper_limit):
    obj_value = []
    X = decode_chromosome(pop, chromosome_length, upper_limit)
    for x in X:
        # 把缩放过后的那个数，带入我们要求的公式中
        # 种群中个体有几个，就有几个这种“缩放过后的数”
        obj_value.append(10 * math.sin(5 * x) + 7 * math.cos(4 * x))
    # 这里先返回带入公式计算后的数值列表，作为种群个体优劣的评价
    return obj_value


# 淘汰
def calc_fit_value(obj_value):
    fit_value = []
    # 去掉小于0的值，更改c_min会改变淘汰的下限
    # 比如设成10可以加快收敛
    # 但是如果设置过大，有可能影响了全局最优的搜索
    c_min = 10
    for value in obj_value:
        if value > c_min:
            temp = value
        else:
            temp = 0.
        fit_value.append(temp)
    # fit_value保存的是活下来的值
    return fit_value


# 找出最优解和最优解的基因编码
def find_best(pop, fit_value):
    # 用来存最优基因编码
    best_individual = []
    # 先假设第一个基因的适应度最好
    best_fit = fit_value[0]
    for i in range(1, len(pop)):
        if (fit_value[i] > best_fit):
            best_fit = fit_value[i]
            best_individual = pop[i]
    # best_fit是值
    # best_individual是基因序列
    return best_individual, best_fit


# 计算累计概率
def cum_sum(fit_value):
    # 输入[1, 2, 3, 4, 5]，返回[1,3,6,10,15]，matlab的一个函数
    # 这个地方遇坑，局部变量如果赋值给引用变量，在函数周期结束后，引用变量也将失去这个值
    temp = fit_value[:]
    for i in range(len(temp)):
        fit_value[i] = (sum(temp[:i + 1]))


# 轮赌法选择
def selection(pop, fit_value):
    # https://blog.csdn.net/pymqq/article/details/51375522

    p_fit_value = []
    # 适应度总和
    total_fit = sum(fit_value)
    # 归一化，使概率总和为1
    for i in range(len(fit_value)):
        p_fit_value.append(fit_value[i] / total_fit)
    # 概率求和排序

    # https://www.cnblogs.com/LoganChen/p/7509702.html
    cum_sum(p_fit_value) # 计算累计概率
    pop_len = len(pop)
    # 类似搞一个转盘吧下面这个的意思
    ms = sorted([random.random() for i in range(pop_len)])
    fitin = 0
    newin = 0
    newpop = pop[:]
    # 转轮盘选择法
    while newin < pop_len:
        # 如果这个概率大于随机出来的那个概率，就选这个
        if (ms[newin] < p_fit_value[fitin]):
            newpop[newin] = pop[fitin]
            newin = newin + 1
        else:
            fitin = fitin + 1
    # 这里注意一下，因为random.random()不会大于1，所以保证这里的newpop规格会和以前的一样
    # 而且这个pop里面会有不少重复的个体，保证种群数量一样

    # 之前是看另一个人的程序，感觉他这里有点bug，要适当修改
    pop = newpop[:]


# 杂交
def crossover(pop, pc):
    # 一定概率杂交，主要是杂交种群种相邻的两个个体
    pop_len = len(pop)
    for i in range(pop_len - 1):
        # 随机看看达到杂交概率没
        if (random.random() < pc):
            # 随机选取杂交点，然后交换数组
            cpoint = random.randint(0, len(pop[0]))
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0:cpoint])
            temp1.extend(pop[i + 1][cpoint:len(pop[i])])
            temp2.extend(pop[i + 1][0:cpoint])
            temp2.extend(pop[i][cpoint:len(pop[i])])
            pop[i] = temp1[:]
            pop[i + 1] = temp2[:]


# 基因突变
def mutation(pop, pm):
    px = len(pop)
    py = len(pop[0])
    # 每条染色体随便选一个杂交
    for i in range(px):
        if (random.random() < pm):
            mpoint = random.randint(0, py - 1)
            if (pop[i][mpoint] == 1):
                pop[i][mpoint] = 0
            else:
                pop[i][mpoint] = 1


if __name__ == '__main__':
    main()
