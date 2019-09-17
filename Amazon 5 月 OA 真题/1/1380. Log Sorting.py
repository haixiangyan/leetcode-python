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

        result = []
        # 字符
        for log in sortedLogs:
            index = log.find(' ')
            if log[index + 1].isalpha():
                result.append(log)

        # 数字
        for log in logs:
            index = log.find(' ')
            if not log[index + 1].isalpha():
                result.append(log)

        return result
