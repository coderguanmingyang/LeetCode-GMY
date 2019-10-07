# -*- coding:utf-8 -*-
'''
给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。
如果不存在任意一个符合要求的子数组，则返回 0。

注意:
 nums 数组的总和是一定在 32 位有符号整数范围之内的。

示例 1:

输入: nums = [1, -1, 5, -2, 3], k = 3
输出: 4
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
示例 2:

输入: nums = [-2, -1, 2, 1], k = 1
输出: 2
解释: 子数组 [-1, 2] 和等于 1，且长度最长。
进阶:
你能使时间复杂度在 O(n) 内完成此题吗?

'''
import collections
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_tab = collections.defaultdict(list)
        preSum = 0
        hash_tab[0].append(-1) #加入一个位置为-1的preSum
        max_len = 0
        for i, num in enumerate(nums):
            preSum += num
            if len(hash_tab[preSum-k]) !=0:
                if i - hash_tab[preSum-k][0] > max_len:
                    max_len = i - hash_tab[preSum-k][0]
            hash_tab[preSum].append(i)
        return max_len

nums = [1, -1, 5, -2, 3]
k = 3
s = Solution()
print s.maxSubArrayLen(nums, k)