# -*- coding:utf-8 -*-
'''

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”
单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

'''
#Solution: dfs + 回溯

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, index, flag):
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            if (i, j) in flag:
                return False
            if board[i][j] == word[index]:
                if index == len(word) - 1:
                    return True
                else:
                    flag.append((i, j))
                    for dx, dy in directions:
                        if dfs(i+dx, j+dy, index+1, flag):
                            return True
                    flag.remove((i, j)) # 这个是最重要的回溯步骤
                    return False
            else:
                return False

        for i in range(row):
            for j in range(col):
                flag = []
                if dfs(i, j, 0, flag):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.exist([["a", "a"]], "aaa")
    print s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
    print s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS")