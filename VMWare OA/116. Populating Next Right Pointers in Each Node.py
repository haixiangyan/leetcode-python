from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if root is None:
            return root

        dummy = Node(0, None, None, None)

        queue = deque([root])
        while queue:
            node = dummy

            for _ in range(len(queue)):
                curt = queue.popleft()

                node.next = curt
                node = curt

                if curt.left:
                    queue.append(curt.left)
                if curt.right:
                    queue.append(curt.right)

        return root
