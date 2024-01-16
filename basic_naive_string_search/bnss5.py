


def string_seek(long_string, sub_string):
    sub_length = len(sub_string)
    count = 0
    for item in range(len(long_string) - sub_length + 1):
        s = long_string[item: item+sub_length]
        count += int(s == sub_string)
    return count

print(string_seek("wowomgzomgomg","omg"))