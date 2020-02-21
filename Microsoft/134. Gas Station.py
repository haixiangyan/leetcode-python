class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        gas_remain = 0

        for i in range(len(gas)):
            gas_remain += gas[i] - cost[i]
            if gas_remain < 0:
                gas_remain = 0
                start = i + 1

        return start
