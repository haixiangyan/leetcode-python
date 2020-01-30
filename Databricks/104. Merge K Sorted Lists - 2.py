class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None

        return self.merge_range(lists, 0, len(lists) - 1)

    def merge_range(self, lists, start, end):
        if start == end:
            return lists[start]

        middle = (start + end) // 2
        left = self.merge_range(lists, start, middle)
        right = self.merge_range(lists, middle + 1, end)

        return self.merge_two_sorted_lists(left, right)

    def merge_two_sorted_lists(self, left, right):
        dummy = ListNode(0)
        node = dummy

        while left is not None and right is not None:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        while left is not None:
            node.next = left
            left = left.next
            node = node.next
        while right is not None:
            node.next = right
            right = right.next
            node = node.next

        return dummy.next
