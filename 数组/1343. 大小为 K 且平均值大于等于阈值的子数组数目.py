from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        cur_sum = 0

        for i in range(k):
            cur_sum += arr[i]

        for i in range(k, len(arr)):
            if cur_sum >= threshold * k:
                result += 1

            cur_sum += arr[i]
            cur_sum -= arr[i - k]

        if cur_sum >= threshold * k:
            result += 1

        return result
