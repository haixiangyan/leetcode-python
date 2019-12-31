class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, target):
        paths = []
        if root:
            self.divide_conquer(root, paths, target, [])
        return paths

    def divide_conquer(self, root, paths, target, prev_path):
        curt_path = prev_path + [root.val]

        if root.left is None and root.right is None:
            if self.sum_up(curt_path) == target:
                paths.append(curt_path)

        if root.left:
            self.divide_conquer(root.left, paths, target, curt_path)
        if root.right:
            self.divide_conquer(root.right, paths, target, curt_path)

    def sum_up(self, path):
        result = 0
        for value in path:
            result += value
        return result
