class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        source_length = len(source)
        target_length = len(target)

        for i in range(source_length - target_length + 1):
            j = 0

            while j < target_length:
                if source[i + j] != target[j]:
                    break
                j += 1

            if j == target_length:
                return i

        return -1
