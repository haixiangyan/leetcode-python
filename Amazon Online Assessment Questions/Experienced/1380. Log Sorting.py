import functools
class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        def compare(a, b):
            index_a, index_b = a.find(' '), b.find(' ')
            id_a, id_b = a[:index_a], b[:index_b]
            content_a, content_b = a[index_a + 1:], b[index_b + 1:]

            if content_a == content_b:
                return 1 if id_a > id_b else -1
            else:
                return 1 if content_a > content_b else -1

        # Sort the logs first
        sorted_logs = sorted(logs, key=functools.cmp_to_key(compare))

        results = []

        # Letter content should be placed in the first
        for log in sorted_logs:
            index = log.find(' ')
            if log[index + 1].isalpha():
                results.append(log)

        # If it's number, then append to results
        for log in logs:
            index = log.find(' ')
            if not log[index + 1].isalpha():
                results.append(log)

        return results
