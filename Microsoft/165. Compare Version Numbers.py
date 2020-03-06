class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v_list1, v_list2 = version1.split('.'), version2.split('.')
        l1, l2 = len(v_list1), len(v_list2)

        for i in range(max(l1, l2)):
            v1 = int(v_list1[i]) if l1 > i else 0
            v2 = int(v_list2[i]) if l2 > i else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
