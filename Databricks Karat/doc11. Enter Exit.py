def find_invalid(badge_records):
    status = {}
    for record in badge_records:
        name, curt_status = record
        if name not in status:
            status[name] = 0

        status[name] += 1 if curt_status == 'enter' else -1

    return [name for name in status if status[name] != 0]

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
