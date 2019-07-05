'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        p1 = p2 = head
        for i in range(n):
            p1 = p1.next

        ## Delete the head node
        if p1 == None:
            return head.next

        while(p1.next != None):
            p1 = p1.next
            p2 = p2.next
        ## Delete the node
        if n == 1: # If delete the last node, set the last node is None
            p2.next = None
        else:
            p2.next = p2.next.next

        return head

def appendNode(head, x):
    p = head
    while(p.next != None):
        p = p.next

    newNode = ListNode(x)
    p.next = newNode


if __name__ == "__main__":
    head = ListNode(1)

    s =Solution()
    print s.removeNthFromEnd(head, 1)

    appendNode(head, 2)
    appendNode(head, 3)
    appendNode(head, 4)
    appendNode(head, 5)

    s =Solution()
    s.removeNthFromEnd(head, 2)
