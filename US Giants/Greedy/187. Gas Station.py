class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        if gas is None or cost is None or len(gas) == 0 or len(cost) == 0:
            return -1

        interest_sum = 0
        total = 0
        index = -1

        for i in range(len(gas)):
            interest_sum += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if interest_sum < 0:
                index = i
                interest_sum = 0

        return -1 if total < 0 else index + 1
