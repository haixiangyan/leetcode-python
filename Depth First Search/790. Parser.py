from collections import deque
from collections import defaultdict
class Solution:
    """
    @param generator: Generating set of rules.
    @param startSymbol: Start symbol.
    @param symbolString: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    def canBeGenerated(self, generator, startSymbol, symbolString):
        graph = defaultdict(list)

        for edge in generator:
            parent, child = edge.split('->')
            graph[parent].append(child)

        queue = deque([list(startSymbol)])
        target = list(symbolString)

        while queue:
            curt = queue.popleft()
            if curt == target:
                return True

            for i in range(len(curt)):
                char = curt[i]
                if char in graph:
                    for next_str in graph[char]:
                        # 去环，如 S -> aS, cc 变成 S -> acc, cc
                        if char in next_str:
                            next_str = next_str.replace(char, graph[char][-1])
                        curt[i] = next_str
                        queue.append(list(''.join(curt)))
        return False
