# Also courtesy of forum member: demola
# https://discuss.python.org/t/writing-a-linear-search-algorithm-malformed-string-representation/42716/26

class LinearSearch:
    def __init__(self, entered_list=[]):
        self.entered_list = entered_list
        
    def seek(self, item):
      return item in self.entered_list