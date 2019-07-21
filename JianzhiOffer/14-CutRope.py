# -*- coding:utf-8 -*-

#给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)
#每段绳子的长度记为k[0],k[1],...,k[m].请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
#绳子长度，一个整型数n(n>1)
#n=9 output=27 (3*3*3)
# 剑指Offer 面试题14


class Solution:
    ##动态规划
    def CutRope(self, n):
        if n == 1: return None
        elif n == 2: return 1
        elif n == 3: return 2
        else:
            products = [0 for i in range(n + 1)]
            products[1] = 1
            products[2] = 2
            products[3] = 3

            for i in range (4, n+1):
                if i != n:
                    max = i #该段绳子不分割
                else:
                    max = 0 #当整条绳子时，不能不分割（m>1）
                for j in range(1, i/2 +1):
                    if max < products[j] * products[i-j]:
                        max = products[j] * products[i-j]
                products[i] = max
                #print max


        return products[n]


    ## 贪心算法
    # 尽可能地多切割出3， 当余数为1，应该把最后的1放到3里面形成一个4
    def CutRopeV2(self, n):
        if n == 1: return None
        elif n == 2: return 1
        elif n == 3: return 2
        elif n == 4: return 4
        else:
            numOf3 = n / 3
            if n % 3 == 0: return pow(3, numOf3)
            elif n % 3 == 1: return pow(3, numOf3-1) * 4
            else: return pow(3, numOf3) * 2


if __name__ == "__main__":
    s = Solution()
    #matrix = [['a', 'b'], ['t', 'g']]
    print s.CutRope(11)