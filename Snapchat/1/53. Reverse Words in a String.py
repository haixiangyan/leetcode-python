import re
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        words = re.findall('([a-zA-Z!@#$%^&*()?]+)', s)
        return ' '.join(reversed(words))
