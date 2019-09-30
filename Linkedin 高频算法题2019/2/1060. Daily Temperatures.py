class Solution:
    """
    @param temperatures: a list of daily temperatures
    @return: a list of how many days you would have to wait until a warmer temperature
    """
    def dailyTemperatures(self, temperatures):
        if not temperatures:
            return [0]
        n = len(temperatures)
        stack = []
        results = [0 for _ in range(n)]
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return results