class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        stack = [root]
        results = []
        next_from_left = False

        while len(stack) != 0:
            results.append([node.val for node in stack])
            next_stack = []

            for i in range(len(stack)):
                node = stack.pop()

                if next_from_left:
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)
                else:
                    if node.right:
                        next_stack.append(node.right)
                    if node.left:
                        next_stack.append(node.left)

            stack = next_stack
            next_from_left = not next_from_left

        return results
