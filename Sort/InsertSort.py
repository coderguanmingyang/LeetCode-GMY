# -*- coding:utf-8 -*-

# 每次将待排序元素插入前面的有序区间，插入过程是逐步比较，找到合适位置
def SimpleInsertSort(data_list):

    count=0 #统计循环次数
    length = len(data_list)
    for i in range(1, length): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
        tmp = data_list[i] #待插入的数据
        j = i
        while j > 0: #从已排序区间查找插入位置
            count +=1
            if tmp < data_list[j-1]:
                data_list[j] = data_list[j-1]  #元素向后移动，腾出插入位置
            else:
                break
            j -= 1
        data_list[j] = tmp #插入操作
        print(data_list)
    print("总循环次数为 {}".format(count))
    return data_list


# 有序区间本身就是一个可以节省时间的key，可以利用二分查找来减少长有序序列的比较
def BinaryInsertSort(data_list):

    def binarySearch(SortedList, data):

        left = 0
        right = len(SortedList)
        if data <= SortedList[0]: return 0
        if data >= SortedList[right-1]: return right
        insert_index = 0
        while left < right - 1 :
            mid = (left + right)//2
            if data < SortedList[mid]:
                right = mid
                insert_index = right # 如果小于中间值，应该插在当前位置
            else:
                left = mid
                insert_index = left + 1 # 如果大于或等于该值，应该插在当前位置后面
        return insert_index

    length = len(data_list)
    for i in range(1, length): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
        tmp = data_list[i] #待插入的数据

        insert_index = binarySearch(data_list[0:i], tmp)
        print insert_index
        for k in reversed(range(insert_index+1, i+1)):
            data_list[k] = data_list[k-1]
        data_list[insert_index] = tmp #插入操作
        print(data_list)

    return data_list


if __name__ == "__main__":
    data = [9, 3, 2, 1, 4, 6, 7, 0, 5]
    BinaryInsertSort(data)