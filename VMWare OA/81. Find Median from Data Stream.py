import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        if not nums:
            return []

        results = []
        max_heap, min_heap = [], []

        results.append(nums[0])
        heapq.heappush(max_heap, -nums[0])

        for i in range(1, len(nums)):
            # Push to heaps
            if nums[i] <= -max_heap[0]:
                heapq.heappush(max_heap, -nums[i])
            else:
                heapq.heappush(min_heap, nums[i])

            # Maintain balance
            # max_heap = min_heap + 1
            # max_heap = min_heap
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            results.append(-max_heap[0])

        return results
