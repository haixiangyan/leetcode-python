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
        node = head

        while node is not None:
            new_node = RandomListNode(node.label)
            new_node.random = node.random

            new_node.next = node.next
            node.next = new_node

            node = new_node.next

        copy = dummy
        node = head
        while node is not None:
            new_node = node.next

            # Random
            if new_node.random:
                new_node.random = new_node.random.next

            # Reorganize
            copy.next = new_node

            node = new_node.next
            copy = copy.next

        return dummy.next
