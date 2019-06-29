class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        if numbers is None:
            return [-1, -1]

        number_hash = {}

        for i, number in enumerate(numbers):
            offset = target - number
            if offset in number_hash:
                return [number_hash[offset], i]

            number_hash[number] = i

        return [-1, -1]
