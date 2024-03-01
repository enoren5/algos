class Node:
    # Create a new node with the value passed to the function
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_right(self, value):
        # If the head property is null set the head and tail to be the newly created node
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        # If not... 
        else:
            # Set the next property on the tail to be that node
            self.tail.next = newNode
            # Set the previous property on the newly created node to be the tail
            newNode.prev = self.tail
            # Set the tail to be the newly created node
            self.tail = newNode
        # Increment the length
        self.length = self.length + 1
        # Return the Doubly Linked List
        return self
    
    def __str__(self):
        if self.length == 0:
            return "Doubly Linked List: []"

        current = self.head
        elements = []
        while current:
            elements += [str(current.value)]
            current = current.next

        return "Doubly Linked List: [" + " <-> ".join(elements) + "]"
    
# Instantiation and testing
DLL_obj = DoublyLinkedList()
print(DLL_obj)
DLL_obj.add_right(7)
DLL_obj.add_right(12)
DLL_obj.add_right(22)
print(DLL_obj)
DLL_obj.add_right(11)
print(DLL_obj)
