def find_invalid(badge_records):
    status = {}

    for record in badge_records:
        name, move = record
        status[name] = status.get(name, 0) + (1 if move == 'enter' else -1)

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
