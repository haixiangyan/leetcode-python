class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)

        def build_path(path, word):
            if len(pre_map[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0, word)
            for pre_word in pre_map[word]:
                build_path(path, pre_word)
            path.pop(0)

        length = len(start)
        pre_map = {}

        # 初始化 pre map
        for word in dict:
            pre_map[word] = []

        result = []
        current_level = set()
        current_level.add(start)

        while True:
            pre_level = current_level
            current_level = set()

            for pre_word in pre_level:
                dict.remove(pre_word)

            for pre_word in pre_level:
                for i in range(length):
                    left, right = pre_word[:i], pre_word[i + 1:]
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if pre_word[i] == char:
                            continue
                        next_word = left + char + right
                        if next_word in dict:
                            pre_map[next_word].append(pre_word)
                            current_level.add(next_word)

            if len(current_level) == 0:
                return []
            if end in current_level:
                break

        build_path([], end)
        return result