# coding:UTF-8
# 2018-11-5
# FP-growing

import numpy as np 

def loadSimpDat():
    """
    测试数据
    """
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat


def createInitSet(data):
    """
    初始化数据
    """
    ret = {}
    for item in data:
        ret[frozenset(item)] = 1
    return ret


class treeNode():
    """
    创建节点类
    """
    def __init__(self, name_value, num_occur, parent_node):
        self.name = name_value
        self.count = num_occur
        self.node_link = None # 连接相似元素项
        self.parent = parent_node
        self.children = {} # 存储子节点


    def inc(self, num_occur):
        self.count += num_occur


    def disp(self, ind=1):
        print("*" * ind, self.name, ':', self.count)
        for child in self.children.values():
            child.disp(ind + 1)



def createTree(data, min_sup=1):
    """
    创建树
    data: {frozenset({'p', 'j', 'z', 'r', 'h'}): 1, frozenset({'t', 'z', 'y', 'v', 'u', 's', 'x', 'w'}): 1, frozenset({'z'}): 1, frozenset({'o', 'r', 's', 'x', 'n'}): 1, frozenset({'p', 't', 'z', 'y', 'r', 'q', 'x'}): 1, frozenset({'t', 'e', 'm', 'z', 'y', 'q', 's', 'x'}): 1}
    min_sup: 最小支持度
    步骤：
    a. 移除不满足最小支持度的元素项
    b. 根据全局频率对每个事物中的元素进行排序
    c. 使用排序后的频率项集进行建树
    d. 返回：树和每个元素对应的树节点
    """
    # a. 移除不满足最小支持度的元素项
    # 词频统计
    header_table = {}
    for item in data:
        for x in item:
            header_table[x] = header_table.get(x, 0) + data[item]
    tmp = []
    for k, v in header_table.items():
        if v < min_sup:
            tmp.append(k)
    for k in tmp:
        del(header_table[k])

    freq_item_set = set(header_table.keys())
    if len(freq_item_set) == 0: return None, None 
    # 更改header_table的结果使每个value存储词频和树节点
    for k in header_table:
        header_table[k] = [header_table[k], None]

    ret_tree = treeNode('null', 1, None) # 初始化树根节点
    for k, v in data.items():
        # v词频
        # b. 根据全局频率对每个事物中的元素进行排序
        local_items = {} # 每一个事务
        for item in k:
            if item in freq_item_set:
                local_items[item] = header_table[item][0]
        if len(local_items) > 0:
            # 从大到小进行排序
            item_sotred = [v[0] for v in sorted(local_items.items(), key=lambda x:x[1], reverse=True)]
            # c. 使用排序后的频率项集进行建树
            updateTree(item_sotred, ret_tree, header_table, v)
    # d. 返回：树和每个元素对应的树
    return ret_tree, header_table


def updateTree(items, tree, header_table, count):
    """
    items: 生成树的项
    tree: 树
    递归构建FP树
    """
    if items[0] in tree.children:
        # 如果在树中则词频+1
        tree.children[items[0]].inc(count)
    else:
        # 添加到tree的孩子中
        tree.children[items[0]] = treeNode(items[0], count, tree)
        # 连接相似元素
        if header_table[items[0]][1] == None:
            header_table[items[0]][1] = tree.children[items[0]]
        else:
            updateHeader(header_table[items[0]][1], tree.children[items[0]])
    if len(items) > 1:
        # 递归
        updateTree(items[1:], tree.children[items[0]], header_table, count)


def updateHeader(node, next_node):
    """
    连接相似元素
    将next_node连接到node
    """
    while node.node_link != None:
        node = node.node_link
    node.node_link = next_node


def ascendTree(node, prefix_path):
    """
    记录当前节点的所有父节点,返回结果包括当前结节点
    返回父节点的name属性
    """
    if node.parent != None:
        prefix_path.append(node.name)
        ascendTree(node.parent, prefix_path)


def findPrefixPath(node):
    """
    找到某一元素及其似元素项在树中的所有父类路径
    """
    ret_path = {}
    while node != None:
        prefix_path = []
        ascendTree(node, prefix_path)
        if len(prefix_path) > 1:
            ret_path[frozenset(prefix_path[1:])] = node.count
        node = node.node_link

    return ret_path


def minTree(tree, header_table, min_sup, prefix_path, freq_item_list):
    """
    生成FP条件树
    tree:FP树
    header_table:词频+节点
    min_sup:最小支持度
    prefix_path:set()
    freq_item_list:基于每一项的条件树
    """
    # 由小到大排序，从低端开始
    item_sotred = [v[0] for v in sorted(header_table.items(), key=lambda x:x[0])]

    for base_item in item_sotred:
        new_freq = prefix_path.copy()
        new_freq.add(base_item)
        freq_item_list.append(new_freq)
        cond_pattern_bases = findPrefixPath(header_table[base_item][1])
        my_cond_tree, my_header = createTree(cond_pattern_bases, min_sup)
        if my_header:
            minTree(my_cond_tree, my_header, min_sup, new_freq, freq_item_list)


if __name__ == '__main__':
    data = loadSimpDat()
    data_set = createInitSet(data)
    print(data_set)
    min_sup = 3
    fp_tree, header_table = createTree(data_set, min_sup)
    # print(header_table)
    fp_tree.disp()
    freq_item_list = []
    minTree(fp_tree, header_table, min_sup, set([]), freq_item_list)
    print(freq_item_list)
    print(len(freq_item_list)) # 18
    # [{'r'}, {'s'}, {'x', 's'}, {'t'}, {'x', 't'}, {'y', 't'}, {'x', 'y', 't'}, {'z', 't'}, {'x', 'z', 't'}, {'y', 'z', 't'}, {'x', 'y', 'z', 't'}, {'x'}, {'x', 'z'}, {'y'}, {'x', 'y'}, {'y', 'z'}, {'x', 'y', 'z'}, {'z'}]