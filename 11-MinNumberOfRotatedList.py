# -*- coding:utf-8 -*-

##把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
# 剑指Offer 面试题11


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray[0] < rotateArray[-1]: return rotateArray[0]
        index_left = 0
        index_right = len(rotateArray) - 1
        while index_right - index_left > 1:
            mid = (index_left + index_right) // 2
            ## 当三者相等的时候，需要顺序查找才能确认最小值
            if rotateArray[index_right] == rotateArray[mid] == rotateArray[index_left]:
                i = index_left
                while rotateArray[i] < rotateArray[i+1]:
                    i += 1
                return rotateArray[i+1]
            ## 二分查找，移动两个指针，当左指针在右指针左边一个位置，右指针指向的位置就是最小值
            if rotateArray[index_left] <= rotateArray[mid]:
                index_left = mid
            if rotateArray[index_right] >= rotateArray[mid]:
                index_right = mid
        return rotateArray[index_right]


if __name__ == "__main__":
    s = Solution()
    print s.minNumberInRotateArray([3,4,5,1,2])
    print s.minNumberInRotateArray([1, 0, 1, 1, 1])
    print s.minNumberInRotateArray([1, 1, 0, 1, 1])
    print s.minNumberInRotateArray([1, 2, 3, 4, 5])