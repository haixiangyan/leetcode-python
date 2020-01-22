import math

class Solution:
    def __init__(self):
        self.COLS = 702

    def notation(self, target):
        if target <= 0:
            return None

        # Get row number and col number
        row = math.ceil(target / self.COLS)
        col = (target - 1) % self.COLS + 1

        col_str = self.get_col_str(col)

        return str(row) + col_str

    # Transfer column number to string.
    # Example: 702 -> 'ZZ'
    def get_col_str(self, col):
        col_str = ''

        while col > 0:
            quotient, remainder = divmod(col - 1, 26)

            col_str = chr(ord('A') + remainder) + col_str
            col = quotient

        return col_str

s = Solution()

# 1ZZ
target = 702
print(s.notation(target))

# 2A
target = 703
print(s.notation(target))

# 1AA
target = 27
print(s.notation(target))
