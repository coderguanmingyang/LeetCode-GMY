# -*- coding:utf-8 -*-
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        self.buildHeap(nums, len(nums))
        for i in range(len(nums)-1, -1, -1):
            max = nums[0]
            nums[0] = nums[i]
            nums[i] = max
            k = k - 1
            if not k:
                return max
            self.adjustHeap(nums, 0, i)

    def buildHeap(self, nums, size):
        for i in range(int(size/2), -1, -1):
            self.adjustHeap(nums, i, size)

    def adjustHeap(self, nums, i, size):
        left = 2 * i + 1
        right = 2 * i + 2
        max_index = i
        if left < size and nums[left] > nums[max_index]:
            max_index = left
        if right < size and nums[right] > nums[max_index]:
            max_index = right
        if max_index != i:
            temp = nums[max_index]
            nums[max_index] = nums[i]
            nums[i] = temp
            self.adjustHeap(nums, max_index, size)


s = Solution()
print s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print s.findKthLargest([3,2], 2)
