class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

import heapq

ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None

        dummy = ListNode(0)
        tail = dummy

        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        while heap:
            current = heapq.heappop(heap)

            tail.next = current
            tail = current

            if current.next:
                heapq.heappush(heap, current.next)

        return dummy.next