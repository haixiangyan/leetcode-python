class Solution:
    def __init__(self):
        self.numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2147483647, -2147483648

        s = s.strip()
        if not s:
            return 0

        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        new_s = ''
        for char in s:
            if char.isdigit():
                new_s += char
            else:
                break

        if not new_s:
            return 0

        result = 0
        for char in new_s:
            result = 10 * result + self.numbers[char]

        if negative:
            result = -result

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
