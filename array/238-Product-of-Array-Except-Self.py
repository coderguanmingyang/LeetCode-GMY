# -*- coding:utf-8 -*-
'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中
output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

'''
# 从左边乘积 从右边乘积
# 然后将中间的扣掉

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [nums[0]]
        right = [nums[-1]]



        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i])

        for j in range(len(nums)-2, -1, -1):
            right.append(right[-1] * nums[j])

        res = []
        for i in range(0, len(nums)):
            if i == 0:
                res.append(right[len(nums)-1-1])
            elif i == len(nums)-1:
                res.append(left[len(nums)-1-1])
            else:
                res.append(left[i-1] * right[len(nums)-i-2])
        return res

if __name__ == "__main__":
    s = Solution()
    print s.productExceptSelf([1,2,3,4])