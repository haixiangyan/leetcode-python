class Solution:
    """
    @param setList: The input set list
    @return: the cartesian product of the set list
    """
    def getSet(self, setList):
        sets = []

        self.dfs(0, [], setList, sets)

        return sets

    def dfs(self, depth, curt, set_list, sets):
        if depth == len(set_list):
            sets.append(curt[:])
            return

        for num in set_list[depth]:
            curt.append(num)
            self.dfs(depth + 1, curt, set_list, sets)
            curt.pop()
