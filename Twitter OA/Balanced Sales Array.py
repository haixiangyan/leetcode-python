class Solution:
    """
    @param sales: a integer array
    @return: return a Integer
    """

    def BalancedSalesArray(self, sales):
        # write your code here

        for index in range(len(sales)):
            if sum(sales[0:index]) == sum(sales[index + 1: len(sales)]):
                return index
