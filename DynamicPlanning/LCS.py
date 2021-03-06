# -*- coding:utf-8 -*-
'''
https://blog.csdn.net/ggdhs/article/details/90713154
最长公共子串 and 最长公共子序列
子问题res[i][j] 为截止到字符A的第i个字符和截止到字符串B的第j个字符的最长公共子序列（子串）
'''
'''
最长公共子串（连续）
'''
def LCstring(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    result = 0
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
                result = max(result,res[i][j])
    return result
print(LCstring("helloworld","loop"))
'''
最长公共子序列（不连续）
'''
def LCS(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
            else:
                res[i][j] = max(res[i-1][j],res[i][j-1])
    return res,res[-1][-1]
print(LCS("helloworld","loop"))

