class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        if not nestedList:
            return 0

        order = []
        curt_list = nestedList

        while curt_list:
            level = []
            next_list = []

            for item in curt_list:
                if item.isInteger():
                    level.append(item.getInteger())
                else:
                    next_list += item.getList()

            order.append(level)
            curt_list = next_list

        result, weight = 0, 1
        while order:
            result += weight * sum(order.pop())
            weight += 1
        return result
