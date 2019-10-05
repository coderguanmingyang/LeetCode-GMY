# -*- coding:utf-8 -*-
'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

'''
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    pre_num = stack.pop()
                    stack.append(pre_num * num)
                elif pre_op == '/':
                    pre_num = stack.pop()
                    if pre_num < 0:
                        stack.append(- (abs(pre_num) / num))
                    else:
                        stack.append(pre_num / num)
                pre_op = each
                num = 0
        return sum(stack)
print -100 // 9
print -100 / 9
print -100 / 10
print -100 // 10
s = Solution()
print s.calculate("14-3/2")
print s.calculate("10000-1000/10+100*1")