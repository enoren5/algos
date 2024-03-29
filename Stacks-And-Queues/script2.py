class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = None

        
class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    
    def place_on_top(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
            self.size += 1
        else: 
            temp = self.first
            self.first = new_node
            self.first.next = temp 
            self.size += 1
        return self.size
    
    
    def remove_from_bottom(self):
        if self.size == 0: return None
        temp = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        if self.size > 1:
            self.first = self.first.next
            self.size = self.size - 1
        return temp.value
    
    
    def add_to_queue(self, value): # Enqueue
        new_node = Node(value)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
            self.size += 1
        else: 
            # temp = self.first
            self.last.next = new_node 
            self.last = new_node
            self.size += 1
        return self.size
    
    def remove_from_queue(self): # "Dequeue"
        if self.size == 0: return None
        temp = self.first
        if self.size == 1:
            self.first = None
            self.last = None
            return self.last
        self.first = self.first.next
        self.size = self.size - 1
        return temp.value

    def __str__(self):
        if self.size == 0:
            return "Empty structure for intialization"
        current = self.first
        elements = []
        while current:
            elements += [str(current.value)]
            current = current.next

        return "Stack: [" + " <- ".join(elements) + "]"
    

print("Stacks: First in Last Out: FILO : ")
SAQ = Stack()
print(SAQ)
SAQ.place_on_top(7)
SAQ.place_on_top(12)
SAQ.place_on_top(12)
print(f'Length of stack so far: {SAQ.place_on_top(12)}')
print(SAQ)
SAQ.place_on_top(22)
print(SAQ)
print(f'First item removed from bottom: {SAQ.remove_from_bottom()}')
SAQ.remove_from_bottom()
print(SAQ)

SAQ = Stack()
print(' = = End of stack experimentation. = = ')
print(' = = Begin queue experimentation :  = = ')
print("Queues: First in First Out FIFO ")
print(SAQ)
SAQ.add_to_queue(' queue item 1 ')
SAQ.add_to_queue(' queue item 2 ')
SAQ.add_to_queue(' queue item 3 ')
print(SAQ)
print(SAQ.remove_from_queue())
print(SAQ.remove_from_queue())
print(SAQ)