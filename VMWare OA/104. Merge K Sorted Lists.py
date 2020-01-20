import heapq


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        heap = []

        for l in lists:
            if l is not None:
                heapq.heappush(heap, l)

        dummy = ListNode(0)
        node = dummy

        while heap:
            curt = heapq.heappop(heap)

            node.next = curt
            node = node.next

            if curt.next:
                heapq.heappush(heap, curt.next)

        return dummy.next
