class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        dummy = Node(0)
        new_list = dummy
        node = head

        while node:
            new_node = Node(node.val)
            new_node.random = node.random

            next = node.next

            node.next = new_node
            new_node.next = next

            node = next

        node = head
        while node:
            new_node = node.next

            if new_node.random:
                new_node.random = new_node.random.next

            new_list.next = new_node

            new_list = new_list.next
            node = new_node.next

        return dummy.next
