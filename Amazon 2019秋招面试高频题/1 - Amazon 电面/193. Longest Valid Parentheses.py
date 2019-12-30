class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        if not s:
            return 0
        # Store index of '('
        stack = []

        start = 0
        longest = 0

        for i in range(len(s)):
            # '(' -> append index to stack
            if s[i] == '(':
                stack.append(i)
            # ')'
            else:
                # If empty stack, Update start index
                if not stack:
                    start = i + 1
                # Not empty stack
                else:
                    # Pop most right '('
                    stack.pop()
                    # If empty stack, check i - start + 1
                    if not stack:
                        longest = max(longest, i - start + 1)
                    # If not empty stack, check i - (stack[-1] + 1) + 1
                    else:
                        longest = max(longest, i - stack[-1])
        return longest
