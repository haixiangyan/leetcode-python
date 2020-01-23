class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        if not S or len(S) < 3:
            return 0

        nums = sorted(S)
        counts = 0
        for i in range(len(nums) - 1, -1, -1):
            left, right = 0, i - 1
            target = nums[i]

            while left < right:
                curt_sum = nums[left] + nums[right]
                if curt_sum <= target:
                    left += 1
                elif curt_sum > target:
                    counts += right - left
                    right -= 1

        return counts
