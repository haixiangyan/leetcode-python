class Solution:
    def removeDuplicates(self, s, k):
        if k <= 1:
            return ''

        stack = []
        for char in s:
            if stack:
                if char in stack[-1].keys() and stack[-1][char] + 1 != k:
                    stack[-1][char] += 1
                elif char in stack[-1].keys() and stack[-1][char] + 1 == k:
                    stack.pop()
                else:
                    stack.append({char: 1})
            else:
                stack.append({char: 1})

        result = ''
        for item in stack:
            for key, value in item.items():
                result += key * value

        return result
