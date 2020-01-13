from collections import deque
class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns
    """
    def openLock(self, deadends, target):
        deadend_set = set()
        start = '0000'

        for end in deadends:
            if start == end:
                return -1
            deadend_set.add(end)

        queue = deque([start])
        visited = {start}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                curt = queue.popleft()
                if curt == target:
                    return steps

                for next_lock in self.get_next_locks(curt, deadend_set, visited):
                    queue.append(next_lock)
                    visited.add(next_lock)

            steps += 1
        return -1

    def get_next_locks(self, curt, deadend_set, visited):
        next_locks = []
        for i in range(4):
            next_lock = curt + ''
            origin = str(next_lock[i])

            # + 1
            next_lock = next_lock[:i] + str((int(origin) + 1) % 10) + next_lock[i + 1:]
            if next_lock not in deadend_set and next_lock not in visited:
                next_locks.append(next_lock)

            # - 1
            next_lock = next_lock[:i] + str((int(origin) + 10 - 1) % 10) + next_lock[i + 1:]
            if next_lock not in deadend_set and next_lock not in visited:
                next_locks.append(next_lock)

        return next_locks
