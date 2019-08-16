# -*- coding:utf-8 -*-
'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

'''
## 核心思想是当余数出现循环的时候，对应的商也会循环。 用一个hashtable来存出现的余数
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        if numerator / denominator < 0:
            res += "-"

        if numerator % denominator == 0:
            return str(numerator / denominator)

        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator / denominator)
        res += "."
        numerator %= denominator
        i = len(res)
        table = {}
        while numerator != 0:
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res += str(numerator / denominator)
            numerator %= denominator
            i += 1
        return res