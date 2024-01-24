def binary_seek(array,target):
    start = 0
    end = len(array)-1
    middle = (start + end) // 2
    print(f'Initialization: {start}, {middle}, {end}')
    while (array[middle] != target) and (start <= end):
        print(start, middle, end)
        if target < array[middle]:
            print(start, middle, end)
            end = middle -1
            middle = (start + end) // 2
            print(start, middle, end)
        else:
            print(start, middle, end)
            start = middle + 1
            # end = array[-1]
            middle = (start + end) // 2            
            print(start, middle, end)
    if array[middle] == target:
        print(start, middle, end)
        return print(f'Found:{middle}')
    else:
        print(start, middle, end)
        return print(f'Not Found')

print(binary_seek([ 1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19 ],6))
