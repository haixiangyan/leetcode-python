class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if root is None:
            return float('inf')
        lowerBound = self.getLowerBound(root, target)
        upperBound = self.getUpperBound(root, target)

        if lowerBound is None:
            return upperBound.val
        if upperBound is None:
            return lowerBound.val

        if target - lowerBound.val < upperBound.val - target:
            return lowerBound.val
        return upperBound.val

    def getLowerBound(self, root, target):
        if root is None:
            return None

        if target < root.val:
            return self.getLowerBound(root.left, target)

        lower = self.getLowerBound(root.right, target)

        return root if lower is None else lower

    def getUpperBound(self, root, target):
        if root is None:
            return None

        if target >= root.val:
            return self.getUpperBound(root.right, target)

        upper = self.getUpperBound(root.left, target)

        return root if upper is None else upper
