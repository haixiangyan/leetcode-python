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
            return head

        store = {}
        dummy = RandomListNode(0)
        node = head
        copy = dummy

        while node is not None:
            new_node = RandomListNode(node.label)
            new_node.random = node.random

            store[node] = new_node

            copy.next = new_node

            copy = copy.next
            node = node.next

        node = dummy.next
        while node is not None:
            node.random = store[node.random] if node.random else None
            node = node.next

        return dummy.next
