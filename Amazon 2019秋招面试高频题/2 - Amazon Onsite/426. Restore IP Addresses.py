class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        ips = []
        self.dfs(s, 0, ips, '')
        return ips

    def dfs(self, s, part, ips, ip):
        if part == 4:
            if s == '':
                ips.append(ip[1:])
                return

        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], part + 1, ips, ip + '.' + s[:i])
                if s[0] == '0':
                    break