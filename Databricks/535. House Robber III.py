class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        if not root:
            return 0

        rob, not_rob = self.dfs(root)

        return max(rob, not_rob)

    def dfs(self, root):
        if root is None:
            return 0, 0

        left_rob, left_not_rob = self.dfs(root.left)
        right_rob, right_not_rob = self.dfs(root.right)

        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

        return rob, not_rob
