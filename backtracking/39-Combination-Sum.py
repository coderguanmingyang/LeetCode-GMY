# -*- coding:utf-8 -*-
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path, res = [], []
        def dfs(num, path, res):
            if num == 0:
                if sorted(path) not in res: ##防止元素顺序不一样的path加进去
                    res.append(sorted(path[:]))
                return
            for i in candidates:
                if num - i >= 0:
                    path.append(i)
                    dfs(num - i, path, res)
                    path.pop()

        dfs(target, path, res)
        return res

# 此方法通过设立开始的index 来避免集合重复， 这样时间效率会更高一些
class Solutionv2:
    def combinationSum(self, candidates, target):
        size = len(candidates)
        if size == 0:
            return []

        res = []
        self.__dfs(candidates, size, 0, [], target, res)
        return res

    def __dfs(self, candidates, size, start, path, residue, res):
        if residue < 0:
            return
        if residue == 0:
            res.append(path[:])
            return

        for index in range(start, size):
            path.append(candidates[index])
            # 注意：因为数字可以无限制重复被选取，因此起始位置还是自己
            self.__dfs(candidates, size, index, path, residue - candidates[index], res)
            path.pop()




if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,5], 8)