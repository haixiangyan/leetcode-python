from collections import defaultdict
from collections import deque

class Solution:
    """
    @param x: The x
    @param y: The y
    @param a: The a
    @param b: The b
    @return: The Answer
    """
    def tree(self, x, y, a, b):
        graph = defaultdict(set)

        for i in range(len(x)):
            graph[x[i]].add(y[i])
            graph[y[i]].add(x[i])

        fathers = {1: -1}
        self.find_fathers(graph, 1, fathers)

        results = [0 for _ in range(len(a))]
        for i in range(len(a)):
            node1, node2 = a[i], b[i]

            if node1 not in fathers or node2 not in fathers:
                continue

            father1, father2 = fathers[node1], fathers[node2]
            if father1 == father2:
                results[i] = 1
            if father1 == node2 or father2 == node1:
                results[i] = 2

        return results

    def find_fathers(self, graph, root, fathers):
        visited = {root}
        queue = deque([root])

        while queue:
            node = queue.popleft()

            for next_node in graph[node]:
                if next_node in visited:
                    continue

                fathers[next_node] = node
                queue.append(next_node)
                visited.add(next_node)
