from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        rows_num, cols_num = len(matrix), len(matrix[0])
        rows, cols = [False] * rows_num, [False] * cols_num

        for i in range(rows_num):
            for j in range(cols_num):
                if matrix[i][j] == 0:
                    rows[i], cols[j] = True, True

        for i in range(rows_num):
            for j in range(cols_num):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
