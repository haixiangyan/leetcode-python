class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        n = len(pid)
        graph = {}

        for i in range(n):
            parent, child = ppid[i], pid[i]

            if child not in graph:
                graph[child] = []
            if parent not in graph:
                graph[parent] = []
            graph[parent].append(child)

        shutdown = set()
        self.dfs(kill, graph,  shutdown)
        return list(shutdown)

    def dfs(self, node, graph, shutdown):
        shutdown.add(node)

        for next_node in graph[node]:
            if next_node in shutdown:
                continue
            self.dfs(next_node, graph, shutdown)
