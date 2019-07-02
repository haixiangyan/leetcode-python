class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        length = len(numbers)
        closest_sum = float("inf")

        numbers.sort()

        if length < 3:
            return closest_sum

        for i in range(length - 2):
            if numbers[i] == numbers[i - 1]:
                continue

            left, right = i + 1, length - 1
            while left < right:
                three_sum = numbers[i] + numbers[left] + numbers[right]
                # Update when diff is smaller
                if abs(target - three_sum) < abs(target - closest_sum):
                    closest_sum = three_sum

                # Update left and right
                if three_sum < target:
                    left += 1
                elif three_sum > target:
                    right -= 1
                else:
                    return three_sum

        return closest_sum
