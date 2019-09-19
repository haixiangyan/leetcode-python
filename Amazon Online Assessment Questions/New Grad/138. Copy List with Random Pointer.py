class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0, None, None)
        newHead = dummy

        store = {}

        while head is not None:
            copy = Node(head.val, None, head.random)

            newHead.next = copy
            store[head] = copy

            newHead = newHead.next
            head = head.next

        newHead = dummy.next
        while newHead is not None:
            newHead.random = store[newHead.random] if newHead.random is not None else None
            newHead = newHead.next

        return dummy.next
