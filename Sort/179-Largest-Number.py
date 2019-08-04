# -*- coding:utf-8 -*-
'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

'''
## 此问题为排序的变形，即如何判断两个数字字符串的大小是关键，即将将两个字符串
## 变化顺序拼接，

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        total = ""
        nums_str = map(str, nums)
        self.quick_sort_standord(nums_str, 0, len(nums)-1)
        for i in range(len(nums)-1, -1, -1):
            total += nums_str[i]
        if int(total) == 0:
            return "0"
        return total


    def quick_sort_standord(self, array, low, high):
        if low < high:
            key_index = self.partion(array, low, high)
            self.quick_sort_standord(array, low, key_index)
            self.quick_sort_standord(array, key_index + 1, high)

    # 保证基准左边小于右边
    def partion(self, array, low, high):
        key = array[low]  # 选择数组第一个数字作为基准
        while low < high:
            while low < high and self.compare(array[high], key):
                high -= 1  # 从右边扫描找到小于基准的index
            if low < high:
                array[low] = array[high]  # 将小于基准的数换到左边去

            while low < high and not self.compare(array[low], key):
                low += 1  # 从左边扫描找到大于基准的index
            if low < high:
                array[high] = array[low]  # 将大于基准的数换到了右边

        array[low] = key  # 当 low 和 high到一起，把之前的基准放进去， 即完成了一次划分
        return low  # 返回基准所在索引


    def compare(self, str1, str2):
        a_b = str1 + str2
        b_a = str2 + str1
        return a_b >= b_a

s = Solution()
print s.largestNumber([3,30,34,5,9])