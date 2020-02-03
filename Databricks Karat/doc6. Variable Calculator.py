class Solution:
    def __init__(self):
        self.map = {
            'abc': 11,
            'def': 33,
            'ii': 7
        }
    def calculator(self, s):
        if not s:
            return 0

        stack = []
        result, num, sign, var = 0, 0, 1, ''
        is_num = True

        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
                is_num = True
            elif char.isalpha():
                var += char
                is_num = False
            elif char == '+':
                result += sign * (num if is_num else self.map[var])
                sign, num, var = 1, 0, ''
            elif char == '-':
                result += sign * (num if is_num else self.map[var])
                sign, num, var = -1, 0, ''
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif char == ')':
                result += sign * (num if is_num else self.map[var])
                result *= stack[-1]
                stack.pop()
                result += stack[-1]
                stack.pop()
                num, var = 0, ''
        result += sign * (num if is_num else self.map[var])
        return result

s = Solution()
str = '(1 + 3) - (ii + (abc + 3) - 2)'
print(s.calculator(str))
