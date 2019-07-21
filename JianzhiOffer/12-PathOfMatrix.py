# -*- coding:utf-8 -*-

##请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
# 每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
# 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
# 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
# 剑指Offer 面试题12


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        pathLength = 0
        visited = [False  for j in range(cols * rows)]
        for i in range(rows):
            for j in range(cols):
                if self.hasPathCore(matrix, rows, i, cols, j, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, row, cols, col, path, pathLength, visited):
        if pathLength == len(path):
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols \
            and (matrix[row * cols + col] == path[pathLength]) and not visited[row * cols + col]:

            pathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, row, cols, col - 1, path, pathLength, visited) or \
            self.hasPathCore(matrix, rows, row - 1, cols, col, path, pathLength, visited) or \
            self.hasPathCore(matrix, rows, row, cols, col + 1, path, pathLength, visited) or \
            self.hasPathCore(matrix, rows, row + 1, cols, col, path, pathLength, visited)

            if not hasPath: ## 回溯到上一节点
                pathLength -= 1
                visited[row * cols + col] = False

        return hasPath


if __name__ == "__main__":
    s = Solution()
    #matrix = [['a', 'b'], ['t', 'g']]
    print s.hasPath("ABCESFCSADEE",3,4,"ABCCED")