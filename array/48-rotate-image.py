# -*- coding:utf-8 -*-
'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

'''
## 可以画出3*3 和 4*4 的矩阵找到规律，看成是左上角的大约1/4部分在移动，这里注意
## n为奇数时 左上角是一个矩形，而非正方形，所以注意边界条件，不能重复移动 也不能多移动

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        if n <= 1:
            return matrix
        import math
        for i in range(int(n/2)):
            border = n/2 if n%2 == 0 else int(n/2) + 1
            for j in range(border):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n - 1 - i] = temp
        return matrix

s = Solution()
print s.rotate([[1,2,3],[4,5,6],[7,8,9]])