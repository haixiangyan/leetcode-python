class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        if not s:
            return False

        stack = []

        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ']' and stack[-1] != '[' or char == '}' and stack[-1] != '{' or char == ')' and stack[-1] != '(':
                    return False
                stack.pop()

        return not stack
