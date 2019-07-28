# -*- coding:utf-8 -*-
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):
    def subsetsV1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        for num in nums:
            copy_of_res = res[:] #切片操作 只深拷贝list第一层
            for temp in copy_of_res:
                x = temp[:]
                x.append(num)
                if sorted(x) not in res:
                    res.append(sorted(x))
        return res

    def subsetsV2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results

    def search(self, nums, S, index):
        if index == len(nums): #当index到最右边了，就把当前的list加进去
            if S not in self.results: #当出现重复了，就不放进去
                self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1) #加入当前index指向的元素
        self.search(nums, S, index + 1) #不加入当前index指向的元素，index一直往右移

if __name__ == "__main__":
    s = Solution()
    print s.subsetsV1([4,4,4,1,4])