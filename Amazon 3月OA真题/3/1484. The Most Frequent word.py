import re
class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        store = {}
        mostAppear, result = 0, ''

        s = ' ' + s
        tokens = re.findall(r'\b\S+\b', s)

        for token in tokens:
            # 排除字典里的 token
            if token in excludewords:
                continue
            # 计数
            if token not in store:
                store[token] = 0
            store[token] += 1

            if store[token] > mostAppear:
                mostAppear = store[token]
                result = token
            elif store[token] == mostAppear:
                result = token if token < result else result

        return result
