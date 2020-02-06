from collections import deque

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        n = len(nums)
        k = min(k, n)

        queue = deque([])
        for i in range(k - 1):
            self.push(queue, nums, i)

        results = []
        for i in range(k - 1, n):
            self.push(queue, nums, i)
            results.append(nums[queue[0]])

            if i - k + 1 == queue[0]:
                queue.popleft()

        return results

    def push(self, queue, nums, i):
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)
