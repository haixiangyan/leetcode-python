class Solution:
    def username_system(self, names):
        store = {}
        results = []

        for name in names:
            if name not in store:
                store[name] = 0
            else:
                store[name] += 1

            results.append(name + ('' if store[name] == 0 else str(store[name])))

        return results


s = Solution()
names = ['bob', 'alice', 'bob', 'alice', 'bob']
print(s.username_system(names))
