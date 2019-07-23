class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        if head is None:
            return head

        size = self.get_list_size(head)
        k = k % (size - 1)

        if k == 0:
            return head

        temp_head = head
        next_k_head = head

        # 先走 k 步
        for i in range(k):
            next_k_head = next_k_head.next

        # 同时走，直到 head 走到尽头
        while next_k_head.next is not None:
            head = head.next
            next_k_head = next_k_head.next

        result = head.next
        head.next = None
        next_k_head.next = temp_head

        return result

    def get_list_size(self, head):
        size = 1
        current_node = head

        while current_node is not None:
            size += 1
            current_node = current_node.next

        return size
