# -*- coding:utf-8 -*-

'''
  二叉搜索树(Binary Search Tree)，又名二叉排序树(Binary Sort Tree)。
  二叉搜索树是具有有以下性质的二叉树：
  （1）若左子树不为空，则左子树上所有节点的值均小于或等于它的根节点的值。
  （2）若右子树不为空，则右子树上所有节点的值均大于或等于它的根节点的值。
  （3）左、右子树也分别为二叉搜索树。

'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#从根节点开始，若插入的值比根节点的值小，则将其插入根节点的左子树；
# 若比根节点的值大，则将其插入根节点的右子树。该操作可使用递归进行实现。
def insert(root, val):
    if root == None:
        root = TreeNode(val)
    elif val <= root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

# 从根节点开始查找，待查找的值是否与根节点的值相同，若相同则返回True；
# 否则，判断待寻找的值是否比根节点的值小，若是则进入根节点左子树进行查找，
# 否则进入右子树进行查找。该操作使用递归实现。

def query(root, val):
    if root == None: return False
    if root.val == val:
        return True
    elif val < root.val:
        return query(root.left, val)
    elif val > root.val:
        return query(root.right, val)

# 查找最小值：从根节点开始，沿着左子树一直往下，直到找到最后一个左子树节点
def findMin(root):
    if root == None: return None
    while root.left:
        root = root.left
    return root.val

# 查找最大值：从根节点开始，沿着左子树一直往下，直到找到最后一个左子树节点
def findMax(root):
    if root == None: return None
    while root.right:
        root = root.right
    return root.val

def delNode(root, val):
    if root == None:
        return None

    if val < root.val:
        root.left = delNode(root.left, val)
    elif val > root.val:
        root.right = delNode(root.right, val)
    else:
        if root.left == None and root.right == None:
            root = None
        elif root.left != None and root.right != None:
            temp = findMin(root.right)
            root.val = temp
            delNode(root.right, temp)
        elif root.left == None:
            root = root.right
        elif root.right == None:
            root = root.left
    return root


# 按照中序打印
def printTree(root):
    # 打印二叉搜索树(中序打印，有序数列)
    if root == None:
        return
    printTree(root.left)
    print(str(root.val))
    printTree(root.right)

if __name__ == "__main__":
    root = TreeNode(17)
    insert(root, 2)
    insert(root, 5)
    insert(root, 29)
    insert(root, 33)
    insert(root, 38)
    insert(root, 35)
    #print query(root, 34)
    #print query(root, 35)
    #print findMin(root)
    #print findMax(root)
    printTree(root)
    root = delNode(root, 29)
    printTree(root)