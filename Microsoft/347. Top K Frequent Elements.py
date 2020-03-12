class Solution:
    def topKFrequent(self, nums, k):
        store = {}

        for num in nums:
            store[num] = store.get(num, 0) + 1

        sorted_store = sorted(store.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_store[i][0])

        return result
