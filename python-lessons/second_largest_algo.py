def second_largest(numbers):
    # TODO: return the second largest DISTINCT number in `numbers`
    sorted_list = sorted(numbers)
    len_sorted_list = len(sorted_list)-1
    if len(sorted_list) >= 3:
        if sorted_list[len_sorted_list] == sorted_list[len_sorted_list-1]:
            return sorted_list[len_sorted_list-2]
        else:
            return sorted_list[len_sorted_list-1]
    elif len(sorted_list) == 2:
        return sorted_list[0]
    else:
        return sorted_list
