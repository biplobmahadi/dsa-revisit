from heapq import heappop, heappush


adj = {
    "A": [('B', 10), ('C', 3)],
    "B": [('D', 1), ('A', 10), ('C', 4)],
    "C": [('A', 3), ('B', 4), ('E', 4), ('D', 4)],
    "D": [('E', 2), ('B', 1), ('C', 4)],
    "E": [('D', 2), ('C', 4)],
}


def prims(adj, src):
    mst = []
    minHeap = []
    visited = set()
    for des, wei in adj[src]:
        heappush(minHeap, (wei, des, src))
    visited.add(src)
    while minHeap:
        _, d, s = heappop(minHeap)
        if d in visited:
            continue

        mst.append([s, d])
        visited.add(d)

        for des, wei in adj[d]:
            if des not in visited:
                heappush(minHeap, (wei, des, d))
    return mst

print(prims(adj, 'A'))