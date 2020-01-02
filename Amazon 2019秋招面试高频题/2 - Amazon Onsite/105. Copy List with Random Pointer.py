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

        dummy = RandomListNode(0)
        copy = dummy
        node = head

        store = {}

        while node is not None:
            new_node = RandomListNode(node.label)
            new_node.random = node.random

            store[node] = new_node

            copy.next = new_node

            copy = copy.next
            node = node.next

        copy = dummy.next
        while copy is not None:
            copy.random = store[copy.random] if copy.random else None
            copy = copy.next

        return dummy.next
