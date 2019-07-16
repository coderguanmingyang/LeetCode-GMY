# -*- coding:utf-8 -*-

##地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
# 因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
# 剑指Offer 面试题13


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [False for i in range(rows * cols)]
        return self.movingCountCore(threshold, rows, 0, cols, 0, visited)

    def movingCountCore(self, threshold, rows, row, cols, col, visited): # 计算当前节点可以到达的格子数
        count = 0
        if self.check(row, col, threshold) and row >=0 and row < rows and col >= 0 and col < cols and not visited[row * cols + col]:
            visited[row * cols + col] = True
            count = 1 + \
                self.movingCountCore(threshold, rows, row - 1, cols, col, visited) + \
                self.movingCountCore(threshold, rows, row, cols, col - 1, visited) + \
                self.movingCountCore(threshold, rows, row + 1, cols, col, visited) + \
                self.movingCountCore(threshold, rows, row, cols, col + 1, visited)
        return count



    def check(self, row, col, k):
        sum = self.getDigit(row) + self.getDigit(col)
        if sum > k: return False
        else: return True

    def getDigit(self, number):
        sum = 0
        while number > 0:
             sum += number % 10
             number = number/10
        return sum



if __name__ == "__main__":
    s = Solution()
    #matrix = [['a', 'b'], ['t', 'g']]
    print s.movingCount(5, 10, 10)