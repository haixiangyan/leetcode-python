def triplets(t, d):
    results = 0
    d.sort()
    n = len(d)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            if d[i] + d[left] + d[right] <= t:
                results += right - left
                left += 1
            else:
                right -= 1
    return results

d = [3, 1, 2, 4]
t = 7
print(triplets(t, d))
