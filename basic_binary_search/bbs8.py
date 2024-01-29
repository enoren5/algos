def binary_seek(ordered_list, value):
    left_pointer = 0
    right_pointer = len(ordered_list) - 1
    while left_pointer < right_pointer:
        center_pointer = len(ordered_list) // 2
        if ordered_list[center_pointer] == value:
            return f"Found at: {center_pointer}"
        elif ordered_list[left_pointer] < value < ordered_list[center_pointer]:
            right_pointer = ordered_list[center_pointer]
            new_list = ordered_list[left_pointer:center_pointer]
            center_pointer = len(new_list) // 2
            return binary_seek(new_list, value)
        elif ordered_list[right_pointer] < value < ordered_list[center_pointer]:
            left_pointer = ordered_list[center_pointer]
            new_list = ordered_list[center_pointer:right_pointer]
            center_pointer = len(new_list) // 2
            return binary_seek(new_list, value)
    return "Not present"

print(binary_seek([1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19,22],119))