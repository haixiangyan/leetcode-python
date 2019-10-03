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

        for list in lists:
            if list is not None:
                heapq.heappush(heap, list)

        dummy = ListNode(0)
        head = dummy
        while heap:
            node = heapq.heappop(heap)

            head.next = node
            head = head.next

            if node.next is not None:
                heapq.heappush(heap, node.next)

        return dummy.next
