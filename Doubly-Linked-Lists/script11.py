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


    def add_left(self, value):
        # If the head property is null set the head and tail to be the newly created node
        newNode = Node(value) # If the length is 0
        if self.length == 0:
            self.head = newNode # Set the head to be the new node
            self.tail = newNode # Set the tail to be the new node
        else: # Oherwise... 
            # Set the prev property on the head of the list to be the new node
            self.head.prev = newNode
            # Set the next property on the new node to be the head property
            newNode.next = self.head
            # Update the head to be the new node
            self.head = newNode
        self.length = self.length + 1 # Increment the length
        return self


    def pop_left(self):
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

    def cust_get(self, item_location):
        
        if item_location < 0 or item_location >= self.length:
            return None
        
        if item_location <= (self.length // 2):
            print("Traversing from start")
            count = 0
            current = self.head
            while count != item_location:
                current = current.next
                count = count + 1
            return current
        
        elif item_location >= (self.length // 2):
            print("Traversing backwards from end")
            count = self.length -1
            current = self.tail
            while count != item_location:
                current = current.prev
                count = count - 1            
            return current


    def cust_set(self, item_location, new_value):
        found_node = self.cust_get(item_location)
        
        if found_node != None:
            found_node.value = new_value
            return True
        return False
        

    def cust_insert(self, item_location, new_value):
        if item_location < 0 or item_location > self.length:
           return None
        elif item_location == 0:
            return self.add_left(new_value)
        elif item_location == self.length:
           self.add_right(new_value)
           self.length += 1 
           # print(self.length)
           return self
        new_node = Node(new_value)
        before_node = self.cust_get(item_location-1)
        after_node = before_node.next
        before_node.next = new_node
        new_node.prev = before_node
        new_node.next = after_node
        after_node.prev = new_node
        self.length = self.length + 1
        return True
    

    def cust_remove(self, item_location):
        if item_location < 0: # or item_location > self.length:
           return None
        elif item_location == 0:
            return self.pop_left()
        elif item_location == (self.length-1):
           return self.pop_right()
        removed_node = self.cust_get(item_location)
        removed_node.prev.next = removed_node.next
        removed_node.next.prev = removed_node.prev
        removed_node.next = None
        removed_node.prev = None
        self.length = self.length - 1
        return removed_node
    

    def shift_linked_list(self, variance):
        if variance > 0:
            for iteration in range(0,variance):
                self.head = self.tail 
                # self.length = self.length + 1
            return self
        elif variance < 0:
            for iteration in range(0,variance):
                self.tail = self.head
                # self.length = self.length + 1
            return self
        elif variance == 0:
            pass
    
    
    def __str__(self):
        if self.length == 0:
            return "Empty DLL for intialization"

        current = self.head
        elements = []
        while current:
            elements += [str(current.value)]
            current = current.next

        return "Doubly Linked List: [" + " <-> ".join(elements) + "]"
      

# Instantiation and testing
    
DLL_obj = DoublyLinkedList()
DLL_obj.add_right(7)
DLL_obj.add_right(12)
DLL_obj.add_right(22)
DLL_obj.cust_insert(0,999)
DLL_obj.cust_insert(4,90099)
DLL_obj.cust_insert(2,"'Custom insert test'")
print(DLL_obj)
DLL_obj.shift_linked_list(5)
print(DLL_obj)

'''
def shift_linked_list(DLL_obj,k):
    # if k > 0:
    for iteration in range(0,k):
        DLL_obj.cust_insert(0, DLL_obj.tail)
        DLL_obj.cust_remove(len(DLL_obj)-1)
    return DLL_obj
'''


'''
def shift_linked_list(DLL_obj,k):
    if k > 0:
        for iteration in range(0,k):
            DLL_obj.cust_insert(0, DLL_obj.pop_right())
            DLL_obj.cust_remove(len(DLL_obj)-1)
        return DLL_obj

shift_linked_list(DLL_obj,2)

print(DLL_obj)
'''

'''
def shift_linked_list(DLL_obj,k):
    if k > 0:
        for iteration in range(0,k):
            DLL_obj.add_left(DLL_obj[-1])
            DLL_obj.pop_right(DLL_obj[0])
        return DLL_obj
'''