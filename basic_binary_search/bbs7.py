def binary_seek(ordered_list, value):
    # This function accepts a sorted array and a value
    # Create a left pointer at the start of the array, and a right pointer at the end of the array
    left_pointer = 0
    right_pointer = len(ordered_list) - 1
    # center_pointer = (left_pointer + right_pointer) // 2
    # While the left pointer comes before the right pointer:
    while left_pointer < right_pointer:
        # Create a pointer in the middle:
        center_pointer = len(ordered_list) // 2
        # If you find the value you want, return the index pointer:
        if ordered_list[center_pointer] == value:
            return f"Found at: {center_pointer}"
        #If the value is smaller than the center point, move the right pointer down to the center and run the function again:
        elif center_pointer < (ordered_list[left_pointer] < ordered_list[center_pointer]):
            new_list = ordered_list[left_pointer:center_pointer]
            return binary_seek(new_list, center_pointer)
        # If the value is too large, move the left pointer up and run the function again:
        elif center_pointer < (ordered_list[center_pointer] < ordered_list[right_pointer]):
            new_list = ordered_list[center_pointer:right_pointer]
            return binary_seek(new_list, center_pointer)
    return "Not present"

print(binary_seek([1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19,22],12))