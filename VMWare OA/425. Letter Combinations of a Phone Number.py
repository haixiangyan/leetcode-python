KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []

        results = []

        self.dfs(0, '', digits, results)

        return results

    def dfs(self, index, curt, digits, results):
        if index == len(digits):
            results.append(curt)
            return

        for char in KEYBOARD[digits[index]]:
            self.dfs(index + 1, curt + char, digits, results)
