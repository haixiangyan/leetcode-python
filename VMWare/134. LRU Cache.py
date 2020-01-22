class LinkedNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.dummy = LinkedNode(-1, -1)
        self.tail = self.dummy
        self.capacity = capacity
        self.key_to_prev = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_to_prev:
            return -1

        self.kick(self.key_to_prev[key])

        return self.key_to_prev[key].next.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return

        self.push_back(LinkedNode(key, value))

        if len(self.key_to_prev) > self.capacity:
            self.pop_front()

    def kick(self, prev):
        node = prev.next

        if node == self.tail:
            return

        # Delete all links
        prev.next = node.next
        self.key_to_prev[node.next.key] = prev
        node.next = None

        # Push to back
        self.push_back(node)

    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        head = self.dummy.next

        # Delete head
        del self.key_to_prev[head.key]

        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

        head.next = None
