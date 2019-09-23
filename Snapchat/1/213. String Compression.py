class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        if not originalString:
            return ''
        if len(originalString) == 1:
            return originalString

        start, end = 0, 0
        newString = ''
        for end in range(len(originalString)):
            if originalString[start] != originalString[end]:
                newString += originalString[start] + str(end - start)
                start = end

        # 最后一次
        newString += originalString[start] + str(end - start + 1)

        if len(newString) >= len(originalString):
            return originalString

        return newString
