#this function implements the insertion sort logic
def insertion_sort(data: list)-> list:
    len_data = len(data)
    for i in range(1, len_data): # loop will start from 1
        value = data[i] # stores the second value of list to neable us do the swapping
        start = i-1 #enbles us to get the index of the first calue in the list so we can compare

        #
        while start>=0 and data[start] > value:
            data[start+1] = data[start] # this shifts the value right as long as start >= 0 and data[start] > value
            start -=1 #this condition ensures the loop breaks and we remain withoin the boundry of the list

        data[start+1] = value #This line does the swapping after the while loop breaks
    return data

#test case to see if the function works
if __name__ == "__main__":
    data = [5,4,10,2,1,0]
    sorted_data = insertion_sort(data)
    print(sorted_data)
    