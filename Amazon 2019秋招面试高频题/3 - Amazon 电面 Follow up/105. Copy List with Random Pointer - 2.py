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

        node = head
        while node is not None:
            node_next = node.next

            new_node = RandomListNode(node.label)

            node.next = new_node
            new_node.next = node_next

            node = node_next

        copy = head.next
        node = head
        while node is not None:
            new_node = node.next
            node_next = new_node.next

            if node_next:
                new_node.next = node_next.next

            if node.random:
                new_node.random = node.random.next

            node = node_next

        return copy
