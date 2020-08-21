# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        root_pos = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:root_pos], postorder[:root_pos])
        root.right = self.buildTree(inorder[root_pos + 1:], postorder[root_pos:-1])

        return root
