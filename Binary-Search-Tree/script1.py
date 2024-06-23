class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        # newNode = Node(value)
        # self.root = newNode
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return self
        temp = self.root
        while True:
            if newNode.value == temp.value:
                return None
            if newNode.value < temp.value:
                if temp.left == None:
                    temp.left = newNode
                    return self
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = newNode
                    return self
                temp = temp.right
        
    def __str__(self):
        return self._str_recursive(self.root)

    def _str_recursive(self, node):
        if node is None:
            return ""
        return f"({self._str_recursive(node.left)} {node.value} {self._str_recursive(node.right)})"

mytree = BST()
mytree.insert(47)
mytree.insert(21)
mytree.insert(76)
mytree.insert(18)
mytree.insert(52)
mytree.insert(82)
print(mytree)