# -*- coding:utf-8 -*-

'''

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution1: 二叉查找树，用中序遍历应该是一个递增的序列
class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def midTraverse(root):
            '''
            中序遍历
            '''
            if root == None:
                return
            midTraverse(root.left)

            self.inorder.append(root.value)

            midTraverse(root.right)

        self.inorder = []
        midTraverse(root)
        for i in range(1, len(self.inorder)):
            if self.inorder[i-1] > self.inorder[i]:
                return False
        return True

# solution2: 用递归的方式，这里需要注意二叉搜索树的左子树的所有节点全都小于根节点
# 即 要确定上下界
class Solution2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)




