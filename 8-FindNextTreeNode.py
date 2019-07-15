# -*- coding:utf-8 -*-

## 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# 剑指Offer 面试题8
# Reference:https://blog.csdn.net/u010005281/article/details/79718856

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None #父节点

class Solution():
    def getNextNode(self, curNode):

        if not curNode: # 当前节点为空
            return None

        if curNode.right is not None: # 有右子树
            return self.getRightTreeLeftNode(curNode.right)
        else: # 没有右子树
            return self.getHeadTree(curNode)

    """
    获取右子树的最左节点
    """
    def getRightTreeLeftNode(self, curNode):
        while curNode.left:
            curNode = curNode.left
        return curNode

    """
    没有右子树
    """
    def getHeadTree(self, curNode):
        while curNode.next:
            father = curNode.next
            if father.left == curNode: # 如果当前节点为左子节点，那么下一个节点就是父节点
                return father
            elif father.right == curNode: # 如果当前节点为右子节点，那么还要继续向上找
                curNode = curNode.next
        return None #找不到说明当前节点是左后一个节点
