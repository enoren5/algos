class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
class Stack:
    def __init__(self):
        # new_node = Node(value)
        self.first = None
        self.last = None
        self.size = 0

    def place_on_top(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
            self.size += 1
            # return self
        else: #elif self.size >= 1:
            temp = self.first
            self.first = new_node
            self.first.next = temp 
            self.size += 1
        return self #= self.size + 1  
    
    '''
    def __str__(self):
    
        current = self.first
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
    '''
    def __str__(self):
        #if self.size == 0:
        #    return "Empty Stack for intialization"

        current = self.first
        elements = []
        while current:
            elements += [str(current.value)]
            current = current.next

        return "Stack: [" + " <- ".join(elements) + "]"
    

SAQ = Stack()
print(SAQ)
SAQ.place_on_top(7)
SAQ.place_on_top(12)
print(SAQ)
SAQ.place_on_top(22)
print(SAQ)