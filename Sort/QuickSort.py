# -*- coding:utf-8 -*-
# https://blog.csdn.net/qq_35654080/article/details/82701237

def quick_sort_standord(array, low, high):
    if low < high:
        key_index = partion(array, low, high)
        quick_sort_standord(array, low, key_index)
        quick_sort_standord(array, key_index + 1, high)

# 保证基准左边小于右边
def partion(array, low, high):
    key = array[low] # 选择数组第一个数字作为基准
    while low < high:
        while low < high and array[high] >= key:
            high -= 1 # 从右边扫描找到小于基准的index
        if low < high:
            array[low] = array[high] # 将小于基准的数换到左边去

        while low < high and array[low] < key:
            low += 1 # 从左边扫描找到大于基准的index
        if low < high:
            array[high] = array[low] #将大于基准的数换到了右边

    array[low] = key # 当 low 和 high到一起，把之前的基准放进去， 即完成了一次划分
    return low # 返回基准所在索引


if __name__ == '__main__':
    array2 = [9, 3, 2, 1, 4, 6, 7, 0, 5]

    print(array2)
    quick_sort_standord(array2, 0, len(array2) - 1)
    print(array2)
