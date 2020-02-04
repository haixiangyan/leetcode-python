class Solution:
    def __init__(self):
        self.map = {
            'abc': 11,
            'def': 33,
            'ii': 7
        }

    def get_curt_number(self, number, variable, is_num):
        return number if is_num else self.map[variable]

    def calculator(self, s):
        if not s:
            return 0

        is_num = False
        result, number, variable, sign = 0, 0, '', 1
        stack = []

        for char in s:
            if char.isdigit():
                number = 10 * number + int(char)
                is_num = True
            elif char.isalpha():
                variable += char
                is_num = False
            elif char == '+':
                result += sign * self.get_curt_number(number, variable, is_num)
                number, variable, sign = 0, '', 1
            elif char == '-':
                result += sign * self.get_curt_number(number, variable, is_num)
                number, variable, sign = 0, '', -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif char == ')':
                result += sign * self.get_curt_number(number, variable, is_num)

                result *= stack[-1]
                stack.pop()

                result += stack[-1]
                stack.pop()

                number, variable = 0, ''
        result += sign * self.get_curt_number(number, variable, is_num)
        return result


s = Solution()
str = '(1 + 3) - (ii + (abc + 3) - 2)'
print(s.calculator(str))