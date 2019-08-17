# -*- coding:utf-8 -*-
'''

给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，
找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

示例:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
说明:
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。
'''
## 使用最小堆
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        length = len(matrix)
        if length == 1:
            return matrix[0][0]
        ref = []

        for i in range(length):
            for j in range(length):
                ref.append(matrix[i][j])
        heapq.heapify(ref)
        result = 0
        for i in range(k):
            result = heapq.heappop(ref)
        return result

## 用两次二分
class Solutionv2(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        ## 如果<=val的值大于k就返回True
        def guess(matrix, k, val):

            for i in range(row):
                left = 0
                right = col - 1
                ans = 0
                while(left <= right):
                    mid = left + (right - left) / 2
                    if matrix[i][mid] <= val:
                        left = mid + 1
                        ans = mid + 1
                    else:
                        right = mid - 1
                k -= ans
                if k < 1:
                    return True
            return False

        ans = 0
        left = matrix[0][0]
        right = matrix[row-1][col-1]
        while left <= right:
            mid = left + (right - left) / 2
            if guess(matrix, k, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

