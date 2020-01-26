def calculator(str):
    if not str:
        return 0

    result, num, sign = 0, 0, 1
    for char in str:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            result += sign * num
            sign = 1 if char == '+' else -1
            num = 0
    result += sign * num

    return result

str = '2+3-999'
print(calculator(str))