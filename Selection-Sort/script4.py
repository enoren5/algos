arr = [5,3,4,1,2]

print(f"Original list: {arr}")


def sorting_by_selection(arr):
    for i in range(len(arr)-1):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i] = arr[smallest]
    return arr

sorted_list = sorting_by_selection(arr)

print(f"Final sorted list: {sorted_list}")