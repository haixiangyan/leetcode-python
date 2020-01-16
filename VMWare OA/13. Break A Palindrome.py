class Solution:
    def breakAPalindrome(self, palindrome):
        found = False
        index = 0

        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                index = i
                found = True

        if found:
            return palindrome[:index] + 'a' + palindrome[index + 1:]
        else:
            return 'IMPOSSIBLE'

s = Solution()
palindrome = 'abba'
print(s.breakAPalindrome(palindrome))
