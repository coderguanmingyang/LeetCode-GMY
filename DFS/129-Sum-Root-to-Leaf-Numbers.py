# -*- coding:utf-8 -*-
'''

给定一个二叉树，它的每个结点都存放一个 0-9 的数字，
每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

'''
## 此题考查dfs,结合题目特点，第一想法就是将dfs的path记录进来，然后再转换成int,
## 这种方法最直观，最简单

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.paths = []
        if not root:
            return 0
        def dfs(root, path):
            path = path + str(root.val)
            if root.left == None and root.right == None and path != "":
                self.paths.append(path)
                return 0
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
        dfs(root, "")
        self.paths = map(int, self.paths)
        return sum(self.paths)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s =Solution()
print s.sumNumbers(root)