class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if fast.next is None or fast.next.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True
