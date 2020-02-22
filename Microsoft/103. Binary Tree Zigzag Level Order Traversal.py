from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return []

        flag = True
        queue = deque([root])
        order = []

        while queue:
            level = []
            if flag:
                order.append([node.val for node in queue])
            else:
                order.append([node.val for node in queue[::-1]])

            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            queue = level
            flag = not flag

        return order
