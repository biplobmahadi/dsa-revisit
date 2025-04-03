# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def createSet(self, value):
        self.parent[value] = value
        self.rank[value] = 0

    def find(self, value):
        if value not in self.parent:
            return None
        p = self.parent[value]
        while p != self.parent[p]:
            p = self.parent[self.parent[p]]
        return p

    def union(self, valueOne, valueTwo):
        p1, p2 = self.find(valueOne), self.find(valueTwo)
        if p1 == p2 or p1 is None or p2 is None:
            return
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 > r2:
            self.parent[p2] = p1
        elif r2>r1:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
