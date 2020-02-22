class Solution:
    def maxChunksToSorted(self, arr) -> int:
        if not arr:
            return 0

        counts = 0
        n = len(arr)
        left_max = [0 for _ in range(n)]
        right_min = [0 for _ in range(n)]

        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])

        right_min[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], arr[i])

        for i in range(n - 1):
            if left_max[i] <= right_min[i + 1]:
                counts += 1

        return counts + 1
