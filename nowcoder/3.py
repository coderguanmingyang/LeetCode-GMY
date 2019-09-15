# -*- coding:utf-8
'''
[编程题]小Q的歌单
时间限制：1秒

空间限制：32768K

小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，现在小Q想用这些歌组成一个总长度正好为K的歌单，每首歌最多只能在歌单中出现一次，在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
接下来的一行包含四个正整数，分别表示歌的第一种长度A(A<=10)和数量X(X<=100)以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。保证A不等于B。

输出描述:
输出一个整数,表示组成歌单的方法取模。因为答案可能会很大,输出对1000000007取模的结果。

输入例子1:
5
2 3 3 3

输出例子1:
9
'''

## 因为巧克力不能半块吃，所以在计算数列时要上取整
## 采用二分法来试验结果
from scipy.special import comb, perm

k = int(raw_input().strip())
line = map(int, raw_input().strip().split())
a, x, b, y = line[0], line[1], line[2], line[3]
res = []
tmp = 0
while (tmp <= x):
    if (k - tmp * a) % b == 0 and  (k - tmp * a) / b <= y:
        res.append((tmp, (k - tmp * a) / b))
    tmp += 1
total = 0
for i in res:
    total += comb(x, i[0]) * comb(y, i[1])
print  int(total) % 1000000007

