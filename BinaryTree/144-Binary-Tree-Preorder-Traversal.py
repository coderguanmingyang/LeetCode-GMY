# -*- coding:utf-8 -*-

'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

#      8
#   6     10
# 5  7   9  11


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 二叉树非递归前序序遍历
    def preorderTraversal(self, root):
        if not root:
            return None
        node_list = []
        p = root
        res = []
        while p or len(node_list):
            # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
            while p:
                node_list.append(p)
                res.append(p.val) # 前序遍历要求先打印根，所以，一直遍历左子树，其实在保存左子树的各个根
                p = p.left
            # 开始出栈
            if len(node_list):
                p = node_list[-1]
                node_list.pop()
                p = p.right
        return res

    # 二叉树非递归中序遍历
    def inorderTraversal(self, root):
        node_list = []
        p = root
        res = []
        while p or len(node_list) != 0:
            # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
            while p:
                node_list.append(p)
                p = p.left
            # 开始出栈
            if len(node_list):
                p = node_list[-1]
                node_list.pop()
                res.append(p.val)
                # 进入右子树
                p = p.right
        return res

    # 二叉树非递归后序序遍历
    def postorderTraversal(self, root):
        if not root:
            return None
        node_list = []
        p = root
        pLast = None
        res = []
        # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
        while p:
            node_list.append(p)
            p = p.left
        # 开始出栈
        while len(node_list):
            p = node_list[-1]
            node_list.pop()
            # 若无右子树或者右子树被访问，则访问该节点
            # 若右子树被访问过，则说明当前根节点要被打印出来
            if not p.right or p.right == pLast:
                res.append(p.val)
                pLast = p
            else:
                # 节点再次入栈
                node_list.append(p) # 保证右节点在栈的top部位
                p = p.right
                while p:
                    node_list.append(p)
                    p = p.left
        return res


def main():
    solution = Solution()
    root = TreeNode(8)
    root.left = TreeNode(6)
    node1 = root.left
    root.right = TreeNode(10)
    node2 = root.right
    node1.left = TreeNode(5)
    node1.right = TreeNode(7)
    node2.left = TreeNode(9)
    node2.right = TreeNode(11)
    print(solution.inorderTraversal(root))
    print(solution.postorderTraversal(root))
    print(solution.preorderTraversal(root))


if __name__ == '__main__':
    main()
