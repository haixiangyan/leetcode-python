class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """

    def KSubstring(self, stringIn, K):
        if not stringIn or len(stringIn) < K:
            return 0

        store = {}
        substrings = set([])
        count = 0

        # 初始化前 K 个
        for i in range(K):
            if stringIn[i] not in store:
                store[stringIn[i]] = 0
                count += 1

            store[stringIn[i]] += 1

        if count == K:
            substrings.add(stringIn[:K])

        for i in range(K, len(stringIn)):
            # 去掉前面的字符
            store[stringIn[i - K]] -= 1
            if store[stringIn[i - K]] == 0:
                count -= 1

            # 加上后面的新字符
            if stringIn[i] not in store or store[stringIn[i]] == 0:
                count += 1
                store[stringIn[i]] = 0
            store[stringIn[i]] += 1

            # 判断是否是一个合格的子串
            if count == K:
                substrings.add(stringIn[i - K + 1:i + 1])

        return len(substrings)
