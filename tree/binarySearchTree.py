from pprint import pprint
from collections import deque

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
    
    def _display_helper(self, node):
        if node is None:
            return None
        return {
            'balue': node.val,
            'left': self._display_helper(node.left),
            'right': self._display_helper(node.right)
        }

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
    
    def remove(self, val):
        parent = None
        current = self.root
        while current:
            if current.val == val:
                if not current.left and not current.right:
                    if parent.left == current:
                        parent.left = None
                    else: 
                        parent.right = None
                    current = None
                elif current.left is None and current.right:
                    if parent.left == current:
                        parent.left = current.right
                    else: 
                        parent.right = current.right
                    current = None
                elif current.left and current.right is None:
                    if parent.left == current:
                        parent.left = current.left
                    else: 
                        parent.right = current.left
                    current = None
                else:
                    newTree = current.right
                    if newTree.left:
                        newParent = newTree
                        newCurrent = newTree.left
                        while newCurrent.left:
                            newParent = newCurrent
                            newCurrent = newCurrent.left
                        if newCurrent.right:
                            newParent.left = newCurrent.right
                        else:
                            newParent.left = None
                        if parent.left == current:
                            parent.left = newCurrent
                        else:
                            parent.right = newCurrent
                        newCurrent.right = newTree
                        if current.left:
                            newCurrent.left = current.left
                    else:
                        newCurrent = current.right
                        if parent.left == current:
                            parent.left = newCurrent
                        else: 
                            parent.right = newCurrent
                        if current.left:
                            newCurrent.left = current.left
                    current = None
            else:
                parent = current
                if val > current.val:
                    current = current.right
                else:
                    current = current.left
        
    def bfsIterative(self):
        queue = deque()
        list = []
        queue.append(self.root)
        
        while len(queue):
            popped = queue.popleft()
            list.append(popped.val)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        return list
    
    def bfsRecursive(self, queue: deque, list: list):
        if len(queue) == 0:
            return list
        popped = queue.popleft()
        list.append(popped.val)
        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
        return self.bfsRecursive(queue=queue, list=list)

    def dfsPreRecursive(self, node:Node, list: list):
        list.append(node.val)
        if node.left:
            self.dfsPreRecursive(node=node.left, list=list)
        if node.right:
            self.dfsPreRecursive(node=node.right, list=list)
        return list
    
    def dfsInRecursive(self, node:Node, list: list):
        if node.left:
            self.dfsInRecursive(node=node.left, list=list)
        list.append(node.val)
        if node.right:
            self.dfsInRecursive(node=node.right, list=list)
        return list
        
    def dfsPostRecursive(self, node:Node, list: list):
        if node.left:
            self.dfsPostRecursive(node=node.left, list=list)
        if node.right:
            self.dfsPostRecursive(node=node.right, list=list)
        list.append(node.val)
        return list
    
def display(node):
    tree_dict = bst._display_helper(node)
    pprint(tree_dict)

bst = BST()

bst.insert(9)
bst.insert(4)
bst.insert(1)
bst.insert(6)
bst.insert(26)
bst.insert(170)
bst.insert(15)
bst.insert(7)
# bst.insert(180)
# bst.insert(160)
# bst.insert(150)
# bst.insert(145)
# bst.insert(146)
# bst.insert(147)

# display(bst.lookup(20))

# bst.remove(26)

# display(bst.root)

# print(bst.bfsIterative())
# q = deque()
# q.append(bst.root)
# print(bst.bfsRecursive(queue=q, list=[]))
# print(bst.dfsInRecursive(node=bst.root, list=[]))
print(bst.dfsPostRecursive(node=bst.root, list=[]))