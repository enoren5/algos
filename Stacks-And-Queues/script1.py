class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

