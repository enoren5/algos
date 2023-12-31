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

    def append(self):
        # If the head property is null set the head and tail to be the newly created node
        if head == None:
            self.head = self.tail
        # If not... 
        else:
            # Set the next property on the tail to be that node
            Node.next = self.tail
            # Set the previous property on the newly created node to be the tail
            Node.prev = Node.value
            # Set the tail to be the newly created node
            self.tail = Node.value
            # Increment the length
            self.length = self.length + 1
            # Return the Doubly Linked List
            return self

# Instantiation and testing
DLL_obj = Node(12)
print(DLL_obj)
DLL_obj.next = 13
print(DLL_obj.next)
DLL_obj.prev = 11
print(DLL_obj.prev)