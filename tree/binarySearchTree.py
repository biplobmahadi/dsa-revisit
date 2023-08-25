from pprint import pprint

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'node: {self.val}, left: {self.left}, right: {self.right}'

class BST:
    def __init__(self) -> None:
        self.root = None
    
    # def _display_helper(self, node):
    #     if node is None:
    #         return None
    #     return {
    #         'balue': node.val,
    #         'left': self._display_helper(node.left),
    #         'right': self._display_helper(node.right)
    #     }

    def insert(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            return self.root
        else:
            current = self.root
            while True:
                if current.val > val:
                    if current.left is None:
                        current.left = node
                        return self.root
                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        return self.root
                    current = current.right
                    
    def lookup(self, val):
        current = self.root
        while current:
            if current.val == val:
                return current
            elif current.val > val:
                current = current.left
            else: 
                current = current.right
        return None
    
# def display(node):
#     tree_dict = bst._display_helper(node)
#     pprint(tree_dict)

bst = BST()

bst.insert(9)
bst.insert(4)
bst.insert(1)
bst.insert(6)
bst.insert(26)
bst.insert(170)
bst.insert(15)

# display(bst.lookup(20))

# display(bst.root)