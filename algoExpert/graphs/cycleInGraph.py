def cycleInGraph(edges):
    visit, path = set(), set()
    def dfs(node):
        if node in path:
            return True
        if node in visit:
            return
        path.add(node)
        visit.add(node)
        for n in edges[node]:
            if dfs(n):
                return True
        path.remove(node)
    for n in range(len(edges)):
        if dfs(n):
            return True
    return False
