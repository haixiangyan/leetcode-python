class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        rt = []
        self.get(T1, rt)
        t1 = ','.join(rt)

        rt = []
        self.get(T2, rt)
        t2 = ','.join(rt)

        return t1.find(t2) != -1


    def get(self, root, rt):
        if root is None:
            rt.append('#')
            return

        rt.append(str(root.val))
        self.get(root.left, rt)
        self.get(root.right, rt)