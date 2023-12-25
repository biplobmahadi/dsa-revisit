# write with dfs postorder and reverse 

edges = [['a', 'b'], ['g', 'h'], ['a', 'c'], ['b', 'd'], ['c', 'e'], ['d', 'f'], ['e', 'f']]

def topoSort(edges):
    adj = {}
    for s, d in edges:
        if s in adj:
            adj[s].append(d)
        else:
            adj[s] = [d]
        if d not in adj:
            adj[d] = []
    ans = []
    seen = {}
    for key in adj.keys():
        dfs(adj, ans, seen, key)
    ans.reverse()
    return ans

def dfs(adj, ans, seen, start):
    if start in seen:
        return
    seen[start] = True
    for val in adj[start]:
        dfs(adj, ans, seen, val)
    ans.append(start)

print(topoSort(edges))