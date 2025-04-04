from heapq import heappush, heappop

def primsAlgorithm(edges):
    res = [[] for _ in range(len(edges))]
    heap = []
    visit = set()
    for d, w in edges[0]:
        heappush(heap, (w, d, 0))
    while heap:
        w, d, s = heappop(heap)
        if d in visit:
            continue
        res[s].append([d, w])
        res[d].append([s, w])
        visit.add(d)
        visit.add(s)
        for d1, w1 in edges[d]:
            if d1 not in visit:
                heappush(heap, (w1, d1, d))
    return res
    
