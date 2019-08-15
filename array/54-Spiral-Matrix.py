# -*- coding:utf-8 -*-
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        NROW = len(matrix)
        NCOL = len(matrix[0])
        # 一圈一圈来，用深度来控制
        def helper(depth):
            nrow, ncol = NROW - 2 * depth, NCOL - 2 * depth
            if nrow <= 0 or ncol <= 0: return []
            if nrow == 1: return matrix[depth][depth:depth + ncol]
            if ncol == 1: return [matrix[r][depth] for r in range(depth, depth + nrow)]

            res = []
            res += matrix[depth][depth:depth + ncol - 1]
            res += [matrix[r][depth + ncol - 1] for r in range(depth, depth + nrow - 1)]
            res += reversed(matrix[depth + nrow - 1][depth + 1:depth + ncol])
            res += [matrix[r][depth] for r in reversed(range(depth + 1, depth + nrow))]
            return res + helper(depth + 1)

        return helper(0)

