# -*- coding:utf-8 -*-

## 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
## n<=39
# 剑指Offer 面试题10


class Solution:
    ##TLE
    def Fibonacci(self, n):
        # write code here
        if n == 0: return 0
        if n == 1: return 1
        if n > 1: return (self.Fibonacci(n-1) + self.Fibonacci(n-2))

    def Fibonacciv2(self, n):

        if n == 0: return 0
        if n == 1: return 1
        minusOne = 0
        minusTwo = 1
        i = 2
        while i <= n:
            ans = minusOne + minusTwo
            minusOne = minusTwo
            minusTwo = ans
            i = i + 1
        return ans


s = Solution()
print s.Fibonacciv2(3)