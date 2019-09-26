"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        if Guess.guess(n) == 0:
            return n
        left, right = 0, n
        while left < right:
            middle = (left + right) // 2

            if Guess.guess(middle) < 0:
                right = middle
            elif Guess.guess(middle) > 0:
                left = middle
            else:
                return middle
        
        if left == n:
            return left
        if right == n:
            return right

        return -1
