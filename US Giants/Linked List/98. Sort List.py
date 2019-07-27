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

        # 找中点
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 找到右边链表的头
        left_head = head
        right_head = slow.next
        slow.next = None

        # 分别 sort
        left_list = self.sortList(left_head)
        right_list = self.sortList(right_head)

        # 合并
        sorted_list = self.merge(left_list, right_list)

        return sorted_list

    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = None
        # 初始化第一次合并，为了记录 head
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 is not None:
            current.next = list1
        if list2 is not None:
            current.next = list2

        return head
