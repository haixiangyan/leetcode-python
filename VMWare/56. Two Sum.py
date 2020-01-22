class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if not numbers:
            return [-1, -1]

        store = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in store:
                return [min(store[diff], i), max(store[diff], i)]

            store[numbers[i]] = i

        return [-1, -1]
