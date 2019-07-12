# -*- coding:utf-8 -*-
'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''
## Solution: 遍历长度为10的substring,将其作为key建立hashtable
## 计数出现次数
##

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10: return []
        #if len(s) == 10: return [s]
        import collections
        ans = collections.Counter()
        for i in range(len(s)-9):
            substring = s[i:i+10]
            ans[substring] += 1

        return [key for key, value in ans.iteritems() if value > 1]


if __name__ == "__main__":
    s = Solution()
    print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print s.findRepeatedDnaSequences("AAAAAAAAAA")
