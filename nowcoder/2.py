# -*- coding:utf-8
'''
###纸牌游戏

小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，
但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，表示父母出差的天数N(N<=50000)和巧克力
的数量M(N<=M<=100000)。

输出描述:
输出一个数表示小Q第一天最多能吃多少块巧克力。

输入例子1:
3 7

输出例子1:
4

'''

## 因为巧克力不能半块吃，所以在计算数列时要上取整
## 采用二分法来试验结果

def sum(first, n):
    total = 0
    for i in range(n):
        total += first
        first = (first + 1 )/2

    return total

line = raw_input().strip()
a = map(int, line.strip().split())
n, m = a[0], a[1]

low, high = 1, m
while(low <= high):
    mid = (low + high)/2
    sum_try = sum(mid, n)
    if sum_try == m:
        high = mid
        break
    elif sum_try > m:
        high = mid - 1
    elif sum_try < m:
        low = mid + 1
print high

