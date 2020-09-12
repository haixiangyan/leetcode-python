class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []

        self.helper([], 1, k, n)

        return self.res

    def helper(self, curt, index, k, n):
        if k == 0:
            if sum(curt) == n:
                self.res.append(curt[:])
            return

        for i in range(index, 10):
            curt.append(i)
            if sum(curt) <= n:
                self.helper(curt, i + 1, k - 1, n)
            curt.pop()
