class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.maxValue = float('-inf')
        self.maxRoot = None
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        if root is None:
            return None
        
        self.dfs(root)

        return self.maxRoot
    
    def dfs(self, root):
        if root is None:
            return
        
        if root.val > self.maxValue:
            self.maxValue = root.val
            self.maxRoot = root
        
        self.dfs(root.left)
        self.dfs(root.right)