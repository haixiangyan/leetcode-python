class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
        self.islands = set()
        self.counts = 0
        self.fathers = {}

    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        results = []

        for point in operators:
            x, y = point.x, point.y

            if (x, y) in self.islands:
                results.append(self.counts)
                continue

            self.islands.add((x, y))
            self.fathers[(x, y)] = (x, y)
            self.counts += 1
            # 找相邻的点
            for delta in range(4):
                next_x, next_y = x + self.dx[delta], y + self.dy[delta]

                # 判断是否已经是个 island
                if (next_x, next_y) in self.islands:
                    self.union((next_x, next_y), (x, y))

            results.append(self.counts)

        return results


    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.fathers[root_a] = root_b
            self.counts -= 1

    def find(self, node):
        path = []

        while node != self.fathers[node]:
            path.append(node)
            node = self.fathers[node]

        for p in path:
            self.fathers[p] = node

        return node
