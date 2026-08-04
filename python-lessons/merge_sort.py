# This function when called does the merge for each sorted part
def merge(left, right):
    sorted_list = []
    i = 0 # indexes the left list
    j = 0 # Indexes the right list 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # add any extra number not in the already sorted list from left and right
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    # returns a merged list
    return sorted_list
    
    #this function divides the list into two part and call merge
def merge_sort(data: list):
    if len(data) <= 1:
        return data
    mid = len(data)//2
    left_side = merge_sort(data[:mid])
    right_side = merge_sort(data[mid:])

    return merge(left_side, right_side)

if __name__ == "__main__":
    unsorted_list = merge_sort([8,3,15,11])
    print(unsorted_list)