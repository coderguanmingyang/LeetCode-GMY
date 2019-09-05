# -*- coding:utf-8 -*-
'''

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''
## 动态规划：
# 当前正整数n的结果对应于n去掉一个完全平方数之后的子问题结果加一，
# 但是去掉哪一个完全平方数才能达到最佳结果呢，这就需要我们自己去进行一个遍历，然后取最小的值即可

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

#队列 [当前和为多少，有几个数相加]，层级为step，同一层级的step都相同，
#所以，当和达到n时，返回层级step即可

class SolutionV2(object):
    def numSquares(self, n):
        ps = [i**2 for i in xrange(1, int(n**0.5) + 1)]
        ps = ps[::-1]
        if n == 0:
            return 1
        used = [False for i in xrange(n + 1)]
        used[0] = True
        Q = [[0, 0]]
        while len(Q) > 0:
            [x, step] = Q.pop(0) ##先进先出
            for y in ps:
                t = x + y
                if t < n and not used[t]:
                    Q.append([t, step + 1])
                    used[t] = True
                elif t == n:
                    return step + 1
        return -1

s = Solution()
print s.numSquares(12)