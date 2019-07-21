# -*- coding:utf-8 -*-

## 用两个队列来实现一个栈，完成队列的Push和Pop操作。
# 队列中的元素为int类型。
# 剑指Offer 面试题9题变形
import queue

class Solution():
    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()


    def push(self, node):
        # write code here
        if not self.queue1.empty():
            self.queue1.put(node)
        else:
            self.queue2.put(node)

    def pop(self):

        if not self.queue1.empty():
            while self.queue1.qsize() > 1:
                temp = self.queue1.get()
                self.queue2.put(temp)
            return self.queue1.get()

        elif not self.queue2.empty():
            while self.queue2.qsize() > 1:
                temp = self.queue2.get()
                self.queue1.put(temp)
            return self.queue2.get()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
s.push(4)
print s.pop()
print s.pop()