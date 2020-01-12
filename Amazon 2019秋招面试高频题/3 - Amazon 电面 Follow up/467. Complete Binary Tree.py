class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):
        if root is None:
            return True

        stack = [root]
        index = 0

        while index < len(stack):
            if stack[index]:
                stack.append(stack[index].left)
                stack.append(stack[index].right)

            index += 1

        while stack[-1] is None:
            stack.pop()

        for node in stack:
            if node is None:
                return False

        return True
