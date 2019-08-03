# -*- coding:utf-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preTraverse(root):
    '''
    前序遍历
    '''
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    '''
    中序遍历
    '''
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def afterTraverse(root):
    '''
    后序遍历
    '''
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

