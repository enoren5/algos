def binary_seek(ordered_list, value):
    left = 0
    right = len(ordered_list) - 1
    center = len(ordered_list) // 2
    if value == ordered_list[center]:
        return f"Found at: {center}"
    elif value < ordered_list[center]:
        right = center
        new_list = ordered_list[left:center]
        # center = len(new_list) // 2
        return binary_seek(new_list, value)
    elif value > ordered_list[center]:
        left = center
        new_list = ordered_list[center:right]
        # center = len(new_list) // 2
        return binary_seek(new_list, value)
    else:
        return "Not present"

print(binary_seek([101, 444, 567, 812, 999, 1101, 1232, 1522, 1684, 222234],9990000))