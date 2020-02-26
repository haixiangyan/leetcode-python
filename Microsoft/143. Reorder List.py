class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return head

        # 找中点
        p_slow = head
        p_fast = head
        while p_fast.next is not None and p_fast.next.next is not None:
            p_slow = p_slow.next
            p_fast = p_fast.next.next

        # 初始
        p_fast = p_slow.next
        p_slow.next = None
        p_next = p_fast.next
        p_fast.next = None

        # 反序
        while p_next is not None:
            p_temp = p_next.next
            p_next.next = p_fast

            p_fast = p_next
            p_next = p_temp

        tail = head
        while p_fast is not None:
            p_temp = p_fast.next
            p_fast.next = tail.next
            tail.next = p_fast

            p_fast = p_temp
            tail = tail.next.next

        return head