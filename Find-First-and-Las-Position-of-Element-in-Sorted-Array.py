'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        else:
            index = self.BinarySearch(nums, target, 0, len(nums)-1)
            if index == -1:
                return [-1, -1]
            index_left = index
            index_right = index
            while (index_left - 1 >= 0 ):
                if nums[index_left - 1] == target:
                    index_left -= 1
                else: break

            while (index_right + 1 < len(nums) ):
                if nums[index_right + 1] == target:
                    index_right += 1
                else: break
            return [index_left, index_right]

    def BinarySearch(self, nums, target, start, end):
        if start > end :
            return -1
        mid = (start + end) // 2

        if nums[mid] == target: return mid
        elif nums[mid] < target: return self.BinarySearch(nums, target, mid + 1, end)
        elif nums[mid] > target: return self.BinarySearch(nums, target, start, mid - 1)


if __name__ == "__main__":
    s = Solution()
    nums = [5,7,7,8,8,10]
    target = 100
    print s.searchRange(nums, target)