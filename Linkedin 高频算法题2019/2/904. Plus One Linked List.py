class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """

    def plusOne(self, head):
        newHead = head
        stack = []

        while head is not None:
            stack.append(head)
            head = head.next

        while stack and stack[-1].val == 9:
            curt = stack.pop()
            curt.val = 0

        if stack:
            stack[-1].val += 1
        else:
            newHead = ListNode(1, newHead)

        return newHead
