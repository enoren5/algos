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
            # center_pointer = len(new_list) // 2
            return binary_seek(new_list, value)
        elif ordered_list[right_pointer] < value < ordered_list[center_pointer]:
            left_pointer = ordered_list[center_pointer]
            new_list = ordered_list[center_pointer:right_pointer]
            # center_pointer = len(new_list) // 2
            return binary_seek(new_list, value)
    return "Not present"

print(binary_seek([111, 333, 444, 666, 888, 999, 1101, 1232, 1522, 1684, 222234],1101))