# -*- coding:utf-8 -*-
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
# preSum 表示从1~i的和，然后每次都将preSum记录在一个哈希表里，每次判断之前是否出现了
# preSum[j] - presum[i] == k (j > i), 出现了就找到了preSum[i]个符合条件的序列

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum = 0
        hash_table = {}
        hash_table[0] = 1
        res = 0
        for i in nums:
            preSum += i
            if hash_table.has_key(preSum - k):
                res += hash_table[preSum-k]
            if hash_table.has_key(preSum):
                hash_table[preSum] += 1
            else:
                hash_table[preSum] = 1
        return res

s = Solution()
print s.subarraySum([1, 1, 1, -1, 1], 2)