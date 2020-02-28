class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or head.next is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        self.remove_node(slow)

        return dummy.next

    def remove_node(self, prev):
        node, next = prev.next, prev.next.next

        prev.next = next
        node.next = None
