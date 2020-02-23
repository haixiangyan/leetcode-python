class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        # 左，右
        if rec1[2] <= rec2[0] or rec1[0] >= rec2[2]:
            return False
        # 上，下
        if rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
            return False
        return True
