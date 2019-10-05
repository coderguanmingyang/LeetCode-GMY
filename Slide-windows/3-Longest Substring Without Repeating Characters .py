# -*- coding:utf-8 -*-
'''
【不含重复字母最长子串】（连续）
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
#这道题主要用到思路是：滑动窗口
#什么是滑动窗口？
#其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，
#当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
#如何移动？
#我们只要把队列的左边的元素移出就行了，直到满足题目要求！
#一直维持这样的队列，找出队列出现最长的长度时候，求出解！
#时间复杂度：O(n)
import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Q = set()
        max_len = 0
        cur_len = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in Q:
                Q.add(s[i])
                cur_len += 1
            else:
                while s[i] in Q:
                    Q.remove(s[left])
                    left += 1
                    cur_len -= 1
                Q.add(s[i])
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len

# 滑动窗口+哈希表
# 哈希表里边存的是该字母出现的位置
# 如果 s[j] 在[i,j) 范围内有与 j' 重复的字符，我们不需要逐渐增加i 。
# 我们可以直接跳过[i,j′] 范围内的所有元素，并将 i 变为 j'+1
class SolutionV2(object):
    def lengthOfLongestSubstring(self, s):
        hashMap = {}
        left = 0
        max_len = 0
        for i in range(len(s)):
            # 出现了哈希表里边有的字母，首先计算当前不重复子串的长度，
            # 和最大长度比较，然后就是要将左边界提前到重复字母右边一个位置
            if hashMap.has_key(s[i]) and hashMap[s[i]] >= left:
                cur_len = i - left
                max_len = max(max_len, cur_len)
                left = hashMap[s[i]] + 1
                hashMap[s[i]] = i
            else:
                hashMap[s[i]] = i
        cur_len = len(s) - left
        max_len = max(max_len, cur_len)
        return max_len

s = SolutionV2()
print s.lengthOfLongestSubstring("abcabcbb")
