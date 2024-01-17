# https://discuss.python.org/t/naive-sub-string-search-algorithm/43107/8
# Courtesy of "Antoine Weisrock" @WeisLeDocto on the forums. Excellent!

def string_seek(string, pattern):
    pattern_length = len(pattern)
    count = 0
    for index in range(len(string) - pattern_length + 1):
        sub_string = string[index: index+pattern_length]
        count += int(sub_string == pattern)
    return count

print(string_seek("wowomgzomgomg","omg"))