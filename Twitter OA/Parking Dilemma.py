def carParkingRoof(cars, k):
    result = float("inf")

    n = len(cars)
    # Sorting the array.
    cars.sort()

    # Find minimum value among
    # all K size subarray.
    for i in range(n - k + 1):
        result = int(min(result, cars[i + k - 1] - cars[i] + 1))
    return result

cars = [2, 10, 8, 17]
k = 3
print(carParkingRoof(cars, k))
