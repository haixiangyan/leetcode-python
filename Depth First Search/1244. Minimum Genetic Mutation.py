from collections import deque
class Solution:
    """
    @param start:
    @param end:
    @param bank:
    @return: the minimum number of mutations needed to mutate from "start" to "end"
    """
    def minMutation(self, start, end, bank):
        queue = deque([start])
        visited = {start}
        steps = 0

        while queue:
            string = queue.popleft()

            if string == end:
                return steps

            for next_string in self.find_next_strings(string, bank, visited):
                visited.add(next_string)
                queue.append(next_string)

            steps += 1
        return -1

    def find_next_strings(self, string, bank, visited):
        gene = ['A', 'C', 'T', 'G']
        next_strings = []

        for i in range(len(string)):
            for j in range(4):
                if gene[j] == string[i]:
                    continue

                next_string = string[:i] + gene[j] + string[i + 1:]

                if next_string not in visited and next_string in bank:
                    next_strings.append(next_string)
        return next_strings
