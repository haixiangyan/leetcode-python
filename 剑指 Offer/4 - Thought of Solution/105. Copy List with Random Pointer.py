class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None

        dummy = RandomListNode(0)
        newHead = dummy
        store = {}

        while head is not None:
            newNode = RandomListNode(head.label)
            newNode.random = head.random

            # Store
            store[head] = newNode

            # Update next
            newHead.next = newNode

            newHead = newHead.next
            head = head.next

        newHead = dummy.next
        while newHead is not None:
            if newHead.random:
                newHead.random = store[newHead.random]
            newHead = newHead.next

        return dummy.next
