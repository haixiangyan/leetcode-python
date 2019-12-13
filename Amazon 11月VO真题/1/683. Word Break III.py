class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        if not s:
            return 0

        max_length, lower_dict = self.start(dict)

        return self.memo_search(0, s.lower(), lower_dict, max_length, {})

    def start(self, dict):
        max_length = 0
        lower_dict = set()

        for token in dict:
            max_length = max(max_length, len(token))
            lower_dict.add(token.lower())

        return max_length, lower_dict

    def memo_search(self, index, s, lower_dict, max_length, memo):
        if index == len(s):
            return 1

        if index in memo:
            return memo[index]

        memo[index] = 0
        for i in range(index, len(s)):
            if i + 1 - index > max_length:
                break

            word = s[index:i + 1]

            if word not in lower_dict:
                continue
            memo[index] += self.memo_search(i + 1, s, lower_dict, max_length, memo)

        return memo[index]
