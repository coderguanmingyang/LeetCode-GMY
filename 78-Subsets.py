# -*- coding:utf-8 -*-

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
不能重复

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
#V1
#Print 输出
#采用逐个将元素输进去的方法
#[[], [1]]
#[[], [1], [2]]
#[[], [1], [2], [1, 2]]
#[[], [1], [2], [1, 2], [3]]
#[[], [1], [2], [1, 2], [3], [1, 3]]
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3]]
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

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
                res.append(x)
                print res
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
            self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1) #加入当前index指向的元素
        self.search(nums, S, index + 1) #不加入当前index指向的元素，index一直往右移


if __name__ == "__main__":
    s = Solution()
    s.subsetsV2([1, 2, 3])