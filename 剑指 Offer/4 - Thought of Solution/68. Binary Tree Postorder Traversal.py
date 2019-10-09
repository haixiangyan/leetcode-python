class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.order = []
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        self.dfs(root)

        return self.order
    
    def dfs(self, root):
        if root is None:
            return
        
        self.dfs(root.left)
        self.dfs(root.right)
        self.order.append(root.val)
