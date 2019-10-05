# -*- coding:utf-8 -*-
'''
[最小覆盖子串]

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

'''

class Solution:
    def minWindow(self, s, t):
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        left = 0
        right = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while right < len(s):
            if lookup[s[right]] > 0:
                counter -= 1
            lookup[s[right]] -= 1
            right += 1
            # 当counter=0，则证明当前子串满足覆盖，接下来进行left右移
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                if lookup[s[left]] == 0:
                    counter += 1
                lookup[s[left]] += 1
                left += 1
        return res

s = Solution()
print s.minWindow("eecadacbeabc", "abcc")