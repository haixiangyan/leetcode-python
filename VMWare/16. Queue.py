class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class Queue:
    def __init__(self):
        self.dummy = Node(0, None)
        self.curt = self.dummy
        self.size = 0

    def enqueue(self, key):
        self.curt.next = Node(key)
        self.curt = self.curt.next
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        head = self.dummy.next
        head_next = head.next

        # Update relation
        self.dummy.next = head_next
        head.next = None

        if self.curt == head:
            self.curt = self.dummy

        # Update size
        self.size -= 1

        return head


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.dequeue()
queue.dequeue()
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print(queue.dequeue().key)
