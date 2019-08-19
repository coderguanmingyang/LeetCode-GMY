# -*- coding:utf-8 -*-
'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
DFS：对每个节点进行dfs,将经过的“1”全改成“0”， 然后有多少可以dfs的节点就是多少个连通区域。
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)

        counter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(i, j)
        return counter
'''
并查集：
'''
class SolutionV2:
    def numIslands(self, grid):

        class UnionFind:

            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)] #秩，根节点的树的深度

            def get_count(self):
                return self.count

            # 找到该节点所在集合的代表节点，即根节点
            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p


            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            # 将两个根节点代表的集合合并
            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return

                # 如果两个节点不在一个集合就合并他们
                # 采用按秩来合并，总是将秩小的根节点挂到秩大的，保证合并之后秩不变
                # 这样能加快查找效率
                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                self.count -= 1

        row = len(grid)
        # 特判
        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummy_node = row * col

        # 多开的一个空间就是那个虚拟的空间
        uf = UnionFind(dummy_node + 1)

        for i in range(row):
            for j in range(col):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 不要忘记把那个虚拟结点减掉
        return uf.get_count() - 1




s = Solution()
a = [
['1','1','1','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
print s.numIslands(a)