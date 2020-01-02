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
        if not lists:
            return None

        dummy = ListNode(0)
        copy = dummy
        heap = []

        # Initialize
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        # Pop out
        while heap:
            head = heapq.heappop(heap)

            copy.next = ListNode(head.val)

            copy = copy.next

            if head.next:
                heapq.heappush(heap, head.next)

        return dummy.next