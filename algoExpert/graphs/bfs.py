# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q = deque()
        q.append(self)
        while q:
            p = q.popleft()
            array.append(p.name)
            for n in p.children:
                q.append(n)
        return array
