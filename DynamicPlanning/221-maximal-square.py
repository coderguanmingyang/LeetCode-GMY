# -*- coding:utf-8 -*-
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''
## 构建一个尺寸一样的矩阵a，a中元素代表以当前位置为右下角的、最大的、全1的正方形的边长
# 则有这个转移方程： a[i][j] = min(a[i-1][j], a[i][j-1], a[i-1][j-1]) + 1
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        max_edge = 0
        a = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                a[i][0] = 1
                max_edge = 1

        for j in range(len(matrix[0])):
            if matrix[0][j] == "1":
                a[0][j] = 1
                max_edge = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    a[i][j] = min(a[i-1][j], a[i][j-1], a[i-1][j-1]) + 1
                    if a[i][j] > max_edge:
                        max_edge = a[i][j]
                else:
                    a[i][j] = 0
        return max_edge * max_edge

if __name__ == "__main__":
    s = Solution()
    m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    m = [["1","1"]]
    m =[]
    print s.maximalSquare(m)