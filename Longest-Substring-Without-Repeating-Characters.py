import os



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        maxLen = 0
        i = 0
        j = 1
        while(i < len(s)):
            subStr = s[i:j]
            if s[j] in subStr:
                maxLen = max(maxLen, j - i)
                index = subStr.index(s[j])
                i = i + index + 1
            j = j + 1
            if j == len(s):
                maxLen = max(maxLen, j - i)
                break
            if maxLen >= len(s) - i:
                break

        return maxLen

if __name__=="__main__":
    S = Solution()
    print S.lengthOfLongestSubstring('bbbbb')
    print S.lengthOfLongestSubstring('pwwkew')
    print S.lengthOfLongestSubstring('abcabcbb')
    print S.lengthOfLongestSubstring('')
    print S.lengthOfLongestSubstring('aa')
    print S.lengthOfLongestSubstring('a')
    print S.lengthOfLongestSubstring('ab')
