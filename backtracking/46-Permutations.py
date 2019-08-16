# -*- coding:utf-8 -*-
'''

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''



class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        length = len(nums)

        def dfs(nums, path):
            if len(path) == length:
                res.append(path[:])
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    dfs(nums, path)
                    path.remove(i)
        dfs(nums, path)
        return  res

if __name__ == "__main__":
    s = Solution()
    print s.permute([])
    print s.permute([1])
    print s.permute([1,2])
    print s.permute([1,2,3])