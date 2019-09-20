def maxHeight(tablePositions, tableHeights):
    if not tablePositions or not tableHeights:
        return 0

    result = 0
    for i in range(1, len(tablePositions)):
        distance = tablePositions[i] - tablePositions[i - 1] - 1
        curtMaxHeight = calHeight(distance, tableHeights[i], tableHeights[i - 1])
        result = max(result, curtMaxHeight)

    return result

def calHeight(distance, height1, height2):
    minHeight, maxHeight = min(height1, height2), max(height1, height2)

    if distance == 0:
        return 0
    if distance == 1:
        return minHeight + 1

    if minHeight == maxHeight:
        offset = distance // 2 if distance % 2 == 0 else distance // 2 + 1
        return minHeight + offset

    delta = maxHeight - minHeight
    if delta < distance:
        distance -= delta
        minHeight += delta
        offset = distance // 2 if distance % 2 == 0 else distance // 2 + 1
        return minHeight + offset

    return minHeight + distance
