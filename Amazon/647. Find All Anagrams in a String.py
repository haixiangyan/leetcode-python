class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        ans = []
        ls = len(s)
        lp = len(p)

        s_list = [0 for _ in range(26)]
        p_list = [0 for _ in range(26)]

        for i in range(lp):
            p_list[ord(p[i]) - ord('a')] += 1

        for i in range(ls):
            if i >= lp:
                s_list[ord(s[i - lp]) - ord('a')] -= 1
            s_list[ord(s[i]) - ord('a')] += 1

            if s_list == p_list:
                ans.append(i - lp + 1)

        return ans
