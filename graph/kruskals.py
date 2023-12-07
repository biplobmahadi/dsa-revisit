# find minimum spanning tree

from heapq import heappop, heappush

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        else:
            return False

edges = [[0,1,10], [0,2,3], [1,2,4], [1,3,1], [2,3,4], [2,4,4], [3,4,2]]
n = 5

def kruskalsAlgo(edges, n):
    minHeap = []
    for s, d, w in edges:
        heappush(minHeap, (w, s, d))

    unionFind = UnionFind(n)
    mst = []
    val = 0

    while len(mst) != n-1:
        wt, n1, n2 = heappop(minHeap)
        if not unionFind.union(n1, n2):
            continue
        mst.append([n1, n2])
        val+=wt
    print(val)
    return mst

print(kruskalsAlgo(edges, n))

