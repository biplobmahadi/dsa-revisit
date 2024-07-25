adjacencyList = [[2, 3], [5], [0, 5, 4], [0, 4], [2, 3, 5], [1, 2, 4]]

def dfs(el, adList, visited):
    if el in visited:
        return
    print(el)
    visited.add(el)

    for n in adList[el]:
        dfs(n, adList, visited)

dfs(0, adjacencyList, set())