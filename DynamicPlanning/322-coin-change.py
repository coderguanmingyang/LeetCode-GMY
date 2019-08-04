# -*- coding:utf-8 -*-
'''
You are given coins of different denominations and a total amount of
money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

'''

class Solution(object):
    ## 自下而上
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

class SolutionV2(object):
    ## 自上而下
    def coinChange(self, coins, amount):
        count = [0 for i in range(amount + 1)] #添加count，就是要减少重复计算
        if amount < 1:
            return 0
        return self.Change(coins, amount, count)

    def Change(self, coins, amount, count):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0: return -1
        if amount == 0: return 0
        if count[amount] != 0: return count[amount]
        cur_min = float("inf")
        for coin in coins:
            res = self.Change(coins, amount - coin, count)
            if res >= 0 and (res + 1) < cur_min:
                cur_min = res + 1
        count[amount] = -1 if cur_min == float("inf") else cur_min
        return count[amount]


if __name__ == "__main__":
    s = SolutionV2()
    print s.coinChange([1,5], 11)