class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        miniDiff = float('inf')
        sortedNums = sorted(nums)

        left, right = 0, len(nums) - 1
        while left < right:
            curtSum = sortedNums[left] + sortedNums[right]

            if curtSum < target:
                left += 1
            elif curtSum > target:
                right -= 1
            else:
                return 0
            miniDiff = min(miniDiff, abs(target - curtSum))

        return miniDiff
