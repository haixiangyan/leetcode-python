# Time complexity: O(n)
# Space complexity: O(n)
def find_parent(edges):
    if not edges:
        return []

    parents = {}
    for edge in edges:
        parent, child = edge
        if child not in parents:
            parents[child] = 0
        if parent not in parents:
            parents[parent] = 0
        parents[child] += 1

    results = []
    for child in parents:
        if parents[child] <= 1:
            results.append(child)
    return results

edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
print(find_parent(edges))
