# -*- coding:utf-8 -*-
'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.

'''
# Solution: Sum[i]表示以i为最有边界的最大连续子数组的和：
# 当sum[i-1] < 0 时，其对nums[i]没有增益，所以sum[i]即为本身
# 当sum[i-1] > 0 时，其对nums[i]有增益，故加上。

# 如果返回最大和子数组，要记得记录临时左指针


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        left_temp = 0
        left_max = 0
        right_max = 0
        sum = [0 for i in xrange(len(nums))]
        sum[0] = nums[0]
        for i in xrange(1, len(nums)):
            if sum[i-1] < 0:
                sum[i] = nums[i]
                left_temp = i
            else:
                sum[i] = sum[i-1] + nums[i]

            if sum[i] > max:
                max = sum[i]
                right_max = i
                left_max = left_temp
        return max, nums[left_max:right_max+1]

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print s.maxSubArray([-2,1,-3,4,-1,2,10,-5,4])
print s.maxSubArray([-2,1,0,4,-1,2,10,-5,4])
print s.maxSubArray([2,1,0,4,1,-2,10, 5,4])
print s.maxSubArray([2,1,2,4,1,-2,-10, 5,4])