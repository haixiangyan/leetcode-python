import collections
class TimeMap:

    def __init__(self):
        self.values = collections.defaultdict(list)
        self.times = collections.defaultdict(list)
        self.length = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ''

        index = self.binary_search(self.times[key], timestamp)

        return self.values[key][index] if index != -1 else ''

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        if nums[right] <= target:
            return right
        if nums[left] <= target:
            return left
        return -1


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)