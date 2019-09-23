import re
class Solution:
    """
    @param str: The input string
    @return: The answer
    """
    def dataSegmentation(self, str):
        return re.findall('([a-zA-Z]+|[()#,.@!$%^&*])', str)
