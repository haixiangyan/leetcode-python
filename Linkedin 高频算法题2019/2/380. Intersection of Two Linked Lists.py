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
        # 串起来
        end = headA
        while end.next is not None:
            end = end.next
        end.next = headB

        # 找交点
        slow, fast = headA, headA.next
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        slow = headA
        fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next

        end.next = None

        return slow
