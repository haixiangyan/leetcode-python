class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """
    def widthOfBinaryTree(self, root):
        heights = []

        self.dfs(root, 0, 0, heights)

        width = 0
        for nodes in heights:
            if len(nodes) == 1:
                width = max(width, 1)
            elif len(nodes) >= 2:
                width = max(width, abs(nodes[-1] - nodes[0]) + 1)
        return width

    def dfs(self, root, index, height, heights):
        if root is None:
            return

        if height >= len(heights):
            heights.append([])

        heights[height].append(index)

        self.dfs(root.left, 2 * index, height + 1, heights)
        self.dfs(root.right, 2 * index + 1, height + 1, heights)
