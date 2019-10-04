class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        if not string:
            return length

        spaces = 0
        for char in string:
            if char == ' ':
                spaces += 1

        newLength = length + spaces * 2
        index = newLength - 1
        for i in range(length - 1, -1, -1):
            if string[i] == ' ':
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1

        return newLength
