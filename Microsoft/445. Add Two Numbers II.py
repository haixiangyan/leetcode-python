class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        while l1:
            num1 = 10 * num1 + l1.val
            l1 = l1.next
        while l2:
            num2 = 10 * num2 + l2.val
            l2 = l2.next

        target = num1 + num2
        dummy = ListNode(0)
        curt = dummy

        for num in str(target):
            curt.next = ListNode(int(num))
            curt = curt.next

        return dummy.next
