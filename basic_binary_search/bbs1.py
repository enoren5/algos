# [ 1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19 ]

def binary_seek(ordered_list, value):
    # This function accepts a sorted array and a value
    # Create a left pointer at the start of the array, and a right pointer at the end of the array
    left_pointer = ordered_list[0]
    right_pointer = ordered_list[-1]
    # While the left pointer comes before the right pointer:
    while left_pointer < right_pointer:
        # Create a pointer in the middle:
        center_pointer = int(len(ordered_list/2))
        # If you find the value you want, return the index pointer:
        if center_pointer == value:
            return "found"
        elif ordered_list[left_pointer] < ordered_list[center_pointer]:
            next_center = int(len(ordered_list[left_pointer:center_pointer]/2))
            if next_center == value:
                return "found"
        elif ordered_list[center_pointer] < ordered_list[right_pointer]:
            next_center = int(len(ordered_list[center_pointer:right_pointer]/2))
            if next_center == value:
                return "found"
        # If you never find the value, return 'not present':
        else:
            return "not present"

'''

If the value is too small, move the left pointer up
If the value is too large, move the right pointer down
'''

