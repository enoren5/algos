arr = [5,3,4,1,2]

print(f"Original list: {arr}")


def sorting_by_selection(arr):
    for iteration in range(0,len(arr)):
        for i in range(iteration):
            element1 = arr[i]
            element2 = arr[i+1]
            if element1 < element2:
                minimum = element1
                arr[minimum], arr[i] = arr[minimum], arr[i]
            else: 
                continue
    return arr

sorted_list = sorting_by_selection(arr)

print(f"Final sorted list: {sorted_list}")