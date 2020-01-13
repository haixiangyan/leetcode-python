class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        stack = []
        start, longest = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i + 1
                else:
                    stack.pop()
                    if not stack:
                        longest = max(longest, i - start + 1)
                    else:
                        longest = max(longest, i - stack[-1])

        return longest
