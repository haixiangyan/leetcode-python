# We are working on a security system for a badged-access room in our company's building.
# Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:
# 1. All employees who didn't use their badge while exiting the room – they recorded an enter without a matching exit.
# exit = -1, enter = 1;
#  badge_records = [
#    ["Martha",   "exit"],-google 1point3acres
#    ["Paul",     "enter"],. 1point3acres.com/bbs
#    ["Martha",   "enter"],
#    ["Martha",   "exit"],
#    ["Jennifer", "enter"],. more info on 1point3acres.com
#    ["Paul",     "enter"],. From 1point 3acres bbs
#    ["Curtis",   "enter"],
#    ["Paul",     "exit"],. visit 1point3acres.com for more.
#    ["Martha",   "enter"],
#    ["Martha",   "exit"],
#    ["Jennifer", "exit"],. 鐗涗汉浜戦泦,涓€浜╀笁鍒嗗湴
#  ]
def find_invalid(badge_records):
    status = {}
    for record in badge_records:
        name, curt_status = record

        if name not in status:
            status[name] = 0

        curt_status = 1 if curt_status == 'enter' else -1
        status[name] += curt_status

    invalids = []
    for name in status:
        if status[name] != 0:
            invalids.append(name)
    return invalids


badge_records = [
    ["Martha", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Paul", "enter"],
    ["Curtis", "enter"],
    ["Paul", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"],
]
print(find_invalid(badge_records))
