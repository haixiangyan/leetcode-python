class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """

    def canPlaceFlowers(self, flowerbed, n):
        if not flowerbed:
            return False

        i = 0
        size = len(flowerbed)

        if size < 3:
            return 1 not in flowerbed

        while i < size - 1:
            # 初始
            if i == 0:
                i += 1
                continue
            # 放花
            if self.isLeftValid(i - 1, flowerbed) and flowerbed[i] == 0 and self.isRightValid(i + 1, size, flowerbed):
                flowerbed[i] = 1
                n -= 1
                i += 2
            # 不放花
            else:
                i += 1
        return n == 0

    def isLeftValid(self, left, flowerbed):
        return left < 0 or flowerbed[left] == 0

    def isRightValid(self, right, size, flowerbed):
        return right >= size or flowerbed[right] == 0
