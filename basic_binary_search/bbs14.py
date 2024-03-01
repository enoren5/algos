def binary_seek(original_list, working_list, value):
    print('binary_seek(%r, %r)' % (working_list, value))
    center = len(working_list) // 2
    if value == original_list[center]:
        return f"Found at: {center}"
    elif value < working_list[center]:
        new_list = working_list[:center]
        return binary_seek(original_list, new_list, value)
    else:
        new_list = working_list[center:]
        return binary_seek(original_list, new_list, value)

original_list = [101, 444, 567, 812, 999, 1101, 1232, 1522, 1684, 222234]
working_list = [101, 444, 567, 812, 999, 1101, 1232, 1522, 1684, 222234]

for value in original_list:
    print('Seeking %d: %r' % (value, binary_seek(original_list, working_list, value)))
    