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
            if target - numbers[i] in store:
                return [store[target - numbers[i]], i]
            else:
                store[numbers[i]] = i

        return [-1, -1]