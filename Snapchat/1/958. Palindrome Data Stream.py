class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        results = []
        alphabet = [0 for _ in range(26)]
        count = 0

        for char in s:
            alphabet[ord(char) - ord('a')] += 1

            # 奇数
            if alphabet[ord(char) - ord('a')] & 1:
                count += 1
            # 偶数
            else:
                count -= 1

            results.append(0 if count > 1 else 1)

        return results
