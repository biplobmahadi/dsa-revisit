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

def dfsAdjacencyList(graph, list, seen, curr):
    if seen.get(curr): return
    list.append(curr)
    seen[curr] = True
    for i in graph[curr]:
        dfsAdjacencyList(graph, list, seen, i)
    return list

# def dfsAdjacencyMatrix(graph, list, seen, curr):
#     if seen.get(curr): return
#     list.append(curr)
#     seen[curr] = True
#     for i in range(len(graph[curr])):
#         if graph[curr][i] == 1:
#             dfsAdjacencyMatrix(graph, list, seen, i)
#     return list

# print(dfsAdjacencyList(graph, [], {}, 0))
# print(dfsAdjacencyMatrix(graphInMatrix, [], {}, 0))
