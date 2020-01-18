from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []

        order = []

        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                curt = queue.popleft()
                level.append(curt.val)

                if curt.left:
                    queue.append(curt.left)
                if curt.right:
                    queue.append(curt.right)

            order.append(level)

        return order
