class Solution:
    def maxChunksToSorted(self, arr) -> int:
        if not arr:
            return 0

        n = len(arr)
        counts = 0
        forward = [0 for _ in range(n)]
        backward = [0 for _ in range(n)]

        forward[0] = arr[0]
        for i in range(1, n):
            forward[i] = max(forward[i - 1], arr[i])

        backward[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            backward[i] = min(backward[i + 1], arr[i])

        for i in range(n - 1):
            if forward[i] <= backward[i + 1]:
                counts += 1

        return counts + 1
