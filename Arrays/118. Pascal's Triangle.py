from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for i in range(num_rows):
            rows = [None] * (i + 1)
            rows[0], rows[-1] = 1, 1

            for j in range(1, i):
                rows[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(rows)

        return triangle
