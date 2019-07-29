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
        if root is None:
            return []

        results = []
        first_queue = [root]

        while len(first_queue) != 0:
            second_queue = []
            # 记录当前 queue
            results.append([node.val for node in first_queue])

            for current_node in first_queue:
                # 添加 children
                if current_node.left is not None:
                    second_queue.append(current_node.left)
                if current_node.right is not None:
                    second_queue.append(current_node.right)

            # 更新 queue
            first_queue = second_queue

        return results
