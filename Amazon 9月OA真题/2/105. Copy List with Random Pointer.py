class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return head

        dummy = RandomListNode(0)
        start = dummy
        store = {}

        # 遍历链表
        while head is not None:
            nextNode = RandomListNode(head.label)
            nextNode.random = head.random

            start.next = nextNode
            store[head] = nextNode

            start = start.next
            head = head.next

        # 取回 random 节点
        start = dummy.next
        while start is not None:
            start.random = None if start.random is None else store[start.random]
            start = start.next

        return dummy.next
