class Solution:
    def myPow(self, x: float, n: int) -> float:
        # write your code here
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        temp = self.myPow(x, n // 2)

        result = temp * temp

        if n % 2 == 1:
            result = result * x

        return result
