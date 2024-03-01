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
    
    
    def pop_right(self):
        # If there is no head, return undefined
        if self.head == None:
            return "Undefined"
        else:
            # Store the current tail in a variable to return later
            temp = self.tail
            # If the length is 1, set the head and tail to be null
            if self.length == 1:
                self.head == None
                self.tail == None
            # Update the tail to be the previous Node
            self.tail = self.tail.prev 
            # Set the newTail's next to null
            self.tail.next = None
        # Decrement the length    
        self.length = self.length - 1
        # Return the value removed
        return temp


    def remove_left(self):
        # If length is 0, return undefined
        if self.length == 0:
            return "Undefined"
        else:
            # Store the current head property in a variable (we'll call it old head)
            old_head = self.head
            # If the length is one 
            if self.length == 1:
                # Set the head to be null 
                self.head == None
                # set the tail to be null
                self.tail == None
            # Update the head to be the next of the old head
            self.head = old_head.next
            # Set the head's prev property to null
            self.head.prev = None
            # Set the old head's next to null
            old_head.next = None
        # Decrement the length
        self.length = self.length - 1
        # Return old head
        return old_head


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
DLL_obj.pop_right()
DLL_obj.pop_right()
print(DLL_obj)
DLL_obj.remove_left()
print(DLL_obj)