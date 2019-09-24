# Complete the compute_number_score function below.
def compute_number_score(number):
    score = 0

    # Rule 1
    temp = str(number)
    for char in temp:
        if int(char) == 9:
            score += 4

    print(1, score)

    # Rule 2
    temp = str(number)
    start, end = 0, 0
    for _ in temp:
        if temp[start] != temp[end] != 1:
            score += (end - start - 1) * 5
            start = end
        end += 1
    print(2, score)

    # Rule 3
    temp = str(number)
    start, end = 0, 1
    pointer = 0
    while end < len(temp):
        if int(temp[pointer]) + 1 == int(temp[end]):
            pointer += 1
            end += 1
        else:
            print('res', pow(end - start, 2))
            score += pow(end - start, 2)
            start = end
            pointer += 1
            end += 1
            print('jjj', score)

    print('res', pow(end - start, 2))
    score = score + pow(end - start, 2)

    print(3, score)

    # Rule 4
    if number % 7 == 0:
        score += 1
    print(4, score)

    # Rule 5
    temp = str(number)
    for char in temp:
        if int(char) % 2 == 0:
            score += 2
    print(5, score)

    return score



number = 2395456
print(compute_number_score(number))