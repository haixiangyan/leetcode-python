class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        nums = []

        self.find_nums(root, 0, nums)

        return sum(nums)

    def find_nums(self, root, prefix, nums):
        if root is None:
            return

        num = prefix * 10 + root.val

        if root.left is None and root.right is None:
            nums.append(num)
            return

        self.find_nums(root.left, num, nums)
        self.find_nums(root.right, num, nums)
