class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        if not s:
            return 0

        result, num, sign = 0, 0, 1
        stack = []
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                result *= stack[-1]
                stack.pop()
                result += stack[-1]
                stack.pop()
                num = 0
        result += sign * num
        return result
