def string_seek(long, short):
    i = 0
    j = 0
    count = 0
    for index, i in enumerate(long):
        index += 1
        for j in short:
            if short[j] != long[i+j]:
                break
            if j == len(short)-1:
                count += 1                
    return count