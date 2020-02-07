from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def serialize(self, root):
        if root is None:
            return ''

        queue = deque([root])
        order = []
        while queue:
            node = queue.popleft()
            if node is None:
                order.append('#')
            else:
                order.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        # 去掉后面的 #
        for i in range(len(order) - 1, -1, -1):
            if order[i] == '#':
                order.pop()
            else:
                break
        return ','.join(order)

    def deserialize(self, data):
        if not data or data == '':
            return None

        order = data.split(',')
        root = TreeNode(int(order[0]))
        queue = deque([root])
        index, n = 1, len(order)

        while queue:
            if index == n: break
            node = queue.popleft()
            if order[index] != '#':
                node.left = TreeNode(int(order[index]))
                queue.append(node.left)
            index += 1

            if index == n: break
            if order[index] != '#':
                node.right = TreeNode(int(order[index]))
                queue.append(node.right)
            index += 1
        return root
