class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if numbers is None:
            return []

        results = []
        length = len(numbers)

        # Sort list
        numbers.sort()

        for i in range(length - 2):
            if numbers[i] == numbers[i - 1]:
                continue
            self.two_sum(numbers, i + 1, length - 1, -numbers[i], results)

        return results

    def two_sum(self, numbers, left, right, target, results):
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                # Found it, add to result list
                results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1

                # Remove duplicates
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
