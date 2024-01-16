def count_substring(main_string,sub_string):
    main_len = len(main_string)
    sub_len = len(sub_string)
    iteration = 0
    counter = 0
    while iteration < main_len:
        if main_string[iteration] == sub_string[0]:
            if main_string[iteration:iteration+sub_len] == sub_string:
                counter += 1
        iteration += 1

    return counter

print(count_substring("CABCDCDCCDC","CDC"))