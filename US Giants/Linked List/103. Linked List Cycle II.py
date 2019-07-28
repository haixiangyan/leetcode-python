class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None

        # 找到相交的点
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow != fast:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
