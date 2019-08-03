# -*- coding:utf-8 -*-
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''

from queue import Queue

# Definition for a binary tree node.
class TreeNode(object):
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        que = Queue()
        if not root:
            return res
        que.put(root)
        while not que.empty():
            level = []
            level_num = que.qsize()
            for i in range(level_num):
                node = que.get()
                level.append(node.val)
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)
            res.append(level)
        return res

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    s = Solution()
    print s.levelOrder(root)
