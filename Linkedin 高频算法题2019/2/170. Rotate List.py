class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if head is None:
            return head

        size = self.getSize(head)
        k = k % (size - 1)

        if k == 0:
            return head

        tempHead = head
        kTh = head
        for _ in range(k):
            kTh = kTh.next

        while kTh.next is not None:
            head = head.next
            kTh = kTh.next

        newHead = head.next
        head.next = None
        kTh.next = tempHead

        return newHead

    def getSize(self, head):
        size = 1
        while head is not None:
            size += 1
            head = head.next
        return size
