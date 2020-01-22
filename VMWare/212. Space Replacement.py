class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        if not length:
            return 0

        space = 0
        for char in string:
            if char == ' ':
                space += 1

        true_length = length + 2 * space
        index = true_length - 1

        for i in range(length - 1, -1, -1):
            if string[i] == ' ':
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1

        return true_length
