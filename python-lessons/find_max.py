def find_max(numbers):
    largest = 0
    if len(numbers) >= 2:
        if numbers[0] < 0:
            largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

res = find_max([5, 1, 9, 0])
print(res)
