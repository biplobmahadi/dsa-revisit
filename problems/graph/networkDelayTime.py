from heapq import heappush, heappop
import math

def networkDelayTime(times, n, k):
    distances = [math.inf] * n
    adjList = [[] for _ in range(n)]
    for group in times:
        adjList[group[0]-1].append([group[1]-1, group[2]])
    queue = []
    distances[k-1] = 0
    heappush(queue, [distances[k-1], k-1])
    while queue:
        popped = heappop(queue)
        poppedNode = popped[1]
        poppedWeight = popped[0]
        for i in adjList[poppedNode]:
            total = poppedWeight + i[1]
            if total < distances[i[0]]:
                distances[i[0]] = total
                heappush(queue, [total, i[0]])
    if math.inf in distances:
        return -1
    return max(distances)

times = [[1,2,1]]
n = 2
k = 2
print(networkDelayTime(times, n, k))

def networkTimeDelayBellman(times, n, k):
    distances = [math.inf] * n
    distances[k-1] = 0
    for _ in range(n-1):
        count = 0
        for group in times:
            total = distances[group[0]-1] + group[2]
            if total < distances[group[1]-1]:
                distances[group[1]-1] = total
                count+=1
        if count == 0: break
    if math.inf in distances:
        return -1
    return max(distances)

print(networkDelayTime(times, n, k))
