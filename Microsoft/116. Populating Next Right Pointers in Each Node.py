from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        dummy = Node()

        queue = deque([root])
        while queue:
            node = dummy
            for _ in range(len(queue)):
                curt = queue.popleft()

                node.next = curt
                node = node.next

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
