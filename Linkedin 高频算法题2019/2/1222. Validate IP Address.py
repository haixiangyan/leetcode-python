class Solution:
    """
    @param IP: the given IP
    @return: whether an input string is a valid IPv4 address or IPv6 address or neither
    """
    def validIPAddress(self, IP):
        ip = IP.split('.')

        if len(ip) == 4:
            for item in ip:
                try:
                    num = int(item)
                except ValueError:
                    return 'Neither'
                if num < 0 or num > 255 or (item != '0' and (num // (10 ** (len(item) - 1)) == 0)):
                    return 'Neither'
            return 'IPv4'
        else:
            ip = IP.split(':')
            if len(ip) == 8:
                for item in ip:
                    if not item or len(item) > 4 or not item[0].isalnum():
                        return 'Neither'
                    try:
                        num = int(item, base=16)
                    except ValueError:
                        return 'Neither'
                    if num < 0 or num > 65535:
                        return 'Neither'
                return 'IPv6'
        return 'Neither'
