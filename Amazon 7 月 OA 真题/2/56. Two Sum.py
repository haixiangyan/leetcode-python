class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        store = {}

        for index, num in enumerate(numbers):
            if (target - num) in store:
                return [
                    min(index, store[target - num]),
                    max(index, store[target - num]),
                ]

            store[num] = index

        return [-1, -1]
