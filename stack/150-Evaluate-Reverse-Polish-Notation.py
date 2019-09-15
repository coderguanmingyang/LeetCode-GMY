# -*- coding:utf-8 -*-
'''

根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
## 坑：保留整数部分
## python中， '/' 两个整数相除 下取整
## 还有就是正负不同 做除法也不同


import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                a, b = stack.pop(), stack.pop()
                res = b + i + a
                res = eval(res) if i != '/' else int(math.modf(float(b) / float(a))[1])
                res = str((res)) #整数部分保留整数部
                stack.append(res)
            else:
                stack.append(i)
        return int(stack[-1])

s = Solution()
print s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])

print(5/9)
print(5//9)
print(5%9)
print(5.0/-9.0)
print(5.0//-9.0)
print(5.0%-9.0)