class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return ''

        stack = []
        for char in S:
            if not stack:
                stack.append(char)
            else:
                if stack and char == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)

        return ''.join(stack)