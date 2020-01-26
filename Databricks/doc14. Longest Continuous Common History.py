# 输入： [
#              ["3234.html", "xys.html", "7hsaa.html"], // user1
#              ["3234.html", ''sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
#            ], user1 and user2 （指定两个user求intersect）
#
# 输出：["xys.html", "7hsaa.html"]-google 1po
#
# user0 = [ "/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html" ]
# user2 = [ "/nine.html", "/two.html", "/three.html", "/four.html", "/six.html", "/seven.html" ]
# user1 = [ "/one.html", "/two.html", "/three.html", "/four.html", "/six.html" ]
# user3 = [ "/three.html", "/eight.html" ]. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴
#
# Sample output:
#
# (user0, user2):
#    /four.html
#    /six.html
#    /seven.html
#
# (user1, user2):. visit 1point3acres.com for more.
#    /two.html
#    /three.html
#    /four.html
#    /six.html
#
# (user0, user3):
#    None. 鍥磋鎴戜滑@1point 3 acres
#
# (user1, user3):
#    /three.htmlint3acres
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

            if dp[i][j] > right:
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