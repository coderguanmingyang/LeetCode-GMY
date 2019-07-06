# -*- coding:utf-8 -*-
'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''
## Topic: Merge Sort and Linked List
## Anlysis: 时间复杂度在O(nlogN)的排序算法是快速排序，堆排序，归并排序。
# 但是快排的最坏时间复杂度是O(n^2),平均时间复杂度为O(nlogn)，所以不考虑快速排序。
# 而堆排序太繁琐了。生硬地排除了。对于数组来说占用的空间复杂度为O(1),O(n),O(n)。
# 但是对于链表来说使用归并排序占用空间为O(1).


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
        mid.next = None # Important! Break the chain!

        return self.merge(self.sortList(left), self.sortList(right))

    # Return the middle node
    def partition(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Merge two sorted Linked List
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


def appendNode(head, x):
    p = head
    while(p.next != None):
        p = p.next
    newNode = ListNode(x)
    p.next = newNode

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    appendNode(head, -1)
    appendNode(head, 2)
    appendNode(head, 4)
    appendNode(head, 3)
    print s.sortList(head)