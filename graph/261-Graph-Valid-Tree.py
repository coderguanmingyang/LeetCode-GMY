# -*- coding:utf-8 -*-
'''
[以图判树]
给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），
请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，
边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/graph-valid-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
## 此题判断是否给出的图能构成树，那么采用并查集的方法，只要检测是否出现两个以上集合，还有就是检查是否出现环
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n+1)) # 父节点
        self.rnk = [0] * (n+1) # 记录树的高度

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
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UnionFind(n)
        for e in edges:
            if not uf.union(e[0], e[1]):
                return False #出现环
        par_set = set()
        for i in range(n):
            par_set.add(uf.find(i))
            if len(par_set)> 1:
                return False #超过两个集合
        return True

# 用邻接矩阵+BFS
class SolutionV2(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adj = [[0]* n for i in range(n)]
        for e in edges:
            adj[e[0]][e[1]] = 1
            adj[e[1]][e[0]] = 1
        visited = [False] * n
        Q = [0]
        visited[0] = True
        while len(Q) != 0:
            node = Q.pop(0)
            for j in range(n):
                if adj[node][j] == 1:
                    if visited[j] == True: #如果之前访问过就说明出现环
                        return False
                    visited[j] = True
                    adj[node][j] = 0 #访问过就涂黑
                    adj[j][node] = 0
                    Q.append(j)

        for i in visited:
            if i == False:
                return False
        return True


s =SolutionV2()
print s.validTree(5, [[0,1], [0,2], [0,3], [1,4]])
print s.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]])

