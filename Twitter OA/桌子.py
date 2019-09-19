def solution(positions, heights):
    maxHeight = 0

    for i in range(1, len(positions)):
        positionsDiff = positions[i] - positions[i - 1]
        heightDiff = heights[i] - heights[i - 1]
        if positionsDiff == 1:
            continue

        if positionsDiff <= heightDiff:
            curtHeight = min(heights[i], heights[i - 1]) + positionsDiff - 1
            maxHeight = max(maxHeight, curtHeight)
        else:
            curtHeight = max(heights[i], heights[i - 1]) + (positionsDiff - heightDiff) // 2
            maxHeight = max(maxHeight, curtHeight)

    return maxHeight


positions = [1, 2, 4, 7]
heights = [4, 5, 7, 11]
print(solution(positions, heights))