from collections import deque


def task_order(tasks):
    indegrees = {}
    graph = {}
    for relation in tasks:
        a, b = relation
        if a not in indegrees:
            indegrees[a] = 0
        if b not in indegrees:
            indegrees[b] = 0
        indegrees[b] += 1

        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)

    queue = deque([task for task in graph if indegrees[task] == 0])
    order = []
    while queue:
        level = []
        for _ in range(len(queue)):
            curt_task = queue.popleft()
            level.append(curt_task)

            for next_task in graph[curt_task]:
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
