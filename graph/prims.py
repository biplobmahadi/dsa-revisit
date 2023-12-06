# minimum spanning tree

from heapq import heappop, heappush

edges = [[0,1,10], [0,2,3], [1,2,4], [1,3,1], [2,3,4], [2,4,4], [3,4,2]]
n = 5
src = 1

def primsAlgo(edges, n, src):
    adjList = [[] * _ for _ in range(n)]
    for s, d, w in edges:
        adjList[s].append((w, d))
        adjList[d].append((w, s))
    
    prioQue = []
    srcConnections = adjList[src]
    for w, d in srcConnections:
        heappush(prioQue, (w, src, d))
    
    visited = set()
    visited.add(src)
    mst = []
    val = 0
    while prioQue:
        w, s, d = heappop(prioQue)
        if d in visited:
            continue
        mst.append([s, d])
        val += w
        visited.add(d)

        for wt, des in adjList[d]:
            if des not in visited:
                heappush(prioQue, (wt, d, des))

    print(val)
    return mst

print(primsAlgo(edges, n, src)) # O(ElogV), O(E)