def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    count = 0
    for interval in intervals:
        if len(result) == 0 or result[-1][1] <= interval[0]:
            count += 1
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return count

def arrange(arrival, duration):
    intervals = []

    for i in range(len(arrival)):
        intervals.append([arrival[i], arrival[i] + duration[i]])

    return merge(intervals)

arrival = [1, 3, 3, 5, 7]
duration = [2, 2, 1, 2, 1]
print(arrange(arrival, duration))