class Solution:
    def __init__(self):
        self.map = {
            'abc': 11,
            'def': 33,
            'ii': 7
        }
    def calculator(self, str):
        result, number, sign, var = 0, 0, 1, ''
        is_num = True
        stack = []

        for char in str:
            if char.isdigit():
                number = number * 10 + int(char)
                is_num = True
            elif char.isalpha():
                var += char
                is_num = False
            elif char == '+':
                num = number if is_num else self.map[var]
                result += sign * num
                number, var, sign = 0, '', 1
            elif char == '-':
                num = number if is_num else self.map[var]
                result += sign * num
                number, var, sign = 0, '', -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif char == ')':
                num = number if is_num else self.map[var]
                result += sign * num
                result *= stack[-1]
                stack.pop()
                result += stack[-1]
                stack.pop()

                number, var = 0, ''
        num = number if is_num else self.map[var]
        result += sign * num
        return result

s = Solution()
str = '1+3-11+ii-abc+33'
print(s.calculator(str))