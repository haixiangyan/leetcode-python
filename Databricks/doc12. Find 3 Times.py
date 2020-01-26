import heapq


def find_3_times(records):
    status = {}
    results = {}
    # Get status
    for record in records:
        name, time = record
        if name not in status:
            status[name] = []
        heapq.heappush(status[name], time)

    # Get results
    for name in status:
        for i, time in enumerate(status[name]):
            if len(status[name]) < 3:
                continue
            # status[name][index] not included
            index = find(status[name], get_target(time))
            if index - i < 3:
                continue
            else:
                results[name] = status[name][i:index]
                break

    return results

def get_target(time):
    hours, mins = time // 100, time % 100
    return (hours + ((mins + 60) // 60)) * 100 + (mins + 60) % 60

def find(times, target):
    left, right = 0, len(times) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if times[mid] <= target:
            left = mid
        else:
            right = mid

    if times[left] > target:
        return left
    if times[right] > target:
        return right
    return -1


records = [
    ["Paul", 1355],
    ["Jennifer", 1910],
    ["John", 830],
    ["Paul", 1315],
    ["John", 835],
    ["Paul", 1405],
    ["Paul", 1630],
    ["John", 855],
    ["John", 915],
    ["John", 930],
    ["Jennifer", 1335],
    ["Jennifer", 730],
    ["John", 1630],
]
print(find_3_times(records))
