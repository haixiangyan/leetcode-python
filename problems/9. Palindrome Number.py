class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        input_num = x
        reverted_num = 0
        while x > 0:
            remainder = x % 10

            reverted_num = reverted_num * 10 + remainder

            x = x // 10

        return reverted_num == input_num
