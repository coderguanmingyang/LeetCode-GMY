# -*- coding:utf-8
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import Queue
class Solution(object):
    ## 用广搜来实现 最先找到一个叶子节点 即返回当前level
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        que = Queue.Queue()
        que.put(root)
        level = 1
        while not que.empty():
            level_num = que.qsize()
            for i in range(level_num):
                node = que.get()
                if node.left == None and node.right == None:
                    return level
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)
            level += 1

    def minDepth_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:  # 一旦到达叶子节点的下一级（null），就返回0
            return 0
        if root.left and root.right: # 如果左右子树都有就是最小的深度+1，典型的递归思想
            return min(self.minDepth_dfs(root.left), self.minDepth_dfs(root.right)) + 1
        elif root.right == None: # 右子树为空，那么就是左子树的最小深度 + 1，倘若左子树也为空，左子树返回来的是0
            return self.minDepth_dfs(root.left) + 1
        elif root.left == None:
            return self.minDepth_dfs(root.right) + 1
