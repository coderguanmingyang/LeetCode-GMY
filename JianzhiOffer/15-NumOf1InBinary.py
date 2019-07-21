# -*- coding:utf-8 -*-

#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 剑指Offer 面试题15


class Solution:
    ##此函数无效
    def NumberOf1(self, n):
        # write code here
        count = 0
        tmp = 1
        while tmp !=0:
            if n & tmp:
                count += 1
            tmp = int(tmp << 1)
            print bin(tmp)
        return count

    def NumberOf1V2(self, n):
        # write code here
        count = 0
        if n < 0:
            print bin(n)
            print n
            n = n & 0xffffffff #转换成补码
            print bin(n)
            print n
        while n:
            count += 1
            n = n & (n - 1)
        return count


if __name__ == "__main__":
    s = Solution()
    #matrix = [['a', 'b'], ['t', 'g']]
    print s.NumberOf1V2(-31000)