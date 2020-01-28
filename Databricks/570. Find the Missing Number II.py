class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        return self.dfs(n, 0, str, used)

    def dfs(self, n, index, str, used):
        if index == len(str):
            results = []
            for i in range(1, n + 1):
                if not used[i]:
                    results.append(i)
            return results[0] if len(results) == 1 else -1

        if str[index] == '0':
            return -1

        for l in range(1, 3):
            num = int(str[index : index + l])
            if 1 <= num <= n and not used[num]:
                used[num] = True
                target = self.dfs(n, index + l, str, used)
                if target != -1:
                    return target
                used[num] = False

        return -1
