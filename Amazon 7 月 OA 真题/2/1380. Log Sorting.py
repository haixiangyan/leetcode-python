import functools


class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """

    def logSort(self, logs):
        if not logs:
            return

        def compare(a, b):
            indexA = a.find(' ')
            indexB = b.find(' ')

            idA, contentA = a[:indexA], a[indexA + 1:]
            idB, contentB = b[:indexB], b[indexB + 1:]

            if contentA != contentB:
                return 1 if contentA > contentB else -1
            else:
                return 1 if idA > idB else -1

        sortedLogs = sorted(logs, key=functools.cmp_to_key(compare))

        results = []
        # 字符
        for log in sortedLogs:
            index = log.find(' ')
            if log[index + 1].isalpha():
                results.append(log)

        for log in logs:
            index = log.find(' ')
            if not log[index + 1].isalpha():
                results.append(log)

        return results
