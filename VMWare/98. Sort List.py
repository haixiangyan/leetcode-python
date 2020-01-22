class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        middle = self.find_mid(head)

        right = self.sortList(middle.next)
        middle.next = None
        left = self.sortList(head)

        return self.merge(left, right)

    def find_mid(self, head):
        slow, fast = head, head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, h1, h2):
        dummy = ListNode(0)
        node = dummy

        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                node.next = h1
                h1 = h1.next
            else:
                node.next = h2
                h2 = h2.next
            node = node.next

        node.next = h1 if h1 is not None else h2

        return dummy.next
