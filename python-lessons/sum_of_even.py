def sum_even_numbers(numbers):
    # TODO: return the sum of all even numbers in `numbers`
    if numbers is None:
        return 0
    total_even = 0
    for i in numbers:
        if i % 2 == 0:
            total_even += i
    return total_even

values = sum_even_numbers([1,3,5,-4])
print(values)