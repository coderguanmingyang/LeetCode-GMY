'''
Given the root of a binary search tree with distinct values,
 modify it so that every node has a new value equal to the sum of the values of
  the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:



Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]


Note:

The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.

'''
## 此问题和538题一样

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        # 右中左的中序
        def inorderRightToLeft(node):
            if node == None:
                return None

            inorderRightToLeft(node.right)
            self.sum += node.val
            node.val = self.sum
            inorderRightToLeft(node.left)


        inorderRightToLeft(node=root)
        return root

from BinarySearchTree import insert, printTree

if __name__ == "__main__":
    root = TreeNode(17)
    insert(root, 2)
    insert(root, 5)
    insert(root, 29)
    insert(root, 33)
    insert(root, 38)
    insert(root, 35)
    printTree(root)
    root = Solution().bstToGst(root)
    printTree(root)
