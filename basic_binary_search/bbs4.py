def binary_seek(ordered_list, value):
    left_pointer = ordered_list[0]
    right_pointer = ordered_list[-1]
    while left_pointer < right_pointer:        
        center_pointer = len(ordered_list)//2
        if center_pointer == value:
            return f"Found at: {center_pointer}"
        elif center_pointer < (ordered_list[left_pointer] < ordered_list[center_pointer]):
            new_list = ordered_list[left_pointer:center_pointer]
            return binary_seek(new_list, value)
        elif center_pointer < (ordered_list[center_pointer] < ordered_list[right_pointer]):
            new_list = ordered_list[center_pointer:right_pointer]
            return binary_seek(new_list, value)
        return "Not present"

# [ 1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19 ]

# This function accepts a sorted array and a value
# Create a left pointer at the start of the array, and a right pointer at the end of the array
# While the left pointer comes before the right pointer:
# Create a pointer in the middle:
# If you find the value you want, return the index pointer:
# If the value is too small, move the left pointer down and run the function again:
# If the value is too large, move the right pointer up and run the function again:
# Else" return not present