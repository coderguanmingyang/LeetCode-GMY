# -*- coding:utf-8 -*-
'''
现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。
假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。
因为是从词典中获得的，所以该单词列表内的单词已经 按这门新语言的字母顺序进行了排序。
您需要根据这个输入的列表，还原出此语言中已知的字母顺序。
示例 1：
输入:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
输出: "wertf"

示例 2：
输入:
[
  "z",
  "x"
]
输出: "zx"

示例 3：
输入:
[
  "z",
  "x",
  "z"
]
输出: "" 

解释: 此顺序是非法的，因此返回 ""。
注意：

你可以默认输入的全部都是小写字母
假如，a 的字母排列顺序优先于 b，那么在给定的词典当中 a 定先出现在 b 前面
若给定的顺序是不合法的，则返回空字符串即可
若存在多种可能的合法字母顺序，请返回其中任意一种顺序即可

'''

# solution: 拓扑排序
# 只不过有很多边界条件需要考虑
# 这里边只要出现非法情况就输出“”
# 其它要把所有字符输出来（这也是一种可能的排序）
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 1:
            return words[0]
        nextNode = collections.defaultdict(list)
        in_degree = {}
        self.nodeset = set()
        preword = words[0]
        for i in range(1, len(words)):
            ans = self.cmp(preword, words[i])
            if len(ans) == 2:
                nextNode[ans[0]].append(ans[1])
                if in_degree.has_key(ans[1]):
                    in_degree[ans[1]] += 1
                else:
                    in_degree[ans[1]] = 1
            preword = words[i]

        # 使用列表作为队列并将入度为0的添加到队列中
        Q = []
        for key in nextNode.keys():
            if not in_degree.has_key(key):
                Q.append(key)
        # 非法情况1：没有入度为0的点 但是却有个图，那就是环
        if len(Q) == 0 and len(nextNode) !=0:
            return ""

        res = ""
        # 当队列中有元素时执行
        while Q:
            # 从队列首部取出元素
            u = Q.pop()
            # 将取出的元素存入结果中
            res += u
            # 移除与取出元素相关的指向，即将所有与取出元素相关的元素的入度减少1
            for v in nextNode[u]:
                in_degree[v] -= 1
                # 若被移除指向的元素入度为0，则添加到队列中
                if in_degree[v] == 0:
                    Q.append(v)

        for item in in_degree.items():
            # 非法情况2：还是有环出现
            if item[1] != 0:
                return ""

        for word in self.nodeset:
            if word not in res:
                res += word
        return res

    def cmp(self, word1, word2):

        for i in range(len(word1)):
            self.nodeset.add(word1[i])
        for i in range(len(word2)):
            self.nodeset.add(word2[i])
        i = 0
        while i < min(len(word1), len(word2)):
            if word1[i] == word2[i]:
                i += 1
                continue
            return [word1[i], word2[i]]
        return []

s = Solution()
print s.alienOrder(["wnlb"])
print s.alienOrder(["wrt","wrf","er","ett","rftt"])
print s.alienOrder(["z","z"])
print s.alienOrder(["zy","zx"])
print s.alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]) # ""







