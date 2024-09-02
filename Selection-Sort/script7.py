arr = [5,3,4,1,2]

print(f"Original list: {arr}")


def sorting_by_selection(arr):
    print(f"Initial array: {arr=}")
    for i in range(len(arr)-1):
        print(f"    Outer loop iteration: {i=}")
        smallest = arr[i]
        print(f"    Invariant: {smallest=}")        
        for j in range(len(arr)):
            #print(f"        Inner loop iteration: {j=}, {smallest=}, {arr=}")
            if arr[j] < smallest:
                print(f'        Swapping entries: {arr[j]=}, {smallest=}')
                arr[smallest], arr[j] = arr[j], arr[smallest]
                print(f'        New: {arr=}')
        arr[i] = arr[smallest]
    return arr

sorted_list = sorting_by_selection(arr)

print(f"Final sorted list: {sorted_list}")