def string_seek(long, short):
    i = 0
    j = 0
    count = 0
    while i < len(long):
        i += 1
        while j < len(short):
            if short[j] != long[i+j]:
                break
            if j == len(short)-1:
                count += 1
                continue
        return count