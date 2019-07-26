class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # Define iteration reference
        current = head
        copy = RandomListNode(head.label)

        copy_head = copy
        current_head = head

        # Init hash table
        hash_table = {current: copy}

        while current is not None:
            copy.random = current.random

            # Update next
            if current.next is not None:
                copy.next = RandomListNode(current.next.label)
                hash_table[current.next] = copy.next
            else:
                copy.next = None

            current = current.next
            copy = copy.next

        copy = copy_head

        while copy is not None:
            if copy.random is not None:
                copy.random = hash_table[copy.random]
                current_head = current_head.next
            copy = copy.next

        return copy_head
