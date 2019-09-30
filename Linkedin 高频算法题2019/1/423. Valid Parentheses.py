class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                if not self.isValid(char, stack):
                    return False
                stack.pop()
        return not stack

    def isValid(self, char, stack):
        top = stack[-1]

        if top == '(' and char != ')':
            return False
        if top == '{' and char != '}':
            return False
        if top == '[' and char != ']':
            return False

        return True
