class Solution:
    def notation(self, target):
        if target <= 0:
            return None

        cols = 702

        row = target // cols + (0 if target % cols == 0 else 1)
        col = (target % cols) if (target % cols) else cols

        col_str = self.get_col_str(col)

        return str(row) + col_str

    def get_col_str(self, col):
        col_str = ''

        while col > 0:
            col_str = chr(ord('A') + ((col - 1) % 26)) + col_str
            col = (col - 1) // 26

        return col_str

target = 702
s = Solution()
print(s.notation(target))
