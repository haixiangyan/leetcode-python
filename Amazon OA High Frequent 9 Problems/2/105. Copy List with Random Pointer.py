class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        store = {}
        dummy = RandomListNode(0)
        start = dummy

        while head is not None:
            curtNode = RandomListNode(head.label)
            curtNode.random = head.random
            store[head] = curtNode

            start.next = curtNode

            start = start.next
            head = head.next

        start = dummy.next
        while start is not None:
            start.random = store[start.random] if start.random else None
            start = start.next

        return dummy.next
