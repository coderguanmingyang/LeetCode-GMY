# -*- coding:utf-8
'''

给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

'''
## 将start进行排序，然后扫描一遍就可以了

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        left = []
        right = []
        res = []
        if len(intervals) == 0:
            return []
        for i in intervals:
            left.append(i[0])
            right.append(i[1])
        intervals_zip = zip(left, right)
        intervals_zip.sort()
        temp = list(intervals_zip[0])
        for i in range(1, len(intervals_zip)):
            if temp[1] >= intervals_zip[i][0]:
                temp[1] = max(temp[1],intervals_zip[i][1])
            else:
                res.append(temp)
                temp = list(intervals_zip[i])
        res.append(temp)
        return res

s = Solution()
print s.merge([[1,3],[2,6],[8,10],[15,18]])
print s.merge([[1,4],[4,5]])
print s.merge([])
print s.merge([[1,2],[2,3],[4,5],[5,6]])
