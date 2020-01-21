class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
                continue

            # Get sub string
            sub_str = []
            while stack and stack[-1] != '[':
                sub_str.append(stack.pop())

            stack.pop()

            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += int(stack.pop()) * base
                base *= 10

            stack.append(''.join(reversed(sub_str)) * repeats)

        return ''.join(stack)
