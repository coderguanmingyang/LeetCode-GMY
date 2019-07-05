'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None
        if k == 0: return head

        ## Get the length
        p = head
        length = 1
        while (p.next != None):
            length += 1
            p = p.next
        if length == 1:
            return head
        ##Set cycle Linked LIst
        p.next = head

        ## Find the new head
        k = k % length
        p = head
        for i in range(length - k):
            p = p.next
        head = p

        ## Set the tail is None
        for i in range(length - 1):
            p = p.next
        p.next = None

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
    print s.rotateRight(head, 1).val

    appendNode(head, 2)
    appendNode(head, 3)
    appendNode(head, 4)
    appendNode(head, 5)

    s =Solution()
    print s.rotateRight(head, 2).val