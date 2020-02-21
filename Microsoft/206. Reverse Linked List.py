class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, node = None, head

        while node:
            next = node.next

            node.next = prev

            prev = node
            node = next

        return prev
