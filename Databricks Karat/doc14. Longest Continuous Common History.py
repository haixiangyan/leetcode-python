def find_history(user1, user2):
    n, m = len(user1), len(user2)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    right, length = -1, 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if user1[i - 1] == user2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0

            if dp[i][j] > length:
                length = dp[i][j]
                right = i - 1

    results = []
    for i in range(right, right - length, -1):
        results.append(user1[i])
    results.reverse()
    return results

user1 = ["/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html"]
user2 = ["/nine.html", "/two.html", "/three.html", "/four.html", "/six.html", "/seven.html"]
print(find_history(user1, user2))
