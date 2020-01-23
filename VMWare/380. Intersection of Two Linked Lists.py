class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        len_a, len_b = self.get_length(headA), self.get_length(headB)
        node_a, node_b = headA, headB

        while len_a > len_b:
            node_a = node_a.next
            len_a -= 1
        while len_b > len_a:
            node_b = node_b.next
            len_b -= 1
        while node_a != node_b:
            node_a = node_a.next
            node_b = node_b.next

        return node_a


    def get_length(self, head):
        length = 0
        while head is not None:
            head = head.next
            length += 1
        return length
