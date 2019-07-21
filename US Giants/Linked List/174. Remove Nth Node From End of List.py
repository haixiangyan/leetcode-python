class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        result = ListNode(0)
        result.next = head

        # 先走 n 步
        for i in range(n):
            head = head.next

        # 相当于先往后退了一步
        preDelete = result

        while head is not None:
            preDelete = preDelete.next
            head = head.next

        # 删掉对应的节点
        preDelete.next = preDelete.next.next

        # 返回最初节点
        return result.next
