import math

edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4],
         [2, 4, 2], [2, 3, 8], [3, 4, 5], [3, 6, 1], [4, 5, 20], [5, 6, -100]]
n = 7
s = 0

def bellmanFord(edges, n, src):
    adjList = [[] * _ for _ in range(n)]
    for s, d, w in edges:
        adjList[s].append((w, d))
    distances = [math.inf] * n
    distances[src] = 0
    for _ in range(n-1):
        count = 0
        for i in range(len(adjList)):
            nodes = adjList[i]
            for w, d in nodes:
                total = w + distances[i]
                if total < distances[d]:
                    distances[d] = total
                    count+=1
        if count == 0: break

    return distances

print(bellmanFord(edges, n, s)) # O(V.E), O(V)