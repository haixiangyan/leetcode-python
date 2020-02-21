class Node:
    def __init__(self, key, val, next=None):
        self.val = val
        self.key = key
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.tail = self.dummy = Node(0, 0)
        self.key_to_prev = {}
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_prev:
            return -1

        self.kick(self.key_to_prev[key])

        return self.key_to_prev[key].next.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.val = value
            return

        self.push_back(Node(key, value))
        self.size += 1

        if self.size > self.capacity:
            self.pop_front()

    def kick(self, prev):
        node = prev.next
        next = node.next

        if node == self.tail:
            return

        self.key_to_prev[next.key] = prev
        prev.next = next

        node.next = None

        self.push_back(node)

    def push_back(self, node):
        self.tail.next = node
        self.key_to_prev[node.key] = self.tail
        self.tail = node

    def pop_front(self):
        head = self.dummy.next
        next = head.next

        self.dummy.next = next
        self.key_to_prev[next.key] = self.dummy

        head.next = None
        del self.key_to_prev[head.key]

        self.size -= 1
