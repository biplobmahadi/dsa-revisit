edges = [[1, 2], [4, 1], [2, 4]]

class UnionFind():
    def __init__(self, n) -> None:
        self.parent = {}
        self.rank = {}

        for i in range(1, n):
            self.parent[i] = i
            self.rank[i] = 0

    def findParent(self, node):
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        if p1 == p2: 
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1]+=1
        return True

un = UnionFind(5)

for s, d in edges:
    print(un.union(s, d))
    