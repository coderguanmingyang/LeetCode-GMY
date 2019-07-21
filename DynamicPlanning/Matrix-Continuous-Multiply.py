# -*- coding:utf-8 -*-

#给定n个的矩阵序列，我们希望计算它们的乘积，求最小乘法的次数 （注意：矩阵相乘有交换律）
#对于A1, A2, A3,......,An 这n个矩阵联乘，则他们的维度共包含n+1个数字。
#比如，A1的维度为a1*a2, A2的维度为a2*a3 ......
#设m(1, n)表示从第1个矩阵乘到第n个矩阵相乘的最小次数
#n=1, m(1,1)=0
#n=2, m(1,2)=a1*a2*a3
#n=3时，有两种情况 即 (A1 * (A2 * A3)):  a1*a2*a4 + a2*a3*a4
#                即 ((A1 * A2) * A3): a1*a2*a3 +  a1*a3*a4
# 则，m(1,3)=min(a1*a2*a4 + a2*a3*a4, a1*a2*a3 +  a1*a3*a4)

#子问题划分，假设将该矩阵串分为两个子串，分隔位置为K，那么会得到：
#m(1, n) = m(1, k) + m(k+1, n) + a1*a(k+1)*an
#然后再将k遍历取最小即可
#https://www.jianshu.com/p/02b3b1b81bee



##递归 这里面有好多子问题会重复计算，所以可以用一个二维矩阵来存已经计算过的值
#再优化：仔细分析m(1, n) 要先计算m(1,k)和m(k+1, n),画一个M矩阵，发现整个计算方向是从对角线到右上角
#这样直接循环计算即可
class Solution:
    def method1(self, a, left, right):
        if right == left:
            return 0
        if right - left == 1:
            return a[left-1] * a[left] * a[right]

        min = float('inf')
        for i in range(left, right):
            m_left_right = self.method1(a, left, i) + self.method1(a, i+1, right) + a[left-1] * a[i] * a[right] # 注意a的坐标从0开始
            if m_left_right < min:
                min = m_left_right

        return min

    #加入一个m矩阵记录已经计算的值
    def method2(self, a, m, left, right):

        if m[left][right] != 0: return m[left][right]
        if right == left:
            return 0
        if right - left == 1:
            return a[left-1] * a[left] * a[right]

        min = float('inf')
        for i in range(left, right):
            m_left_i = self.method2(a, m, left, i)
            m_i1_right = self.method2(a, m, i+1, right)
            m_left_right = m_left_i + m_i1_right + a[left-1] * a[i] * a[right] # 注意a的坐标从0开始
            if m_left_right < min:
                min = m_left_right
        m[left][right] = min
        #print m
        return m[left][right]



if __name__ == "__main__":
    s = Solution()
    a = [10,20,30,40, 50,60]
    m = [[0 for i in range(len(a))] for i in range(len(a))]
    print s.method1(a, 1, 5)
    print s.method2(a, m, 1, 5)