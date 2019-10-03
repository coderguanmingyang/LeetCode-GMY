# -*- coding:utf-8 -*-
'''
最小编辑距离
Levenshtein Distance，是编辑距离的一种。指两个字符串之间，由一个转成另一个所需的最少编辑次数。
允许的编辑操作包括【替换】、【插入】和【删除】。

例如将单词kitten转成sitting：

sitten（k→s）
sittin（e→i）
sitting（none→g）
在DNA序列分析、拼写检查、语音辨识、抄袭侦测等方面都有应用。

[Solution]
序列A：GGATCGA
序列B：GAATTCAGTTA

求这两个序列的编辑距离。

Len(A)=7
Len(B)=11

对于 1<=i<=7，1<=j<=11 有：

若 Ai = Bj，LD(i，j) = LD(i-1，j-1)
若 Ai ≠ Bj，LD(i，j) = Min(LD(i-1，j-1)，(LD(i，j-1)，(LD(i-1，j)) + 1
如果两个序列最后一个位点相同，这两个序列的编辑距离和分别去掉最后一个位点的编辑距离相等；
如果两个序列最后一个位点不同，这两个序列的编辑距离是三种可能性最小值加一个编辑距离。

即来填写以下这个表
     G  G  A  T  C  G  A
     1  2  3  4  5  6  7
G 1
A 2
A 3
T 4
T 5
C 6
A 7
G 8
T 9
T 10
A 11
'''


def ld(str1, str2):
    length1, lenght2 = len(str1), len(str2)

    # 初始化矩阵
    matrix = [[0] * (lenght2+1) for i in range(length1+1)]
    matrix[0][0] = 0
    # 当 i 或者 j 为0 时， 则最小次数为另一个字符串的长度
    for i in range(1, length1+1):
        matrix[i][0] = matrix[i - 1][0] + 1

    for j in range(1, lenght2+1):
        matrix[0][j] = matrix[0][j - 1] + 1

    # 动态规划计算ld值
    for i in range(1, length1+1):
        for j in range(1, lenght2+1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1

    return matrix[length1][lenght2]


str1 = 'GAATTCAGTTA'
str2 = 'GGATCGA'
print(ld(str1, str2))
