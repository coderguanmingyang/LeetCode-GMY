# -*- coding:utf-8 -*-
'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

'''

'''
动态规划：dp_max[i]代表右边界为i的连续子串的最大乘积
        dp_min[i]代表右边界为i的连续子串的最小乘积
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        #res = - float("inf")
        for i in range(1, n):
            if nums[i] < 0:
                mi, ma = dp_max[i-1] * nums[i], dp_min[i-1] * nums[i]
            else:
                mi, ma = dp_min[i-1] * nums[i], dp_max[i-1] * nums[i]
            mi = min(mi, nums[i]) # 要把单独自己一个元素和与左边连接起来这两种情况相比较
            ma = max(ma, nums[i])
            dp_min[i] = mi
            dp_max[i] = ma
            #res = max(ma, res)
        return max(dp_max[:])
