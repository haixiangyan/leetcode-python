from collections import deque

class Solution:
    def string_chains(self, words):
        # Put words in set for accessing them quickly
        words = sorted(words, key=len)
        dict_set = set(words)
        memo = {}

        longest = 0

        for word in words:
            longest = max(longest, self.bfs(word, dict_set, memo))

        return longest

    def bfs(self, word, dict_set, memo):
        longest = 0
        queue = deque([word])
        length = 0

        while queue:
            length += 1

            for _ in range(len(queue)):
                curt_s = queue.popleft()
                for next_word in self.get_next_words(curt_s, dict_set):
                    if next_word not in memo:
                        queue.append(next_word)
                    else:
                        longest = max(longest, length + memo[next_word])

        memo[word] = max(longest, length)
        return memo[word]

    def get_next_words(self, curt_s, dict_set):
        next_words = []
        for i in range(len(curt_s)):
            next_word = curt_s[:i] + curt_s[i + 1:]
            if next_word in dict_set:
                next_words.append(next_word)

        return next_words


solution = Solution()

# 3
dictionary = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
print(solution.string_chains(dictionary))
