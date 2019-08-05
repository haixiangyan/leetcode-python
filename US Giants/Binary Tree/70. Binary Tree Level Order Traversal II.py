class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        if not root:
            return []

        results = []
        queue = [root]

        while len(queue) != 0:
            new_queue = []
            results.append([node.val for node in queue])

            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

            queue = new_queue

        return list(reversed(results))
