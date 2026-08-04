def quick_sort(data: list):
    if len(data) <= 1:
        return data
    pivot = data[len(data)//2]
    left_side = [x for x in data if pivot > x]
    middle = [x for x in data if pivot == x]
    right_side = [x for x in data if pivot < x]

    return quick_sort(left_side) + middle + quick_sort(right_side)


if __name__ == "__main__":
    test_list = quick_sort([8,3,15,11])
    print(test_list)