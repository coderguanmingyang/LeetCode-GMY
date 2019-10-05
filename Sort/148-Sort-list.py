# -*- coding:utf-8 -*-

'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

'''
#用归并排序来做
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        mid = self.partition(head)
        left = head
        right = mid.next
        mid.next = None  # Important! Break the chain!

        return self.merge(self.sortList(left), self.sortList(right))

    # 快慢指针来分治
    def partition(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, p1, p2):
        m = ListNode(0)
        temp = m
        while p1 and p2:
            if p1.val < p2.val:
                temp.next = p1
                p1 = p1.next
            else:
                temp.next = p2
                p2 = p2.next
            temp = temp.next

        if p1 == None:
            temp.next = p2
        else:
            temp.next = p1

        return m.next
