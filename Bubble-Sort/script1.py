arr = [5,3,4,1,2]

print(f"Original list: {arr}")

def bubble(arr): 
    for idx1,idx2 in arr:
        if idx1 > idx2:
            temp = arr[idx1]
            arr[idx1] = arr[idx2]
            arr[idx2] = temp
        else:
            continue
    return arr

sorted_list = bubble(arr)

print(f"Final sorted list: {sorted_list}")


'''
            temp = arr[0]
        if arr[idx1] == arr[idx2]
            arr[idx2] = temp
'''