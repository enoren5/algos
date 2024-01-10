def seek(entered_list, item):
    for index, value in enumerate(entered_list):
        if value == item:        
            return index        
    raise ValueError(f"{item} not in {entered_list}")