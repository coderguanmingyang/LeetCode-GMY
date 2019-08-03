# -*- coding:utf-8 -*-
'''

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

#Solution1:用哈希表的方法建里一个key为整数，value为出现个数
#然后用冒泡的方法找出k个最大频数的整数
#小于O((k+1)n)的时间复杂度

#Solution2:用heap排序会更省时

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        import collections
        ans = collections.defaultdict(int)
        for i in nums:
            ans[i] += 1
        for j in range(k):
            max_key = 0
            max_val = 0
            for key, val in ans.items():
                if val > max_val:
                    max_val = val
                    max_key = key
            res.append(max_key)
            del ans[max_key]
        return res

class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        import collections
        ans = collections.Counter(nums)
        import heapq
        return heapq.nlargest(k, ans.keys(), ans.get())

if __name__ == "__main__":
    s = Solution()
    print s.topKFrequent(nums = [1,1,1,2,2,3] , k = 2)
    import heapq
    heapq.nlargest()