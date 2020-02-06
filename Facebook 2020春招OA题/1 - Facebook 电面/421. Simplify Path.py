class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        paths = path.split('/')
        stack = []

        for p in paths:
            if p == '..':
                if stack:
                    stack.pop()
            elif p != '.' and p != '':
                stack.append(p)

        return '/' + '/'.join(stack)
