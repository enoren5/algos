arr = [5,3,4,1,2]

print(f"Original list: {arr}")


def sorting_by_selection(arr):
    for write_index in range(0,len(arr)):
        for search_index in range(write_index): #,0):
            element1 = arr[search_index]
            element2 = arr[search_index+1]
            if element1 < element2:
                arr[write_index] = element1
                element1, element2 =  element2, element1
            else: 
                continue
    return arr

sorted_list = sorting_by_selection(arr)

print(f"Final sorted list: {sorted_list}")