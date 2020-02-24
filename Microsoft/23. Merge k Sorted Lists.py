from heapq import heappop
from heapq import heappush

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

ListNode.__lt__ = lambda x, y: x.val < y.val

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if not lists:
            return None

        heap = []

        for head in lists:
            if head:
                heappush(heap, head)

        dummy = ListNode(0)
        node = dummy
        while heap:
            curt = heappop(heap)

            node.next = curt

            if curt.next:
                heappush(heap, curt.next)

            node = node.next

        return dummy.next
