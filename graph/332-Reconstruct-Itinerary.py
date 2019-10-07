# -*- coding:utf-8 -*-
'''
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，
对该行程进行重新规划排序。所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发。

说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"]
与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
【假定所有机票至少存在一种合理的行程。】
示例 1:

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-itinerary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

此题考查的是欧拉路径的求解，即一笔画，边不能重复，点可以重复，能走过所有的边。
'''

import collections
# Hierholzer 算法
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = collections.defaultdict(list)
        for f, t in tickets:
            adj[f].append(t)
        for f in adj:
            adj[f].sort()
        res = []
        self.dfs(adj, "JFK", res)
        return res[::-1]

    def dfs(self, graph, source, res):
        while graph[source]:
            v = graph[source].pop(0)
            self.dfs(graph, v, res)
        res.append(source)

#DFS
class SolutionV2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        routes = collections.defaultdict(list)
        for s, e in tickets:
            routes[s].append(e)
        def solve(start):
            left, right = [], []
            for end in sorted(routes[start]):
                if end not in routes[start]:
                    continue
                routes[start].remove(end)
                subroutes = solve(end)
                if start in subroutes:
                    left += subroutes
                else:
                    right += subroutes
            return [start] + left + right
        return solve("JFK")

s = Solution()
tickets = [
    ["MUC", "LHR"],
    ["JFK", "MUC"],
    ["SFO", "SJC"],
    ["LHR", "SFO"]
]
print s.findItinerary(tickets)
tickets = [
["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]
]
print s.findItinerary(tickets)