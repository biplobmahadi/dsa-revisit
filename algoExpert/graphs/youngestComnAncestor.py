# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d1, d2 = getLevelCount(descendantOne), getLevelCount(descendantTwo)
    minL = min(d1, d2)
    lu1, lu2 = d1-minL, d2-minL
    one = updateNode(descendantOne, lu1)
    two = updateNode(descendantTwo, lu2)
    while one != two:
        one = one.ancestor
        two = two.ancestor
    return one
    
def updateNode(node, n):
    while n:
        n-=1
        node = node.ancestor
    return node

def getLevelCount(node):
    count = 0
    while node != None:
        node = node.ancestor
        count+=1
    return count