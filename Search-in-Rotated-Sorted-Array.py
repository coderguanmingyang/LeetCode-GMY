'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            if nums[0] <= target:
                for i in range(length):
                    if nums[i] == target: return i
                    if i == length - 1: return  -1
                    if nums[i + 1] < nums[i]: return -1
            else:
                for i in reversed(range(length)):
                    if nums[i] == target: return i
                    if i == 0: return -1
                    if nums[i-1] > nums[i]: return -1



if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    nums_1 = [1, 2, 3, 4, 5, 6, 7]
    nums_2 = []
    nums_3 = [0]
    nums_4 = [3, 0]
    target = 0
    print s.search(nums, target=target)
    print s.search(nums_1, target=target)
    print s.search(nums_2, target)
    print s.search(nums_3, target)
    print s.search(nums_4, target)