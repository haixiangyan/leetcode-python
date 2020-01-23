class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if not numbers or len(numbers) < 4:
            return []

        numbers = sorted(numbers)
        results = []
        n = len(numbers)
        for i in range(n - 3):
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue
            self.find_three_sum(numbers[i], numbers, i + 1, target - numbers[i], n, results)

        return results

    def find_three_sum(self, first, numbers, start, target, n, results):
        for i in range(start, n - 2):
            if i > start and numbers[i - 1] == numbers[i]:
                continue
            self.find_two_sum(first, numbers[i], numbers, i + 1, n - 1, target - numbers[i], results)

    def find_two_sum(self, first, second, numbers, left, right, target, results):
        while left < right:
            curt_sum = numbers[left] + numbers[right]
            if curt_sum < target:
                left += 1
            elif curt_sum > target:
                right -= 1
            else:
                results.append([first, second, numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left - 1] == numbers[left]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
