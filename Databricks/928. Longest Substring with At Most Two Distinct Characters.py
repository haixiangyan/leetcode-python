class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0

        most_right = {}
        most_left, right, longest = 0, 0, 0

        while right < len(s):
            if len(most_right) <= 2:
                most_right[s[right]] = right
                right += 1
            if len(most_right) > 2:
                # Find most left
                left = len(s)
                for value in most_right.values():
                    left = min(left, value)
                most_right.pop(s[left])
                most_left = left + 1
            longest = max(longest, right - most_left)
        return longest
