class Solution:
    def evenSubarray(self, nums, k):
        if not nums:
            return 0

        left, right, odd_counts = 0, 0, 0
        results = set()
        sub_array = []

        while right < len(nums):
            # Count ood number on right
            odd_counts += 1 if nums[right] % 2 == 1 else 0

            # Sliding window, if counts is larger than k, then shift left pointer
            while odd_counts > k:
                if nums[left] % 2 == 1:
                    odd_counts -= 1
                left += 1
                sub_array.remove(sub_array[0])

            sub_array.append(nums[right])
            self.update_results(results, sub_array)
            right += 1

        return len(results)

    def update_results(self, results, sub_array):
        for i in range(len(sub_array)):
            # Serialize subarray to avoid duplicate subarray
            results.add(','.join(str(num) for num in sub_array[i:]))

s = Solution()
nums = [1, 2, 3, 4]
k = 1
print(s.evenSubarray(nums, k))
