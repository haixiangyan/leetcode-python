from heapq import heappush


def find_3_times(records):
    name_to_times = {}
    for record in records:
        name, time = record
        if name not in name_to_times:
            name_to_times[name] = []
        heappush(name_to_times[name], time)

    results = {}
    for name in name_to_times:
        times = name_to_times[name]

        if len(times) < 3:
            continue

        for i, time in enumerate(times):
            index = find(i, get_target(time), times, len(times))
            if index - i < 3:
                continue
            else:
                results[name] = times[i:index]
                break
    return results


def get_target(time):
    hours, mins = time // 100, time % 100
    mins_carrier, mins_remainder = (mins + 60) // 60, (mins + 60) % 60
    return (hours + mins_carrier) * 100 + mins + mins_remainder

def find(start, target, nums, n):
    left, right = start, n - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
    if nums[left] > target:
        return left
    if nums[right] > target:
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
