class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return self
        temp = self.root
        while True:
            if value == temp.value:
                return None
            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return self
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = Node(value)
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