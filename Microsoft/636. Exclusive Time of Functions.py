class Solution:
    def exclusiveTime(self, n: int, logs):
        if not logs:
            return []

        stack = []
        results = [0 for _ in range(n)]

        last_time = 0
        for log in logs:
            id, state, time = log.split(':')
            id, time = int(id), int(time)

            if state == 'start':
                if stack:
                    results[stack[-1]] += time - last_time
                stack.append(id)
            else:
                time += 1
                results[stack.pop()] += time - last_time
            last_time = time
        return results
