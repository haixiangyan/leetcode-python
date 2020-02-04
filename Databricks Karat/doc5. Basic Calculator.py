class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        result, number, sign = 0, 0, 1
        stack = []

        for char in s:
            if char.isdigit():
                number = 10 * number + int(char)
            elif char == '+':
                result += sign * number
                sign, number = 1, 0
            elif char == '-':
                result += sign * number
                sign, number = -1, 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif char == ')':
                result += sign * number

                result *= stack[-1]
                stack.pop()

                result += stack[-1]
                stack.pop()

                number, sign = 0, 1
        result += sign * number
        return result
