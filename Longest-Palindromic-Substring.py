class Solution(object):
    def longestPalindrome_TLE(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        maxStr = ""
        if len(s) == 1: return s
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                subStr = s[i:j]
                subStr_re = reversed(list(subStr))
                if list(subStr) == list(subStr_re):
                    if j - i > maxLen:
                        maxStr = subStr
                        maxLen = j - i
                    #elif j - i == maxLen:
                    #    maxStr.append(subStr)
        return maxStr

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        if len(s) == 1: return s
        for i in range(len(s)):
            len1 = expandCenter(s, i, i)
            len2 = expandCenter(s, i, i+1)
            len_max = max(len1, len2)
            if (len_max > end - start):
                start = i - (len_max - 1)/2
                end = i + len_max / 2
        return s[start:end+1]

def expandCenter(s, left, right):
    L = left
    R = right
    while(L >= 0 and R < len(s) and s[L] == s[R]):
        L = L - 1
        R = R + 1

    return R - L - 1

if __name__=="__main__":
    S = Solution()
    print S.longestPalindrome('bbbbb')
    print S.longestPalindrome('')
    print S.longestPalindrome('a')
    print S.longestPalindrome("bb")
    print S.longestPalindrome('babad')
    print S.longestPalindrome('abbabbbhfkshfkabbabbb')
    print S.longestPalindrome('babcbabzxxzba')

