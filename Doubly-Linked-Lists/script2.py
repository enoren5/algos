class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        return self
    
    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return str(result)

# Instantiation and testing
DLL_obj = DoublyLinkedList()
print(DLL_obj)
DLL_obj.append(7)
DLL_obj.append(12)
DLL_obj.append(22)
print(DLL_obj)
DLL_obj.append(11)
print(DLL_obj)
print(DLL_obj)