class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    def isSubtree(self, s, t):
        if s is None:
            return t is None

        if s == t:
            return self.compare(s, t)

        return self.isSubtree(s.left, t.left) or self.isSubtree(s.right, t.right)

    def compare(self, s, t):
        if s is None:
            return t is None

        if t is None or s.val != t.val:
            return False

        return self.compare(s.left, t.left) and self.compare(s.right, t.right)
