def max_total(arr, n, m):
    if len(arr) < 3:
        return sum(arr)

    for i in range(2, n):
        target_index = -1
        cur_memes = m
        for j in range(i - 2, i + 1):
            if arr[j] == -1:
                target_index = j
            else:
                cur_memes -= arr[j]

        if target_index != -1:
            if cur_memes <= 0:
                arr[target_index] = 0
            else:
                arr[target_index] = cur_memes
        else:
            print(arr[i], arr, cur_memes)
            if cur_memes > 0:
                return 'Impossible'
    return sum(arr)


test_num = int(input())

test_cases = []

for _ in range(test_num):
    [n, m] = list(map(int, input().split(' ')))

    test_cases.append({
        "n": n,
        "m": m,
        "arr": list(map(int, input().split(' ')))
    })

for t in test_cases:
    n, m, arr = t
    print(max_total(t["arr"], t["n"], t["m"]))
