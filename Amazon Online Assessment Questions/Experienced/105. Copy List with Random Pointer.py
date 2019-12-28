class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head

        # Store node -> node copy
        store = {}

        dummy = RandomListNode(0)
        copy = dummy
        while head is not None:
            copy_node = RandomListNode(head.label)
            copy_node.random = head.random

            store[head] = copy_node

            copy.next = copy_node
            copy = copy.next
            head = head.next

        copy = dummy
        while copy is not None:
            copy.random = store[copy.random] if copy.random else None
            copy = copy.next

        return dummy.next