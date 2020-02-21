class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        store = {}
        dummy = Node(0)
        new_list = dummy
        node = head
        while node:
            new_node = Node(node.val)
            new_node.random = node.random

            store[node] = new_node

            new_list.next = new_node

            new_list = new_list.next
            node = node.next

        new_list = dummy.next
        while new_list:
            new_list.random = store[new_list.random] if new_list.random in store else None
            new_list = new_list.next
        return dummy.next
