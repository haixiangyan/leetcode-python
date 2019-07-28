class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """

    def reverse(self, head):
        prev = None
        curt = head
        while curt is not None:
            # 缓存 curt.next
            curt_next = curt.next

            curt.next = prev
            prev = curt
            curt = curt_next

        return prev

    def find_nth(self, head, n):
        curt = head
        for i in range(n):
            if curt is None:
                return None
            curt = curt.next

        return curt

    def reverseBetween(self, head, m, n):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0, head)

        # 找到第 m - 1 个
        mth_prev = self.find_nth(dummy, m - 1)
        mth = mth_prev.next
        # 找到第 n 个
        nth = self.find_nth(dummy, n)
        nth_next = nth.next

        # 断开
        nth.next = None

        self.reverse(mth)

        # 重新连接
        mth_prev.next = nth
        mth.next = nth_next

        return dummy.next
