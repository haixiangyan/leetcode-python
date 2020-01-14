class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        sets = []
        self.dfs(s, sets, [])
        return sets

    def dfs(self, s, sets, path):
        if s == '':
            sets.append(path[:])
            return

        for i in range(2):
            if i + 1 <= len(s):
                path.append(s[:i + 1])
                self.dfs(s[i + 1:], sets, path)
                path.pop()
