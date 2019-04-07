#-*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        up = 0
        root = head = ListNode(0)
        while l1 or l2 or up:
            l1, val1 = [l1.next, l1.val] if l1 else [0, 0]
            l2, val2 = [l2.next, l2.val] if l2 else [0, 0]
            up,down = divmod(val1+val2+up, 10)
            head.next = ListNode(down)
            head = head.next
        return root.next




if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    res = solution.addTwoNumbers(l1, l2)
    while(True):
        print res.val
        if res.next == None:
            break
        else:
            res = res.next