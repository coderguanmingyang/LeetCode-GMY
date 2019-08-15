# -*- coding:utf-8 -*-

class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if 0 < int(s[0]) <= 9 else 0

        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1:i]) <= 9:
                dp[i] += dp[i - 1]
            if s[i - 2:i][0] != '0' and int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]

s = Solution()
s.numDecodings("00")