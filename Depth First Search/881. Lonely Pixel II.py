class Solution:
    """
    @param picture: a 2D char array
    @param N: an integer
    @return: return a integer
    """
    def findBlackPixel(self, picture, N):
        if not picture or not picture[0]:
            return 0

        m, n = len(picture), len(picture[0])
        row_keys = {}
        col_counts = [0 for _ in range(n)]

        for i in range(m):
            key = self.scan_row(picture, i, col_counts, N, n)

            if key:
                row_keys[key] = row_keys.get(key, 0) + 1

        result = 0
        for key in row_keys:
            if row_keys[key] == N:
                for j in range(n):
                    if key[j] == 'B' and col_counts[j] == N:
                        result += N

        return result

    def scan_row(self, picture, row, col_counts, N, n):
        row_counts = 0
        for j in range(n):
            if picture[row][j] == 'B':
                row_counts += 1
                col_counts[j] += 1

        return ''.join(picture[row]) if row_counts == N else ''
