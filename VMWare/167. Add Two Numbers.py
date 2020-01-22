class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        exceed = 0

        dummy = ListNode(0)
        node = dummy

        while l1 is not None and l2 is not None:
            curt_sum = l1.val + l2.val + exceed

            exceed = curt_sum // 10

            node.next = ListNode(curt_sum % 10)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            curt_sum = l1.val + exceed

            exceed = curt_sum // 10

            node.next = ListNode(curt_sum % 10)
            node = node.next
            l1 = l1.next

        while l2 is not None:
            curt_sum = l2.val + exceed

            exceed = curt_sum // 10

            node.next = ListNode(curt_sum % 10)
            node = node.next
            l2 = l2.next

        if exceed > 0:
            node.next = ListNode(exceed)

        return dummy.next
