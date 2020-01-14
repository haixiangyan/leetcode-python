class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        if not s:
            return 0

        if len(s) < k:
            return len(s)

        max_count, result, left = 0, 0, 0
        counts = {}

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1

            max_count = max(max_count, counts[s[right]])

            if right - left + 1 - max_count> k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
