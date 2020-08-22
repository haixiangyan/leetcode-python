from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [1]
        for i in range(1, rowIndex + 1):
            rows.insert(0, 0)
            for j in range(i):
                rows[j] = rows[j] + rows[j + 1]
        return rows
