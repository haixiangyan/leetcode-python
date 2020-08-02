class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s

        rows = []
        for i in range(min(numRows, len(s))):
            rows.append('')

        curRow, goingDown = 0, False
        for char in s:
            rows[curRow] += char

            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown

            curRow += 1 if goingDown else -1

        charList = []
        for row in rows:
            charList += row

        return ''.join(charList)
