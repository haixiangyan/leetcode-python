from collections import deque
from collections import defaultdict
def task_order(tasks):
    graph = defaultdict(set)
    indegrees = {}

    for task in tasks:
        a, b = task

        graph[a].add(b)
        graph[b].add(a)

        indegrees[a] = indegrees.get(a, 0)
        indegrees[b] = indegrees.get(b, 0) + 1

    queue = deque([node for node in graph if indegrees[node] == 0])
    order = []
    while queue:
        level = []
        for _ in range(len(queue)):
            curt = queue.popleft()
            level.append(curt)
            for next_task in graph[curt]:
                indegrees[next_task] -= 1
                if indegrees[next_task] == 0:
                    queue.append(next_task)
        order.append(level)
    return order

tasks = [
    ["cook", "eat"],
    ["study", "eat"],
    ["sleep", "study"]
]
print(task_order(tasks))
