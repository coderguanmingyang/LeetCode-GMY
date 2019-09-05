# -*- coding:utf-8 -*-
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9
的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

'''
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        counter = collections.Counter(numbers)
        for i in counter:
            if counter[i] > len(numbers)/2:
                return i
        return 0

class SolutionV2:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        # 从左向右扫一遍，如果count>0 才有可能有大于一半的数字
        checkNum = numbers[0]
        count = 1
        for n in numbers[1:]:
            if n == checkNum or count == 0:
                count += 1
                checkNum = n
            else:
                count -= 1
        # 验证部分
        if count > 0:
            count = 0
            for n in numbers:
                if n == checkNum:
                    count += 1
            return checkNum if count * 2 > len(numbers) else 0
        else:
            return 0

S = SolutionV2()
print S.MoreThanHalfNum_Solution([1,2,3,4,1,2,1,1,3,1,6,7,8,1,1,1,1])