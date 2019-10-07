# -*- coding:utf-8 -*-
'''
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，
满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，
则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
示例 2：

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
注意:

输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。
更新(2017-09-26):
我们已经重新检查了问题描述及测试用例，明确图是无向 图。对于有向图详见冗余连接II。
对于造成任何不便，我们深感歉意。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
# 用并查集来解决，如果出现一条边的两个端点都在一个set里边，那几说明出现环了，要删除的也是这条边

class UnionFind:
    def __init__(self):
        self.par = list(range(5001)) # 父节点
        self.rnk = [0] * 5001 # 记录树的高度

    # 确定元素属于哪一个子集
    def find(self, x):
        # 如果x有根
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x]) # 在find的同时进行路径压缩，将父节点指向根
        return self.par[x]

    # 将两个子集合并成同一个集合
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        # 如果两个元素的根一样，即属于一个组
        if px == py:
            return False
        # 属于不同组，就将其根连接起来
        else:
            # 高度小的树挂到高度大的树
            if self.rnk[px] > self.rnk[py]:
                self.par[py] = px
            elif self.rnk[px] < self.rnk[py]:
                self.par[px] = py
            else:
                self.par[py] = px
                self.rnk[px] += 1
            return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind()
        for e in edges:
            if not uf.union(e[0], e[1]):
                return e