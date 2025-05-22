# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right:
        return getleftmost(node.right)
    return getrightparent(node)

def getleftmost(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr
    
def getrightparent(node):
    curr = node
    while curr.parent and curr.parent.right == curr:
        curr = curr.parent
    return curr.parent
