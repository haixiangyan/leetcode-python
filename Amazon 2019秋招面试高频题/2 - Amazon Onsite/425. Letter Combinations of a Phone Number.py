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

        self.dfs(digits, '', 0, results)

        return results

    def dfs(self, digits, curt, index, results):
        if index == len(digits):
            results.append(curt)
            return

        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, curt + letter, index + 1, results)