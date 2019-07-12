# -*- coding:utf-8 -*-
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''

##Solution: 本质上是将组成字母相同的string成组输出，那么将包含字母的情况作为key
##建立hash table，来分组就能实现这个功能，key有两种方式，一个是包含字母的tuple；
##另一个是用字母出现次数的tuple。

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            key = [0] * 26
            for i in s:
                key[ord(i) - ord('a')] += 1
            ans[tuple(key)].append(s)
        return ans.values()


if __name__ == "__main__":
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])