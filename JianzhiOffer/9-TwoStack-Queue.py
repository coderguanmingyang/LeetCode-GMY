# -*- coding:utf-8 -*-

## 用两个栈来实现一个队列，完成队列的Push和Pop操作。
# 队列中的元素为int类型。
# 剑指Offer 面试题9

class Solution():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, node):
        # write code here
        self.stack1.append(node) #直接添加到stack1， 即为对列尾
    def pop(self):
        # return xx
        if len(self.stack2) != 0: #如果stack2不为空 删除栈头， 即为队列头
            return self.stack2.pop()
        else: #如果stack2为空， 要先把stack1的元素都压入stack2，然后再删除stack2栈头
            while len(self.stack1) != 0:
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return self.stack2.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
s.push(4)
print s.pop()
print s.pop()