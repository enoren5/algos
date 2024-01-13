def binary_seek(arr,elem):
    start = 0
    end = arr[-1]
    middle = (start + end) // 2
    while (arr[middle] != elem) and (start <= end):
        print(start, middle, end)
        if elem < arr[middle]:
            end = middle -1
        else:
            start = middle + 1
            middle = (start + end) // 2
    if arr[middle] == elem:
        return middle
    return False

# [ 1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19 ]
