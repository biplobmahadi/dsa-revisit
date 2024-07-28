from heapq import heappop, heappush

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Initialize nodes if they are not already in the structure
        if node1 not in self.parent:
            self.parent[node1] = node1
            self.rank[node1] = 0
        if node2 not in self.parent:
            self.parent[node2] = node2
            self.rank[node2] = 0

        # Find roots of the nodes
        root1 = self.find(node1)
        root2 = self.find(node2)

        # If they are already in the same set
        if root1 == root2:
            return False

        # Union by rank
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True


adj = {
    "A": [('B', 10), ('C', 3)],
    "B": [('D', 1), ('A', 10), ('C', 4)],
    "C": [('A', 3), ('B', 4), ('E', 4), ('D', 4)],
    "D": [('E', 2), ('B', 1), ('C', 4)],
    "E": [('D', 2), ('C', 4)],
}

def kruskals(adj, n):
    mst = []
    minHeap = []
    unionfind = UnionFind()
    for key, value in adj.items():
        for des, wei in value:
            heappush(minHeap, (wei, key, des))
    
    while len(mst) < n-1:
        w, s, d = heappop(minHeap)
        if not unionfind.union(s, d):
            continue
        mst.append([s, d])
    return mst

print(kruskals(adj, 5))