# -*- coding:utf-8 -*-
'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# dp[i]代表字符串s从开始到i这个位置是不是可分
# 可知当 dp[i-j] == True and s[i:j] in worddict 则 dp[i] = True

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        point = [0]
        for i in range(1, len(s)+1):
            for j in reversed(point):
                sub_str = s[j:i]
                if sub_str in wordDict:
                    point.append(i)
                    dp[i] = True
                    break
        return dp[len(s)]

if __name__ == "__main__":
    s = Solution()
    print s.wordBreak("leetcode" ,["leet","code"])
