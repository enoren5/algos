class LinearSearch:
    # This class accepts a list as input
    def __init__(self, entered_list=None): 
        self.entered_list = entered_list
                
    def seek(self, item):
        # Loop through the list and check if the current element is equal to the item
        for index, value in enumerate(self.entered_list):
            if value == item:
            # If value found, return the index 
                return index
        return False
        # raise ValueError(f"{item} not in {self.entered_list}")
        # else: print(f"{item} not in {self.entered_list}")
        # If the item is never found, return False
        # return False

    def __str__(self):
        result = self.seek(self.index)
        if result:
            return str(result) 
        else:
            return "Not Present"
