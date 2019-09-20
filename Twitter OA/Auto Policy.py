def finalInstances(instances, averageUtil):
    # Write your code here
    lowerLimit, upperLimit, lower, upper, idle = 1, int(1e8), 25, 60, 10
    n, results = len(averageUtil), instances
    i = 0
    while i < n:
        if averageUtil[i] < lower and results > lowerLimit:
            results, i = (results + 1) // 2, i + idle
        elif averageUtil[i] > upper and results <= upperLimit:
            results, i = results * 2, i + idle
        i += 1
    return results
