import functools

class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        def compare(a, b):
            indexA, indexB = a.find(' '), b.find(' ')
            idA, idB = a[:indexA], b[:indexB]
            contentA, contentB = a[indexA + 1:], b[indexB + 1:]

            if contentA == contentB:
                return 1 if idA > idB else -1
            else:
                return 1 if contentA > contentB else -1


        sortedLogs = sorted(logs, key=functools.cmp_to_key(compare))

        results = []

        for log in sortedLogs:
            index = log.find(' ')
            if log[index + 1].isalpha():
                results.append(log)

        for log in logs:
            index = log.find(' ')
            if not log[index + 1].isalpha():
                results.append(log)

        return results
