class Solution:
    """
    @param num: a string
    @param k: an integer
    @return: return a string
    """
    def removeKdigits(self, num, k):
        if k == 0:
            return num
        if not num:
            return '0'

        stack = []
        for i in range(len(num)):
            while len(stack) > 0 and k > 0 and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            if num[i] != '0' or len(stack) > 0:
                stack.append(num[i])

        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1

        if len(stack) == 0:
            return '0'

        return ''.join(stack)
