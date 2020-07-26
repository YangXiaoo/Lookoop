# coding:utf-8

"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
import collections

"""
类似题
LeetCode 684. Redundant Connection
LeetCode 547. Friend Circles
LeetCode 737. Sentence Similarity II
"""
# 2020-7-26
# graph
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """        
        def helper(x, y, queryed):
            if x == y:
                return 1.0
            queryed.add(x)
            for n in equationsMapper[x]:
                if n in queryed: continue
                queryed.add(n)
                tmpRet = helper(n, y, queryed)
                if tmpRet > 0:
                    return tmpRet * equationsMapper[x][n]

            return -1.0

        equationsMapper = self.mapperFit(equations, values)
        print(equationsMapper)
        ret = [helper(x, y, set()) if x in equationsMapper and y in equationsMapper else -1.0 for (x, y) in queries]

        return ret

    def mapperFit(self, equations, values):
        """完成字典转换"""
        mapper = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            mapper[x][y] = value
            mapper[y][x] = 1 / value 

        return mapper

    def calcEquation2(self, equations, values, queries):
        """不使用尾递归"""
        def helper(x, y, value, queryed):
            nonlocal tmpRet
            if x not in queryed:
                queryed.add(x)
                if x == y:
                    tmpRet = value
                    return 
                else:
                    for nxt in equationsMapper[x]:
                        helper(nxt, y, value*equationsMapper[x][nxt], queryed)

        equationsMapper = self.mapperFit(equations, values)
        print(equationsMapper)

        ret = []
        for (x, y) in queries:
            if x in equationsMapper and y in equationsMapper:
                tmpRet = 1.0 
                helper(x, y, 1.0, set())
                ret.append(tmpRet)
            else:
                ret.append(-1.0)
        return ret


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

test = Solution()
ret = test.calcEquation(equations, values, queries)
print(ret)