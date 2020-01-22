class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """
    def __init__(self):
        self.results = []

    def twoSum(self, root, n):
        node_set = set()

        self.inorder(root, n, node_set)

        return self.results

    def inorder(self, root, target, node_set):
        if root is None:
            return

        self.inorder(root.left, target, node_set)
        if root.val in node_set:
            self.results = [target - root.val, root.val]
        else:
            node_set.add(target - root.val)
        self.inorder(root.right, target, node_set)
