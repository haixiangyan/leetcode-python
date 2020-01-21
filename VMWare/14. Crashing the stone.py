import heapq

class Solution:
    def crash_stone(self, nums):
        if not nums:
            return 0
        if len(nums) == 0:
            return nums[0]

        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, abs(first - second))

        return 0 if not heap else heap[0]

s = Solution()
nums = [1, 2, 3, 4, 4]
print(s.crash_stone(nums))

nums = [1, 2, 3, 4, 5]
print(s.crash_stone(nums))
