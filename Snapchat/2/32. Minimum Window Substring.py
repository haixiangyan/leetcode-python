class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        targetHash = self.getHash(target)

        n = len(source)
        minLength = n + 1
        minString = ''

        windowHash = {}

        # 初始化窗口 Hash
        j = 0
        matchedChars, targetChars = 0, len(targetHash)
        while j < n and matchedChars < targetChars:
            if source[j] in targetHash:
                windowHash[source[j]] = windowHash.get(source[j], 0) + 1
                if windowHash[source[j]] == targetHash[source[j]]:
                    matchedChars += 1
            j += 1

        for i in range(n):
            if j - i < minLength and matchedChars == targetChars:
                minLength = j - i
                minString = source[i:j]

            if source[i] in windowHash:
                if windowHash[source[i]] == targetHash[source[i]]:
                    matchedChars -= 1
                windowHash[source[i]] -= 1

        return minString

    def getHash(self, str):
        resultHash = {}
        for char in str:
            resultHash[char] = resultHash.get(char, 0) + 1

        return resultHash