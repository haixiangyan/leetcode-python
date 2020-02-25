class Solution:
    def removeComments(self, source):
        codes = []
        open_black = False
        buffer = ''

        for line in source:
            i = 0
            while i < len(line):
                if line[i] == '/' and i + 1 < len(line) and line[i + 1] == '/' and not open_black:
                    i = len(line)
                elif line[i] == '/' and i + 1 < len(line) and line[i + 1] == '*' and not open_black:
                    open_black = True
                    i = i + 1
                elif line[i] == '*' and i + 1 < len(line) and line[i + 1] == '/' and open_black:
                    open_black = False
                    i = i + 1
                elif not open_black:
                    buffer += line[i]
                i += 1
            if buffer and not open_black:
                codes.append(buffer)
                buffer = ''
        return codes
