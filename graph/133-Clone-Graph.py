# -*- coding:utf-8 -*-
'''
给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。
图中的每个节点都包含它的值 val（Int） 和其邻居的列表（list[Node]）。

示例：



输入：
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},
{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},
{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

解释：
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
 

提示：

节点数介于 1 到 100 之间。
无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
必须将给定节点的拷贝作为对克隆图的引用返回。



'''


# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        if node == None:
            return None
        else:
            map = {}
            for key, val in self.dfs(node, map).items():
                val.neighbors = [map[x] for x in key.neighbors]
            return map[node]

    # DFS 将图中所有节点和自身建立一个字典，相当于把所有节点复制了一下
    def dfs(self, node, map):
        if node not in map:  # 如果在map里，就说明已经遍历复制了，返回map即可
            map[node] = Node(node.val, None)
            for i in node.neighbors:
                self.dfs(i, map)
        return map


#不用递归，用栈
class SolutionV2:
    def cloneGraph(self, node):
        memories = {}
        stack = [node]   # 利用一个栈来模拟递归
        memories[node] = Node(node.val, None)
        while stack:
            cur = stack.pop()
            for nodes in cur.neighbors:        # 先判断有没有访问过这个节点
                if nodes not in memories:
                    memories[nodes] = Node(nodes.val,None)
                    stack.append(nodes)

        for key,val in memories.items():
            val.neighbors = [memories[x] for x in key.neighbors]
        return memories[node]

a = Node(1, None)
s = Solution()
d = s.cloneGraph(a)
b = Node(2, [a])
c = Node(3, [a])
a.neighbors = [b, c]
s = Solution()
d = s.cloneGraph(a)

