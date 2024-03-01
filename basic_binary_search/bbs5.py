def binary_seek(array,element):
    start = 0
    end = array[-1]
    middle = (start + end) // 2
    print(f'Initialization: {start}, {middle}, {end}')
    while (array[middle] != element) and (start <= end):
        print(start, middle, end)
        if element < array[middle]:
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
    if array[middle] == element:
        print(start, middle, end)
        return print(f'Found:{middle}')
    else:
        print(start, middle, end)
        return print(f'Not Found')

print(binary_seek([ 1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19 ],18))
