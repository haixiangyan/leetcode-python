class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        node = dummy
        store = {}

        while head is not None:
            new_node = RandomListNode(head.label)
            new_node.random = head.random

            store[head] = new_node

            node.next = new_node

            node = node.next
            head = head.next

        node = dummy.next
        while node is not None:
            node.random = store[node.random] if node.random else None
            node = node.next

        return dummy.next
