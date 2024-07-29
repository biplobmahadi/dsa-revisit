# it is actually topological order

adj = [[3], [], [3], [], [0, 1], [0]]

def topologicalSortIndegree(adj, num):
    indegree = [0] * num
    for n in adj:
        for node in n:
            indegree[node] += 1
    stack = []
    for i, n in enumerate(indegree):
        if n == 0:
            stack.append(i)
    count = 0
    res = []
    while stack:
        p = stack.pop()
        res.append(p)
        count+=1
        for nei in adj[p]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                stack.append(nei)
    return res if count == num else -1


print(topologicalSortIndegree(adj, 6))


# without cycle (use path hashmap for cycle detection)
def topologicalSortDfs(adj, num):
    visited = set()
    res = []

    for i in range(num):
        dfs(i, adj, visited, res)
    res.reverse()
    return res

def dfs(node, adj, visited, res):
    if node in visited:
        return
    visited.add(node)

    for n in adj[node]:
        dfs(n, adj, visited, res)
    res.append(node)


print(topologicalSortDfs(adj, 6))
