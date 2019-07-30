class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """

    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:rootPos + 1], inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos + 1:], inorder[rootPos + 1:])

        return root
