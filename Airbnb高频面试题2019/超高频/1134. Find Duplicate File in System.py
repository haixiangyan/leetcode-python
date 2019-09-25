class Solution:
    """
    @param paths: a list of string
    @return: all the groups of duplicate files in the file system in terms of their paths
    """
    def findDuplicate(self, paths):
        store = {}

        for path in paths:
            index = path.find(' ')
            p = path[:index]
            files = path[index + 1:].split(' ')

            for file in files:
                fileName = file[:file.find('(')]
                content = file[file.find('(') + 1:len(file) - 1]
                if content not in store:
                    store[content] = []
                store[content].append(p + '/' + fileName)

        results = []
        for content in store:
            if len(store[content]) != 1:
                results.append(store[content])

        return results
