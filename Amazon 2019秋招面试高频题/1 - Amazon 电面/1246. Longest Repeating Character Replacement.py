class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        if not s:
            return 0

        if k > len(s):
            return len(s)

        counts = {}
        max_count, left, result = 0, 0, 0

        # Find right index
        for right in range(len(s)):
            # Count right index char number
            counts[s[right]] = counts.get(s[right], 0) + 1
            # Calculate maximum char number
            max_count = max(max_count, counts[s[right]])

            # If len - max_count > K, then move left index
            if right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1

            # Calculate current maximum length
            result = max(result, right - left + 1)

        return result
