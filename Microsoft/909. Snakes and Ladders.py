from collections import deque
class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        distance = {1: 0}
        queue = deque([1])

        while queue:
            s = queue.popleft()

            if s == n * n:
                return distance[s]

            for next_step in range(s + 1, min(s + 6, n * n) + 1):
                r, c = self.get(next_step, n)
                # 快速通道
                if board[r][c] != -1:
                    next_step = board[r][c]
                if next_step not in distance:
                    distance[next_step] = distance[s] + 1
                    queue.append(next_step)
        return -1

    def get(self, s, n):
        quotient, remainder = divmod(s - 1, n)

        row = n - 1 - quotient
        col = remainder if row % 2 != n % 2 else n - 1 - remainder

        return row, col
