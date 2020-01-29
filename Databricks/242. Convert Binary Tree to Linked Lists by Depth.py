from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if root is None:
            return []

        linked_list = []
        queue = deque([root])
        while queue:
            dummy = ListNode(0)
            list_node = dummy

            for _ in range(len(queue)):
                node = queue.popleft()
                list_node.next = ListNode(node.val)
                list_node = list_node.next

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            linked_list.append(dummy.next)
        return linked_list
