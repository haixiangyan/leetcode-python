from collections import Counter
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        counts = Counter(nums)

        values = list(counts.keys())

        self.sort(values, counts, k, 0, len(values) - 1)

        return values[:k]

    def sort(self, values, counts, k, start, end):
        left, right = start, end

        if left >= right:
            return

        pivot = counts[values[(left + right) // 2]]
        while left <= right:
            while left <= right and counts[values[left]] > pivot:
                left += 1
            while left <= right and counts[values[right]] < pivot:
                right -= 1
            if left <= right:
                values[left], values[right] = values[right], values[left]
                left, right = left + 1, right - 1

        if k - 1 <= right:
            self.sort(values, counts, k, start, right)
        if k - 1 >= left:
            self.sort(values, counts, k, left, end)
