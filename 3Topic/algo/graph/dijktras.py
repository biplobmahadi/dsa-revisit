from heapq import heappop, heappush

def dijktras(adj, src):
    res = {}
    minHeap = [(0, src)]
    while minHeap:
        w, s = heappop(minHeap)
        if s in res:
            continue
        res[s] = w
        for nei, wei in adj[s]:
            if nei not in res:
                heappush(minHeap, (w+wei, nei))

    return res


adj = {
    "A": [('B', 10), ('C', 3)],
    "B": [('D', 2)],
    "C": [('B', 4), ('E', 2), ('D', 8)],
    "D": [('E', 5)],
    "E": [],
}

print(dijktras(adj, 'A'))