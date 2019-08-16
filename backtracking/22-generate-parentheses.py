# -*- coding:utf-8 -*-
'''
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
# solution:这里面需要满足的最大条件就是 右括号的数量<=左括号的数量<=n
# 一旦不满足就不要把path加进去

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        path = ""

        def dfs(left, right, path):
            if left == n and right == n:
                res.append(path)
                return
            if left >= right and left <= n:
                dfs(left+1, right, path+"(")
                dfs(left, right+1, path+")")


        dfs(0, 0, path)
        return res
if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)