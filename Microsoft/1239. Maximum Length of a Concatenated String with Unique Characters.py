class Solution:
    def __init__(self):
        self.max_len = 0

    def maxLength(self, arr):
        if not arr:
            return 0

        self.dfs(0, [], arr)

        return self.max_len

    def dfs(self, index, curt, arr):
        concatenate = ''.join(curt)

        if len(concatenate) == len(set(concatenate)):
            self.max_len = max(self.max_len, len(concatenate))
        if len(concatenate) > len(set(concatenate)):
            return

        for i in range(index, len(arr)):
            curt.append(arr[i])
            self.dfs(i + 1, curt, arr)
            curt.pop()
