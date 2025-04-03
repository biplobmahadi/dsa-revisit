from collections import defaultdict

def topologicalSort(jobs, deps):
    indegree = {n: 0 for n in jobs}
    adj = defaultdict(list)
    for s, d in deps:
        indegree[d] += 1 
        adj[s].append(d)
    stack = []
    for k, v in indegree.items():
        if v == 0:
            stack.append(k)
    res = []
    while stack:
        p = stack.pop()
        res.append(p)
        for n in adj[p]:
            indegree[n] -= 1
            if indegree[n] == 0:
                stack.append(n)
    return res if len(res) == len(jobs) else []
    
