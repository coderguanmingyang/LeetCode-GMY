# -*- coding:utf-8 -*-
'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some
 characters of the given string. If there are more than one possible results, return the longest word with the smallest
 lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

'''

## Solution:
# 暴力解法， 逐步验证是否为最长子串，当待验证子串长度小于当前最长子串， 则直接skip

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res_str = ''
        for s_test in d:
            if len(s_test) < len(res_str):
                continue
            if self.isMatchSubString(s, s_test):
                if len(s_test) > len(res_str):
                    res_str = s_test
                elif len(s_test) == len(res_str) and s_test < res_str:
                    res_str = s_test
        return res_str


    ## s2 is the sub string of s1 ?
    def isMatchSubString(self, s1, s2):
        if len(s2) > len(s1):
            return False
        j = 0
        i = 0
        while i < len(s2) and j < len(s1):
            if s2[i] == s1[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s2): return True
        else: return False



if __name__ == "__main__":

    so = Solution()
    s = "abpcplea"
    d = ["a", "b", "c", 'apple', 'abcpl']
    print sorted(d)
    print so.findLongestWord(s, d)