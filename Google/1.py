def solution(flowers, cap1, cap2):
    if not flowers:
        return 0

    times = 0
    left, right = 0, len(flowers) - 1
    can1, can2 = 0, 0
    while left < right:
        # Refill
        if flowers[left] > can1:
            times += 1
            can1 = cap1
        if flowers[right] > can2:
            times += 1
            can2 = cap2

        can1 -= flowers[left]
        left += 1

        can2 -= flowers[right]
        right -= 1

    # Last round
    if left == right and flowers[left] > can1 + can2:
        times += 1

    return times

flowers = [1, 1, 1, 1, 1]
cap1 = 5
cap2 = 100

print(solution(flowers, cap1, cap2))
