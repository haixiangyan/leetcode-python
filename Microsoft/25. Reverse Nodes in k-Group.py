class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev:
            prev = self.reverse_next_k(prev, k)

        return dummy.next

    def reverse_next_k(self, prev, k):
        n1 = prev.next
        nk = self.find_kth(prev, k)
        if nk is None:
            return None

        nk_next = nk.next
        nk.next = None

        nk = self.reverse_list(n1)

        prev.next = nk
        n1.next = nk_next

        return n1

    def find_kth(self, prev, k):
        for _ in range(k):
            if prev is None:
                return None
            prev = prev.next
        return prev

    def reverse_list(self, head):
        prev, curt = None, head
        while curt:
            next = curt.next

            curt.next = prev

            prev = curt
            curt = next
        return prev
