class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        if head is None:
            return head

        node = head

        while node.next is not None:
            # 如果相等就指向下一个节点，相当于尝试看下下个节点是否还相等
            if node.val == node.next.val:
                node.next = node.next.next
            # 如果不相等就更新 node
            else:
                node = node.next

        return head
