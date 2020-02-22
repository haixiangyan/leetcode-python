class Solution:
    def rand10(self):
        while True:
            rand49 = (self.rand7() - 1) * 7 + self.rand7() - 1
            if rand49 <= 39:
                return rand49 // 4 + 1

    def rand7(self):
        return 0
