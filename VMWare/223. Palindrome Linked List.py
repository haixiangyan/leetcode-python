class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        if head is None:
            return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        node, prev = slow.next, None
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next

        left, right = head, prev
        while right and left.val == right.val:
            left = left.next
            right = right.next

        return right is None
