# -*- coding:utf-8 -*-
'''

给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。
该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42


'''

# 此题是二叉树求解问题，所以一般采用递归的方式，即递归左右子树
# 此题需要用到一个全局变量来存最大路径，这样每次都用递归过程的结果来比较更新
# 通过分析，对于每个节点（当他作为root），最大路径有三种方式：
# 即1. 当前节点 + 左子树
# 2. 当前节点 + 右子树
# 3. 左子树 + 当前节点 + 右子树 (这种比较特殊，即此时这个结果不能作为向上递归的值，因为不能向上相连了)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def maxPathSum(self, root):
        self.res = float("-inf")

        def helper(root):
            if not root: return 0
            # 右边最大值
            left = helper(root.left)
            # 左边最大值
            right = helper(root.right)
            # 和全局变量比较
            self.res = max(left + right + root.val, self.res) #将第三种情况比较进来
            # >0 说明都能使路径变大
            return max(0, max(left, right) + root.val)
            # 这里只考虑和左右相连的情况
            # 当负数时，即返回0 相当于当前子树并没有起作用，相当于 helper只返回大于0的数

        helper(root)
        return self.res
