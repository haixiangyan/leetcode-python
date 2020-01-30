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

        while len(lists) > 1:
            next_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    next_lists.append(self.merge_two_sorted_lists(lists[i], lists[i + 1]))
                else:
                    next_lists.append(lists[i])
            lists = next_lists

        return lists[0]

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
