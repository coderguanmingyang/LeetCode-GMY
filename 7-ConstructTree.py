# -*- coding:utf-8 -*-

## 输入某二叉树的前序遍历和中序遍历的结果，
# 请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。
# 剑指Offer 面试题7
# Reference:https://blog.csdn.net/micro_hz/article/details/78734991

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def ConstructBinaryTree(self, preOrder, inOrder):
        if len(preOrder) == 0 or len(inOrder) == 0:
            return None

        root = TreeNode(preOrder[0]) ## 前序的第一个元素是根节点
        child = self.getChildTree(preOrder, inOrder)

        root.left = self.ConstructBinaryTree(child['pre_left'], child['in_left'])
        root.right = self.ConstructBinaryTree(child['pre_right'], child['in_right'])

        return root


    def getChildTree(self, preOrder, inOrder):

        root_val = preOrder[0]
        pre_left = []
        pre_right = []
        in_left = []
        in_right = []
        flag = False
        for i in inOrder:
            if i == root_val:
                flag = True
                continue
            if not flag:
                in_left.append(i)
            else:
                in_right.append(i)

        for i in preOrder:
            if i in in_left:
                pre_left.append(i)
            if i in in_right:
                pre_right.append(i)

        return {'pre_left':pre_left, "pre_right":pre_right,
                "in_left":in_left, "in_right":in_right}

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
s = Solution()
root = s.ConstructBinaryTree(pre, tin)

print(root)