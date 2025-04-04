from heapq import heappush, heappop

def dijkstrasAlgorithm(start, edges):
    res = [-1] * len(edges)
    heap = []
    heappush(heap, (0, start))
    visit = set()
    while heap:
        w, s = heappop(heap)
        if s in visit:
            continue
        res[s] = w
        visit.add(s)
        for d, w1 in edges[s]:
            if d not in visit:
                heappush(heap, (w+w1, d))
    return res
