# -*- coding:utf-8 -*-
'''
[序列重建]
验证原始的序列 org 是否可以从序列集 seqs 中唯一地重建。序列 org 是 1 到 n 整数的排列，
其中 1 ≤ n ≤ 104。重建是指在序列集 seqs 中构建最短的公共超序列。（即使得所有  seqs 
中的序列都是该最短序列的子序列）。确定是否只可以从 seqs 重建唯一的序列，且该序列就是 org 。

示例 1：
输入：
org: [1,2,3], seqs: [[1,2],[1,3]]
输出：
false
解释：
[1,2,3] 不是可以被重建的唯一的序列，因为 [1,3,2] 也是一个合法的序列。
 
示例 2：
输入：
org: [1,2,3], seqs: [[1,2]]
输出：
false
解释：
可以重建的序列只有 [1,2]。
 
示例 3：
输入：
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
输出：
true
解释：
序列 [1,2], [1,3] 和 [2,3] 可以被唯一地重建为原始的序列 [1,2,3]。
 

示例 4：
输入：
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
输出：
true
'''
# solution1: 拓扑排序
# 未AC
import collections
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        n = len(org)
        in_degrees = {}
        graph = collections.defaultdict(set)
        for seq in seqs:
            if len(seq) == 0:
                continue
            pre = seq[0]
            for j in range(1, len(seq)):
                if seq[j] > n:
                    continue
                if seq[j] not in graph[pre]:
                    graph[pre].add(seq[j])
                    pre = seq[j]
                    if in_degrees.has_key(seq[j]):
                        in_degrees[seq[j]] += 1
                    else:
                        in_degrees[seq[j]] = 1
        Q = []
        seen = []
        for item in in_degrees.keys():
            if item[1] == 0:
                Q.append(item[0])
                seen.append(item[0])

        while len(Q) != 0:
            if len(Q) > 1:
                return False
            pre = Q.pop()
            for i in graph[pre]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    Q.append(i)
                    seen.append(i)
        if len(seen) != n:
            return False
        if list(seen) != org:
            return False
        return True

s = Solution()
#print s.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])
#print s.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]])
#print s.sequenceReconstruction([1],[[],[]])
print s.sequenceReconstruction([5,3,2,4,1],[[5,3,2,4],[4,1],[1],[3],[2,4]])



