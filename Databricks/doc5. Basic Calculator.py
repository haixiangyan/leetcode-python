# 第二題加上parenthesis 例如"2+((8+2)+(3-999))"一樣回傳計算結果
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        result, number, sign = 0, 0, 1
        stack = []

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '+':
                result += sign * number
                sign = 1
                number = 0
            elif char == '-':
                result += sign * number
                sign = -1
                number = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ')':
                result += sign * number
                result *= stack[-1]
                stack.pop()
                result += stack[-1]
                stack.pop()
                number = 0

        result += sign * number
        return result
