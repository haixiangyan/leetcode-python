class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        size = len(words)
        index1, index2 = size, size

        result = size

        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
                result = min(result, abs(index1 - index2))
            elif words[i] == word2:
                index2 = i
                result = min(result, abs(index1 - index2))
        return result

