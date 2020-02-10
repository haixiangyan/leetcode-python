class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        visited = [False for _ in range(n + 1)]
        return self.find(n, str, 0, visited)

    def find(self, n, str, index, visited):
        if index == len(str):
            results = []
            for i in range(1, n + 1):
                if not visited[i]:
                    results.append(i)
            return results[0] if len(results) == 1 else -1

        if str[index] == '0':
            return -1

        for offset in range(1, 3):
            num = int(str[index: index + offset])
            if 1 <= num <= n and not visited[num]:
                visited[num] = True
                target = self.find(n, str, index + offset, visited)
                if target != -1:
                    return target
                visited[num] = False
        return -1
