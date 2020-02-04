def calculator(s):
    if not s:
        return 0

    result, number, sign = 0, 0, 1
    for char in s:
        if char.isdigit():
            number = 10 * number + int(char)
        elif char == '+':
            result += sign * number
            sign, number = 1, 0
        elif char == '-':
            result += sign * number
            sign, number = -1, 0
    result += sign * number
    return result

str = '2+3-999'
print(calculator(str))
