class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if not numbers or len(numbers) < 3:
            return 0

        numbers = sorted(numbers)
        closest = float('inf')
        n = len(numbers)

        for i in range(n - 2):
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                curt_sum = numbers[i] + numbers[left] + numbers[right]

                if abs(curt_sum - target) < abs(closest - target):
                    closest = curt_sum

                if curt_sum < target:
                    left += 1
                elif curt_sum > target:
                    right -= 1
                else:
                    return target

        return closest
