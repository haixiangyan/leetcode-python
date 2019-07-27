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
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode(0)
        current = dummy
        digit_carry = 0

        while l1 is not None or l2 is not None:
            # 判断当前是否有值
            l1_value = 0 if l1 is None else l1.val
            l2_value = 0 if l2 is None else l2.val

            # 计算必要的变量
            digit_sum = l1_value + l2_value + digit_carry
            digit_remain = digit_sum % 10
            digit_carry = digit_sum // 10

            current.next = ListNode(digit_remain)

            current = current.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        # 判断最后一位
        if digit_carry != 0:
            current.next = ListNode(digit_carry)

        return dummy.next
