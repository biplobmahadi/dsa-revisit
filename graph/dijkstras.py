from heapq import heappop, heappush

edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4],
         [2, 4, 2], [2, 3, 8], [3, 4, 5]]
n = 5
s = 0

def dijkstrasI(edges, n, src):
    adjList = [[] * _ for _ in range(n)]
    for s, d, w in edges:
        adjList[s].append((w, d))
    shortest = {}
    minHeap = [(0, src)]

    while minHeap:
        w1, sr = heappop(minHeap)
        if sr in shortest:
            continue
        shortest[sr] = w1

        for w2, d in adjList[sr]:
            if d not in shortest:
                heappush(minHeap, (w1+w2, d))
    return shortest

print(dijkstrasI(edges, n, s)) # O(ElogV), O(V+E) 