class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        numbers.sort()

        length = len(numbers)
        results = []
        if length < 4:
            return results

        for i in range(length - 3):
            if i and numbers[i] == numbers[i - 1]:
                continue

            for j in range(i + 1, length - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]:
                    continue

                left, right = j + 1, length - 1
                new_target = target - numbers[i] - numbers[j]
                while left < right:
                    if numbers[left] + numbers[right] > new_target:
                        right -= 1
                    elif numbers[left] + numbers[right] < new_target:
                        left += 1
                    else:
                        results.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1
                        right -= 1

                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1
        return results
