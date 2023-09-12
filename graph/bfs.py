from collections import deque

def bfsWithAdjacencyList(graph):
    list, queue, seen = [], deque([0]), {}
    while queue:
        popped = queue.popleft()
        if not seen.get(popped):
            list.append(popped)
            seen[popped] = True
        for i in graph[popped]:
            if not seen.get(i):
                queue.append(i)
    return list

graph = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5, 8],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2, 3],
]
print(bfsWithAdjacencyList(graph))

def bfsWithAdjacencyMatrix(graph):
    list, queue, seen = [], deque([0]), {}
    while queue:
        popped = queue.popleft()
        if not seen.get(popped):
            list.append(popped)
            seen[popped] = True
        for i in range(len(graph[popped])):
            if (not seen.get(i) and graph[popped][i]):
                queue.append(i)
    return list

graphInMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0],
]
print(bfsWithAdjacencyMatrix(graphInMatrix))