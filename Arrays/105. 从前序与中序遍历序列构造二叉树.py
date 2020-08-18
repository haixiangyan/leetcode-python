# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        root = TreeNode(preorder[0])

        rootPos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: 1 + rootPos], inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos + 1:], inorder[rootPos + 1:])

        return root
