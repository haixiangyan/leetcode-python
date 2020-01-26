# 第一题：给广告在每个domain上被click的次数. 1point3acres.com/bbs
#              要求返回domain及其所有sub domain 被click的总次数
# 输入：[
#            ["google.com", "60"],
#            ["yahoo.com", "50"],
#            ["sports.yahoo.com", "80"]
#          ]
# 输出：[
#             ["com", "190"], (60+50+80)
#             ["google.com", "60"],
#             ["yahoo.com", "130"] (50+80)
#             ["sports.yahoo.com", "80"]
#          ]
def count_click(array):
    domain_to_counts = {}
    for item in array:
        url, count = item
        sub_domains = url.split('.')

        curt_domain = ''
        for i in range(len(sub_domains) - 1, -1, -1):
            curt_domain = sub_domains[i] + '.' + curt_domain if curt_domain != '' else sub_domains[i]
            domain_to_counts[curt_domain] = domain_to_counts.get(curt_domain, 0) + int(count)
    return domain_to_counts


array = [
    ["google.com", "60"],
    ["yahoo.com", "50"],
    ["sports.yahoo.com", "80"]
]
print(count_click(array))
