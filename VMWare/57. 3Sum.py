class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if not numbers or len(numbers) < 3:
            return []

        numbers = sorted(numbers)
        results = []
        n = len(numbers)

        for i in range(n - 2):
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue

            self.find_two_sum(numbers, i + 1, n - 1, -numbers[i], results)

        return results

    def find_two_sum(self, numbers, left, right, target, results):
        while left < right:
            curt_sum = numbers[left] + numbers[right]
            if curt_sum < target:
                left += 1
            elif curt_sum > target:
                right -= 1
            else:
                results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left - 1] == numbers[left]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
